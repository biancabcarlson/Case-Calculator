# Northfield Bank — Account Hub (Mock)

A synthetic test account for exercising your other repos. No real customer, account, or PII.

## Files

- `account-hub.html` — visual reference for the data (open in a browser)
- `account-data.json` — the same data as structured fixture data

## Using it in another repo

Copy `account-data.json` into that repo (e.g. `test/fixtures/`) and load it however that project reads test data — most languages can just parse the file directly:

```js
const account = require('./account-data.json');
```

```python
import json
account = json.load(open("account-data.json"))
```

## What's in the data

- `profile` — name, account number, phone, email, address, status
- `activityLog` — non-transactional events (account created, KYC, ACH linked, address/email changes, etc.)
- `paymentMethods` — bank accounts, cards, crypto wallets
- `achTransactions` — deposits/withdrawals, including a returned and a pending transaction
- `cryptoActivity` — buys/sells/transfers, including one flagged transaction
- `loginLog` — login attempts, including a failed lockout and an incomplete MFA challenge
- `security` — KYC, 2FA, trusted devices, risk flags
- `documents` — statements, tax docs

## If you need more later

- Multiple test accounts / edge cases → duplicate the JSON structure with different values
- A live endpoint your repos can call instead of a static file → say the word once you know what's making the request (language, expected routes, etc.)
