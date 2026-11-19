# UML Diagrams

| Field | Value |
|---|---|
| Project | CollecTree |
| Course | BM 321 / SENG 321 Software Engineering — Sprint 2 |
| Version | 0.2.0 (draft) |
| Owner (Accountable) | Berke Akman — Lead Software Architect |
| Consulted | Ata Eren Atlı (Implementation), Kemal Yusuf Ateşer (QA) |
| Informed | Elif Zahide Arat (Product Owner), Feyza Sayar (Scrum Master), Çağrı Baynal (DevOps) |
| Sources | [C4 model](c4-model.md), [domain model](domain-model.md), [`api/openapi.yaml`](../../api/openapi.yaml), [ADR-001](../adr/ADR-001-architecture-style-and-technology-stack.md) |

This document holds the UML behaviour diagrams of CollecTree. The structural UML diagrams are in the [domain model](domain-model.md): the class diagram (section 1), the database schema (section 2), and the offer state diagram (section 3.1).

| Diagram | Type | Section |
|---|---|---|
| Log in and call a protected endpoint | Sequence | 1 |
| Add an item to the collection | Sequence | 2 |
| Daily price job | Sequence | 3 |
| Accept an offer | Sequence | 4 |

**Participants** follow the C4 model, Level 3: the Web App container, the router (HTTP layer) and service (business rules) of each backend module, and the database. `BR-xx` refers to the business rules in the [domain model](domain-model.md#3-business-rules).

---

## 0 Conventions for every request

These rules apply to every flow below and are not repeated in each diagram.

| Topic | Rule |
|---|---|
| Transaction | Each HTTP request uses one database session and one transaction. The transaction is committed when the router returns successfully and rolled back on any error. |
| Errors | Every error is returned as `application/problem+json` with the `Problem` schema from `api/openapi.yaml` (`title`, `status`, `code`, `detail`). |
| Validation errors | FastAPI returns `422` for invalid request bodies by default. The contract uses `400`. A handler in `core` converts every validation error into `400` with the code `VALIDATION_ERROR`. |
| Authentication | Protected endpoints use one FastAPI dependency, `get_current_user` in `auth`. It returns `401` before the router code runs if the token is missing, invalid, or expired. |
| Lock order | When a request locks rows, it always locks **collection items first, in ascending id order, and offers after them**. All flows that change items or offers follow this order, so two requests can never wait for each other forever (deadlock). |

---

## 1 Log in and call a protected endpoint

```mermaid
sequenceDiagram
    autonumber
    actor C as Collector
    participant W as Web App
    participant AR as auth router
    participant AS as auth service
    participant DB as Database

    C->>W: Enter email and password, press "Log in"
    W->>AR: POST /api/v1/auth/login {email, password}
    AR->>AS: authenticate(email, password)
    AS->>DB: SELECT user WHERE lower(email) = lower(:email)
    DB-->>AS: user or nothing
    alt user not found or bcrypt check fails
        AS-->>AR: InvalidCredentials
        AR-->>W: 401 Problem (INVALID_CREDENTIALS)
        W-->>C: "Email or password is incorrect."
    else credentials are correct
        AS->>AS: create JWT (sub = user id, exp = now + JWT_EXPIRE_MINUTES), sign with JWT_SECRET
        AS-->>AR: access token
        AR-->>W: 200 {accessToken}
        W->>W: keep the token in memory and session storage
        W-->>C: Open "My collection"
    end

    Note over W,AR: Every later request sends the token

    W->>AR: GET /api/v1/auth/me (Authorization: Bearer token)
    AR->>AS: get_current_user(token)
    AS->>AS: verify signature and expiry
    alt token missing, invalid, or expired
        AS-->>AR: NotAuthenticated
        AR-->>W: 401 Problem (NOT_AUTHENTICATED)
        W-->>C: Go to "Log in"
    else token is valid
        AS->>DB: SELECT user WHERE id = :sub
        DB-->>AS: user
        AS-->>AR: current user
        AR-->>W: 200 User
    end
```

**Design notes**
- An unknown email and a wrong password return the **same** `401` and message, so an attacker cannot find out which emails are registered.
- Passwords are compared with bcrypt; the plain password is never stored or logged (NFR-SEC-01).
- The token only carries the user id and the expiry time. No personal data is put into the token, because anyone holding it can read it.

---

## 2 Add an item to the collection

```mermaid
sequenceDiagram
    autonumber
    actor C as Collector
    participant W as Web App
    participant CR as collection router
    participant AU as auth (get_current_user)
    participant CS as collection service
    participant CA as catalog service
    participant PS as pricing service
    participant DB as Database

    C->>W: Choose a model, enter price and date, press "Add"
    W->>CR: POST /api/v1/items {modelId, purchasePrice, purchaseDate, openForTrade}
    CR->>AU: get_current_user(token)
    AU-->>CR: current user (or 401)
    CR->>CR: validate body against NewCollectionItem
    alt body is invalid (missing field, negative price, bad date)
        CR-->>W: 400 Problem (VALIDATION_ERROR)
        W-->>C: Show the error under the field
    else body is valid
        CR->>CS: add_item(user, data)
        CS->>CA: get_model(modelId)
        CA->>DB: SELECT diecast_model WHERE id = :modelId
        DB-->>CA: model or nothing
        alt model does not exist
            CA-->>CS: ModelNotFound
            CS-->>CR: ModelNotFound
            CR-->>W: 404 Problem (MODEL_NOT_FOUND)
        else model exists
            CA-->>CS: model
            CS->>DB: INSERT collection_item (owner_id, model_id, price, date, open_for_trade, added_at)
            DB-->>CS: new item id
            CS-->>CR: item
            CR->>PS: current_price(modelId)
            PS->>DB: SELECT newest price_snapshot WHERE model_id = :modelId
            DB-->>PS: price or nothing
            PS-->>CR: currentPrice or null
            CR-->>W: 201 CollectionItem (with model and currentPrice)
            W-->>C: "Item added", back to "My collection"
        end
    end
```

**Design notes**
- `collection` checks the model through the `catalog` service and never reads the `diecast_models` table itself (C4 model, dependency rule 1).
- The router, not the `collection` service, adds `currentPrice` from `pricing`. `collection` is lower than `pricing` in the dependency order, so its service may not call `pricing` (dependency rules 2 and 3).
- The response is for the owner, so it contains the purchase price and date. The same item listed for another user leaves them out (BR-02).

---

## 3 Daily price job

```mermaid
sequenceDiagram
    autonumber
    participant SCH as APScheduler
    participant JOB as PriceJob (pricing)
    participant RP as TcmbRateProvider
    participant TC as TCMB
    participant CA as catalog service
    participant PP as PriceProvider (EbayPriceProvider)
    participant EB as eBay Browse API
    participant DB as Database

    SCH->>JOB: run() every day at 06:00 Europe/Istanbul
    JOB->>RP: rate_for(today)
    RP->>TC: GET /kurlar/today.xml
    alt rate published for today
        TC-->>RP: XML with USD ForexSelling
        RP-->>JOB: rate (is_stale = false)
    else weekend, holiday, or TCMB not reachable
        TC-->>RP: older date or error
        RP->>DB: SELECT newest exchange_rate
        DB-->>RP: last known rate
        RP-->>JOB: last rate (is_stale = true)
    end
    JOB->>DB: UPSERT exchange_rate (rate_date = today, usd_to_try, is_stale)

    JOB->>CA: list_models()
    CA->>DB: SELECT id, search_keyword FROM diecast_models
    DB-->>CA: models
    CA-->>JOB: models

    loop for each model
        JOB->>PP: median_price(search_keyword)
        PP->>PP: reuse the application token, or get a new one when it has expired
        PP->>EB: GET /item_summary/search?q=keyword&category_ids=...&filter=conditionIds:{1000},buyingOptions:{FIXED_PRICE}
        alt eBay answers
            EB-->>PP: item summaries
            PP->>PP: drop lots, bundles, loose, and custom items, then take the median USD price
            PP-->>JOB: median_usd, sample_size
            alt sample_size >= 5
                JOB->>DB: UPSERT price_snapshot (model_id, price_date = today, price_usd, price_try = price_usd x rate, rate_date, source = ebay, sample_size)
            else fewer than 5 listings
                JOB->>JOB: keep the last price, log "too few listings"
            end
        else timeout or error from eBay
            EB-->>PP: error
            PP-->>JOB: PriceUnavailable
            JOB->>JOB: keep the last price, log the error, continue with the next model
        end
    end
    JOB->>JOB: log the summary (updated, kept, failed)
```

**Design notes**
- One request per **model**, not per collection item: a model owned by many users is priced once (US-08).
- `UPSERT` on (`model_id`, `price_date`) means that running the job twice on one day does not create duplicate prices (BR-15).
- One failing model never stops the job (NFR-REL-01). A missing rate never stops the job either: the last rate is reused and marked as stale (NFR-REL-02).
- Nothing from eBay is stored except the median and the sample size: no listing, seller, or user data ([domain model](domain-model.md), section 2.2).
- With `PRICE_PROVIDER=seed`, `SeedPriceProvider` takes the place of `EbayPriceProvider` and returns the TRY price from the seed file. Tests always use it, so no test calls eBay or TCMB.

---

## 4 Accept an offer

The most complex flow. It must stay correct when two offers for the same item are accepted at the same moment (NFR-REL-03).

```mermaid
sequenceDiagram
    autonumber
    actor R as Receiver
    participant W as Web App
    participant OR as offers router
    participant AU as auth (get_current_user)
    participant OS as offers service
    participant CS as collection service
    participant DB as Database

    R->>W: Press "Accept" on a received offer
    W->>OR: PATCH /api/v1/offers/{offerId} {status: ACCEPTED}
    OR->>AU: get_current_user(token)
    AU-->>OR: current user (or 401)
    OR->>OS: change_status(user, offerId, ACCEPTED)

    OS->>DB: SELECT offer and its item ids (no lock yet)
    DB-->>OS: offer or nothing
    alt offer does not exist
        OS-->>OR: OfferNotFound
        OR-->>W: 404 Problem (OFFER_NOT_FOUND)
    else user is not the receiver
        OS-->>OR: Forbidden
        OR-->>W: 403 Problem (FORBIDDEN)
    else user is the receiver
        OS->>CS: lock_items(target and offered item ids)
        CS->>DB: SELECT collection_items WHERE id IN (...) ORDER BY id FOR UPDATE
        Note over CS,DB: A second request for the same items waits here until this transaction ends
        DB-->>CS: locked items
        CS-->>OS: items locked
        OS->>DB: SELECT offer WHERE id = :offerId FOR UPDATE
        DB-->>OS: offer with its current status
        alt status is no longer PENDING (for example cancelled by a parallel acceptance)
            OS-->>OR: OfferNotPending
            OR-->>W: 409 Problem (OFFER_NOT_PENDING)
            W-->>R: "This offer has already been answered."
        else status is PENDING
            OS->>DB: UPDATE offer SET status = ACCEPTED, closed_at = now()
            OS->>DB: UPDATE other PENDING offers with any locked item SET status = CANCELLED
            Note right of OS: BR-16
            OS->>CS: close_for_trade(item ids)
            CS->>DB: UPDATE collection_items SET open_for_trade = false WHERE id IN (...)
            Note right of CS: BR-17
            OS-->>OR: accepted offer
            OR-->>W: 200 Offer (status ACCEPTED)
            W-->>R: "Offer accepted" and the payment notice (BR-10)
        end
    end
    Note over OR,DB: The request transaction commits here, which releases all row locks
```

**Design notes**
- **Why items are locked before the offer:** if two requests locked their own offers first and then tried to cancel each other's offers, each would wait for the other forever. Locking the shared items first, in ascending id order, makes the second request wait at step 13 until the first one has finished. It then reads its own offer, finds it `CANCELLED`, and returns `409`.
- The status is read again **after** the locks are taken. The first read (step 6) is only used to find the items and to check the receiver; it can be out of date by the time the locks are granted.
- `offers` changes items only through the `collection` service (`lock_items`, `close_for_trade`), never by writing `collection_items` itself (C4 model, dependency rule 1).
- Rejecting and withdrawing use the same flow without the cancel and close steps. Removing an item (BR-05), closing it for trade (BR-18), and creating an offer lock the same item rows in the same order, so they cannot slip in between.
- Accepting moves no items and no money (BR-10). The web app shows the notice that the users complete the exchange themselves.
