# Case Calculator

**🔗 Live demo:** https://biancabcarlson.github.io/Case-Calculator/

A lightweight investigator utility for quickly calculating and summarizing case-level financial figures without manually working through the math.

## Why I Built This

Investigations often involve repeatedly calculating figures such as exposure, loss, prevention, recovery, and remaining impact. The math itself is simple, but doing it manually across multiple cases creates unnecessary work and increases the chance of calculation errors.

The Case Calculator handles the mechanical calculations so the investigator can spend their time interpreting the numbers rather than calculating them.

## What It Does

Enter the relevant case figures and the calculator automatically determines:

* Gross exposure
* Confirmed loss
* Prevented loss
* Recovered amount
* Total loss impact
* Total mitigation
* Remaining exposure
* Recovery percentage
* Prevention percentage
* Combined mitigation percentage

## How It Works

There are two ways to get to the same four case-level figures:

- **Web demo:** pulls in the case's transaction history and lets the investigator
  check which transactions count toward the case at all — which bucket a checked
  transaction counts toward (confirmed loss / prevented loss / recovered) comes
  from the case record itself, not a per-row choice. Returned/failed transactions
  can't be checked, since they never completed and never count. Pending
  transactions can be checked but are marked "pending — may change" until they
  clear. Gross Exposure, Confirmed Loss, Prevented Loss, and Recovered are
  auto-filled from the checked transactions, and remain manually editable —
  editing anything after a calculation flags the results as stale until you
  recalculate.
- **Python CLI:** the four figures are entered directly, since there's no
  transaction table in a command-line context.

1. Gross Exposure — the total amount at risk or exposed.
2. Confirmed Loss — the portion determined to have been lost.
3. Prevented Loss — the portion prevented from becoming a loss.
4. Recovered — funds recovered after the loss occurred.

Either way, the calculator then performs the associated calculations automatically.

## Example

Sample scenario — Case CASE-DEMO-0091 (see the mock account used across this tool series): a $4,800 withdrawal to a newly added external payee was flagged and held before it could settle.

| Figure | Amount |
|---|---|
| Gross Exposure | $4,800 |
| Confirmed Loss | $0 |
| Prevented Loss | $4,800 |
| Recovered | $0 |

The calculator automatically calculates the resulting loss impact, mitigation, remaining exposure, and applicable percentages — in this case, a full prevention with no confirmed loss.

## Why It Helps

The value isn't the complexity of the math. It's removing the repetitive calculation from the investigative workflow.

Instead of repeatedly:

* Pulling figures together
* Opening a calculator or spreadsheet
* Performing multiple calculations
* Recalculating percentages
* Checking the arithmetic

the investigator enters the figures once and receives the calculated results immediately.

This leaves the investigator to focus on what the numbers mean and what action, if any, should follow.

## Public-Safe by Design

This project is intentionally built as a generic investigative utility.

It does not contain:

* Fraud detection rules
* Risk thresholds
* Fraud scoring
* Proprietary investigative methodology
* Internal company procedures
* Customer information
* Real transaction data
* Credentials or API keys
* Fraud-enabling or evasion logic

The project can be demonstrated entirely with synthetic or user-provided figures.

## Files

```
case-calculator/
├── README.md
├── case_calculator.py
└── index.html
```

## Python Version

Requires Python 3.

Run:

```
python case_calculator.py
```

The Python implementation uses only the standard library.

## Web Demo

Open `index.html` in a browser, or use the live demo link above.

No server, framework, package installation, or external dependencies are required.

## Design Philosophy

The goal is to identify repetitive mechanical work within an investigation and remove it.

An investigator shouldn't have to spend time performing calculations that a computer can complete instantly and consistently. The calculator handles the arithmetic while the investigator remains responsible for interpreting the results and making the investigative decision.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/) *(this repo)*
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/)
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
