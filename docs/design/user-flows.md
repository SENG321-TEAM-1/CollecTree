# User Flows

| Field | Value |
|---|---|
| Project | CollecTree |
| Course | BM 321 / SENG 321 Software Engineering, Sprint 2 |
| Version | 0.2.0 |
| Owner (Accountable) | Ata Eren Atlı, Implementation and Integration Engineer |
| Consulted | Berke Akman (Architect), Kemal Yusuf Ateşer (QA), Elif Zahide Arat (Product Owner) |
| Sources | [`api/openapi.yaml`](../../api/openapi.yaml), [domain model](../architecture/domain-model.md) (business rules BR-01 to BR-19), [C4 model](../architecture/c4-model.md) |

This document shows how a user moves through the main screens of CollecTree. Each flow names the API operation behind every step, the status code of every error, and the business rule (BR-xx) that causes it. The Figma prototype, the frontend, and the API tests use the same steps and the same on-screen messages.

**Notation:** rectangles are screens or system actions, diamonds are decisions, and red boxes are error or empty states shown to the user. Operation IDs from `api/openapi.yaml` are written in brackets, for example `[addItem]`.

---

## 1 On-screen messages

The flows, the Figma screens, and the API tests use exactly these messages.

| Case | API | Rule | Message on screen |
|---|---|---|---|
| Username or email already used | 409 | BR-01 | `This username or email is already registered.` |
| Wrong email or password | 401 | – | `Email or password is incorrect.` |
| Item in a pending offer cannot be removed | 409 | BR-05 | `This item is part of a pending offer. Accept, reject, or withdraw the offer first.` |
| Item cannot be closed for trade | 409 | BR-18 | `This item has pending offers. Accept or reject them before closing it for trade.` |
| Item not open for trade | 409 | BR-07 | `This item is not open for trade.` |
| Offer on own item | 403 | BR-07 | `You cannot make an offer for your own item.` |
| Empty offer | 400 | BR-06 | `Add at least one of your items or a cash amount.` |
| Offer no longer pending | 409 | BR-09 | `This offer has already been answered.` |
| Conversation already exists | 409 | BR-12 | No message: the existing conversation is opened instead. |
| Empty collection | – | – | `No items yet. Add your first model.` |

Field validation errors (`400`) are shown under the field that caused them, using the `detail` text of the `Problem` response.

---

## 2 Register and log in

Operations: `register`, `login`.

```mermaid
flowchart TD
    A["Landing page"] --> B{"Has an account?"}
    B -->|"No"| C["Register screen"]
    B -->|"Yes"| L["Login screen"]

    C --> D["Enter username, email, and password"]
    D --> E{"Fields valid?<br/>username 3-30 chars,<br/>valid email, password 8+ chars"}
    E -->|"No"| F["Show the error under the field (400)"]
    F --> D
    E -->|"Yes"| G["Send [register]"]
    G --> H{"Username or email<br/>already used?"}
    H -->|"Yes, 409 (BR-01)"| I["Show 'This username or email<br/>is already registered.'"]
    I --> D
    H -->|"No, 201"| K["Store the token"]

    L --> M["Enter email and password"]
    M --> N["Send [login]"]
    N --> O{"Correct?"}
    O -->|"No, 401"| P["Show 'Email or password<br/>is incorrect.'"]
    P --> M
    O -->|"Yes, 200"| K

    K --> Q["My collection"]

    classDef error fill:#fde2e1,stroke:#c0392b,color:#000
    class F,I,P error
```

---

## 3 Add an item

Operations: `listUserItems`, `searchModels`, `addItem`.

```mermaid
flowchart TD
    A["My collection [listUserItems]"] --> B{"Any items?"}
    B -->|"No"| C["Show 'No items yet.<br/>Add your first model.'"]
    B -->|"Yes"| D["Show the item cards"]
    C --> E["Click 'Add item'"]
    D --> E

    E --> F["Type a model name, brand, or series"]
    F --> G["Search the catalogue [searchModels]"]
    G --> H{"Model found?"}
    H -->|"No"| I["Show 'No models found'"]
    I --> F
    H -->|"Yes"| J["Select the model"]

    J --> K["Enter purchase price, purchase date,<br/>and 'Open for trade'"]
    K --> L{"Valid?<br/>price is 0 or more,<br/>date is not in the future"}
    L -->|"No, 400"| M["Show the error under the field"]
    M --> K
    L -->|"Yes"| N["Send [addItem]"]
    N --> O["Item added (201),<br/>back to My collection"]

    classDef error fill:#fde2e1,stroke:#c0392b,color:#000
    class C,I,M error
```

