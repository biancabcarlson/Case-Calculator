# Northfield Bank — Account Hub (Mock)

Synthetic test account for exercising downstream repos. No real customer, account, or PII.

## Files

- `account-hub.html` — visual reference for the data
- `account-data.json` — the data as a structured fixture

## Usage

Copy `account-data.json` into a project's fixtures directory (e.g. `test/fixtures/`) and load it as JSON:

```js
const account = require('./account-data.json');
```

```python
import json
account = json.load(open("account-data.json"))
```

## Data structure

| Key | Contents |
|---|---|
| `profile` | Name, account number, phone, email, address, status |
| `activityLog` | Non-transactional events — account creation, KYC, ACH linking, address/email changes |
| `paymentMethods` | Bank accounts, cards, crypto wallets |
| `achTransactions` | Deposits/withdrawals, including a returned and a pending transaction |
| `cryptoActivity` | Buys/sells/transfers, including one flagged transaction |
| `loginLog` | Login attempts, including a failed lockout and an incomplete MFA challenge |
| `security` | KYC, 2FA, trusted devices, risk flags |
| `documents` | Statements, tax documents |

## Extending

- Additional test accounts / edge cases: duplicate the JSON structure with different values.
- Mock API endpoint instead of a static file: not yet implemented.