---

## 4 Edit or remove an item

Operations: `updateItem` (`PATCH /items/{itemId}`), `deleteItem`.

Only the owner sees the edit and remove actions (BR-03, BR-19). The model of an item cannot be changed; the owner removes the item and adds a new one instead (BR-19).

```mermaid
flowchart TD
    A["My collection"] --> B["Open an item"]
    B --> C{"Action"}

    C -->|"Edit"| D["Edit screen:<br/>purchase price, purchase date,<br/>open for trade"]
    D --> E{"Fields valid?"}
    E -->|"No, 400"| F["Show the error under the field"]
    F --> D
    E -->|"Yes"| G["Send [updateItem]"]
    G --> H{"Closing the item for trade<br/>while it has pending offers?"}
    H -->|"Yes, 409 (BR-18)"| I["Show 'This item has pending offers.<br/>Accept or reject them before<br/>closing it for trade.'"]
    I --> J["Link to My offers"]
    H -->|"No, 200"| K["Changes saved,<br/>back to the item"]

    C -->|"Remove"| L["Confirm dialog:<br/>'Remove this item from your collection?'"]
    L -->|"Cancel"| B
    L -->|"Remove"| M["Send [deleteItem]"]
    M --> N{"Item in a pending offer?"}
    N -->|"Yes, 409 (BR-05)"| O["Show 'This item is part of a pending offer.<br/>Accept, reject, or withdraw<br/>the offer first.'"]
    O --> J
    N -->|"No, 204"| P["Item removed,<br/>back to My collection"]

    classDef error fill:#fde2e1,stroke:#c0392b,color:#000
    class F,I,O error
```

---

## 5 View the portfolio

Operations: `getMyPortfolio`, `getMyPortfolioHistory`, `getPriceHistory`.

```mermaid
flowchart TD
    A["Portfolio dashboard"] --> B["Load totals [getMyPortfolio]"]
    B --> C{"Any items?"}
    C -->|"No"| D["Show 'No items yet.<br/>Add your first model.'<br/>with an 'Add item' button"]
    C -->|"Yes"| E["Show total purchase price,<br/>total current value,<br/>and profit or loss in TRY"]

    E --> F["Load the chart [getMyPortfolioHistory]"]
    F --> G["Show the value and purchase price lines;<br/>the user can change the date range"]
    G --> H{"Range valid?<br/>'from' is not after 'to'"}
    H -->|"No, 400"| I["Show the error next to the date picker"]
    I --> G
    H -->|"Yes"| J["Redraw the chart"]

    E --> K["Item list with current price"]
    K --> L{"Model has a market price?"}
    L -->|"No (BR-14)"| M["Show the purchase price as the value,<br/>labelled 'No market price yet'"]
    L -->|"Yes"| N["Show the price with<br/>'International listing price (eBay),<br/>converted to TRY'"]
    N --> O["Open the model"]
    O --> P["Model price history [getPriceHistory]"]

    classDef error fill:#fde2e1,stroke:#c0392b,color:#000
    class D,I error
```

A model without a market price adds zero profit or loss, because its purchase price is used as its current value (BR-14).

---

## 6 Browse a collector and make an offer

Operations: `getUserProfile`, `listUserItems`, `createOffer`.

Purchase prices and purchase dates of other users are never shown (BR-02).

```mermaid
flowchart TD
    A["Public profile [getUserProfile]"] --> B["Public collection [listUserItems]<br/>no purchase prices (BR-02)"]
    B --> C["Click 'Make offer' on an item"]
    C --> D{"Logged in?"}
    D -->|"No"| E["Login screen, then back to the item"]
    E --> C
    D -->|"Yes"| F["Make offer screen"]

    F --> G["Choose my items and/or<br/>enter a cash amount in TRY"]
    G --> H["Notice: 'Payment and delivery are handled<br/>by the users outside the platform.' (BR-10)"]
    H --> I["Send [createOffer]"]
    I --> J{"Result"}

    J -->|"400 (BR-06)"| K["Show 'Add at least one of your items<br/>or a cash amount.'"]
    K --> G
    J -->|"403 (BR-07)"| L["Show 'You cannot make an offer<br/>for your own item.'"]
    J -->|"409 (BR-07)"| M["Show 'This item is not open for trade.'"]
    J -->|"201"| N["Offer sent with status Pending,<br/>open My offers"]

    classDef error fill:#fde2e1,stroke:#c0392b,color:#000
    class K,L,M error
```

In the interface, the "Make offer" button is hidden on the user's own items and on items that are not open for trade. The 403 and 409 errors can still happen if the data changed after the page was loaded, so the screen must show them.

---

## 7 Respond to an offer

Operations: `listMyOffers`, `updateOfferStatus`.

Offer statuses on screen: **Pending**, **Accepted**, **Rejected**, **Withdrawn**, **Cancelled**.

```mermaid
flowchart TD
    A["My offers [listMyOffers]"] --> B{"Tab"}
    B -->|"Received"| C["Pending offer for my item"]
    B -->|"Sent"| D["Pending offer I made"]

    C --> E{"Action"}
    E -->|"Accept"| F["Send [updateOfferStatus] ACCEPTED"]
    E -->|"Reject"| G["Send [updateOfferStatus] REJECTED"]
    D --> H["Withdraw: send<br/>[updateOfferStatus] WITHDRAWN"]

    F --> I{"Still pending?"}
    G --> I
    H --> I
    I -->|"No, 409 (BR-09)"| J["Show 'This offer has already been answered.'<br/>and reload the list"]
    I -->|"Yes, 200"| K{"New status"}

    K -->|"Accepted"| L["Other pending offers with these items<br/>become Cancelled (BR-16)"]
    L --> M["All items in the offer are<br/>closed for trade (BR-17)"]
    M --> N["Show 'Accepted' and the notice:<br/>'Payment and delivery are handled<br/>by the users outside the platform.' (BR-10)"]
    K -->|"Rejected or Withdrawn"| O["Show the new status badge"]

    classDef error fill:#fde2e1,stroke:#c0392b,color:#000
    class J error
```

Only the receiver sees Accept and Reject; only the sender sees Withdraw (BR-09). Users never set **Cancelled**; only the system sets it (BR-09, BR-16).

---

## 8 Messaging

Operations: `listConversations`, `startConversation`, `listMessages`, `sendMessage`.

```mermaid
flowchart TD
    A["Public profile"] --> B["Click 'Send message'"]
    B --> C["Send [startConversation]"]
    C --> D{"Conversation with this user<br/>already exists?"}
    D -->|"Yes, 409 (BR-12)"| E["Open the existing conversation<br/>(no error shown)"]
    D -->|"No, 201"| F["Open the new conversation"]

    G["Conversations list [listConversations]"] --> H{"Any conversations?"}
    H -->|"No"| I["Show 'No conversations yet'"]
    H -->|"Yes"| J["Open a conversation"]

    E --> K["Conversation screen [listMessages]"]
    F --> K
    J --> K

    K --> L["Type a message"]
    L --> M{"1 to 1000 characters?"}
    M -->|"No, 400"| N["Show the error under the text box"]
    N --> L
    M -->|"Yes"| O["Send [sendMessage]"]
    O --> P["Message added to the list (201)"]
    P --> Q["The list is refreshed by polling"]
    Q --> K

    classDef error fill:#fde2e1,stroke:#c0392b,color:#000
    class I,N error
```

Only the two users of a conversation can read or send its messages (BR-11). Messages are refreshed by polling, not WebSocket (ADR-001).

---

## 9 Figma prototype and screens

- **Figma file (`CollecTree – Sprint 2 Prototype`, view and comment):** [https://www.figma.com/design/kpeIcUYw4x5FKOvrRbYFaM/CollecTree-Sprint-2-Prototype?node-id=24-2](https://www.figma.com/design/kpeIcUYw4x5FKOvrRbYFaM/CollecTree-Sprint-2-Prototype?node-id=24-2)
- **Interactive prototype (`Main Collector Journey`: Login → My Collection → Add Item → Portfolio Dashboard → Model Price History → Public Profile → Make Offer → My Offers → Conversations List → Conversation):** [https://www.figma.com/proto/kpeIcUYw4x5FKOvrRbYFaM/CollecTree-Sprint-2-Prototype?page-id=24%3A2&node-id=24-4&starting-point-node-id=24%3A4](https://www.figma.com/proto/kpeIcUYw4x5FKOvrRbYFaM/CollecTree-Sprint-2-Prototype?page-id=24%3A2&node-id=24-4&starting-point-node-id=24%3A4)

All 12 desktop screens (`1440×900`) are stored in [`docs/design/screens/`](screens/) and map to the API operations as follows:

| # | Screen | File | API operations | Flows |
|---|---|---|---|---|
| 1 | Login | [`01-login.png`](screens/01-login.png) / [`01-login.svg`](screens/01-login.svg) | `login` | Section 2 |
| 2 | Register | [`02-register.png`](screens/02-register.png) / [`02-register.svg`](screens/02-register.svg) | `register` | Section 2 |
| 3 | My collection (list + brand/scale/series filters) | [`03-my-collection.png`](screens/03-my-collection.png) / [`03-my-collection.svg`](screens/03-my-collection.svg) | `listUserItems` | Sections 3, 4 |
| 4 | Add item (catalogue search + price/date form) | [`04-add-item.png`](screens/04-add-item.png) / [`04-add-item.svg`](screens/04-add-item.svg) | `searchModels`, `addItem` | Section 3 |
| 5 | Edit item (price, date, open for trade) | [`05-edit-item.png`](screens/05-edit-item.png) / [`05-edit-item.svg`](screens/05-edit-item.svg) | `updateItem`, `deleteItem` | Section 4 |
| 6 | Portfolio dashboard (total value, profit/loss, history chart) | [`06-portfolio-dashboard.png`](screens/06-portfolio-dashboard.png) / [`06-portfolio-dashboard.svg`](screens/06-portfolio-dashboard.svg) | `getMyPortfolio`, `getMyPortfolioHistory` | Section 5 |
| 7 | Model price history | [`07-model-price-history.png`](screens/07-model-price-history.png) / [`07-model-price-history.svg`](screens/07-model-price-history.svg) | `getPriceHistory` | Section 5 |
| 8 | Public profile and collection (no purchase prices) | [`08-public-profile.png`](screens/08-public-profile.png) / [`08-public-profile.svg`](screens/08-public-profile.svg) | `getUserProfile`, `listUserItems` | Sections 6, 8 |
| 9 | Make offer (choose my items and/or cash) | [`09-make-offer.png`](screens/09-make-offer.png) / [`09-make-offer.svg`](screens/09-make-offer.svg) | `createOffer` | Section 6 |
| 10 | My offers (sent / received, status badges) | [`10-my-offers.png`](screens/10-my-offers.png) / [`10-my-offers.svg`](screens/10-my-offers.svg) | `listMyOffers`, `updateOfferStatus` | Section 7 |
| 11 | Conversations list | [`11-conversations-list.png`](screens/11-conversations-list.png) / [`11-conversations-list.svg`](screens/11-conversations-list.svg) | `listConversations`, `startConversation` | Section 8 |
| 12 | Conversation | [`12-conversation.png`](screens/12-conversation.png) / [`12-conversation.svg`](screens/12-conversation.svg) | `listMessages`, `sendMessage` | Section 8 |

### 9.1 Screen previews

#### 1. Login (`login`)
![Login](screens/01-login.png)

#### 2. Register (`register`)
![Register](screens/02-register.png)

#### 3. My Collection (`listUserItems`)
![My Collection](screens/03-my-collection.png)

#### 4. Add Item (`searchModels`, `addItem`)
![Add Item](screens/04-add-item.png)

#### 5. Edit Item (`updateItem`, `deleteItem`)
![Edit Item](screens/05-edit-item.png)

#### 6. Portfolio Dashboard (`getMyPortfolio`, `getMyPortfolioHistory`)
![Portfolio Dashboard](screens/06-portfolio-dashboard.png)

#### 7. Model Price History (`getPriceHistory`)
![Model Price History](screens/07-model-price-history.png)

#### 8. Public Profile and Collection (`getUserProfile`, `listUserItems`)
![Public Profile](screens/08-public-profile.png)

#### 9. Make Offer (`createOffer`)
![Make Offer](screens/09-make-offer.png)

#### 10. My Offers (`listMyOffers`, `updateOfferStatus`)
![My Offers](screens/10-my-offers.png)

#### 11. Conversations List (`listConversations`, `startConversation`)
![Conversations List](screens/11-conversations-list.png)

#### 12. Conversation (`listMessages`, `sendMessage`)
![Conversation](screens/12-conversation.png)
