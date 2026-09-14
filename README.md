# Case Calculator

**🔗 Live demo:** https://biancabcarlson.github.io/Case-Calculator/

Enter a case's core financial figures and get the derived numbers — loss impact, mitigation, remaining exposure, recovery/prevention percentages — without doing the arithmetic by hand.

## Inputs → outputs

You provide four figures:

- **Gross Exposure** — total amount at risk
- **Confirmed Loss** — the portion actually lost
- **Prevented Loss** — the portion stopped before it became a loss
- **Recovered** — funds recovered after the fact

The calculator derives: total loss impact, total mitigation, remaining exposure, and recovery/prevention/combined-mitigation percentages.

## Web demo vs. CLI

- **Web demo:** loads the case's transaction history and lets you check any transaction to include it — which bucket a checked transaction counts toward comes from the case record, not a per-row choice. The four input fields auto-fill from what's checked but stay manually editable (as currency, with $ and commas); editing after a calculation marks the results stale until you recalculate. "Copy results" copies the figures as plain text for a report.
- **CLI:** the four figures are set directly in the script's `__main__` block (currently the CASE-DEMO-0091 numbers below) — edit them for your own case, since there's no transaction table on the command line.

## Example

Case CASE-DEMO-0091: a $4,800 withdrawal to a newly added external payee was flagged and held before it settled.

| Figure | Amount |
|---|---|
| Gross Exposure | $4,800 |
| Confirmed Loss | $0 |
| Prevented Loss | $4,800 |
| Recovered | $0 |

→ a full prevention with no confirmed loss, once the derived figures are calculated.

## Privacy Mode

The 🔒 Privacy Mode toggle (top right, shared across the suite via `localStorage`) is here for consistency with the other tools — this calculator doesn't display any PII, so there's nothing for it to blur.

## Files

```
case-calculator/
├── README.md
├── case_calculator.py
└── index.html
```

## Running it

```
python case_calculator.py
```

Python 3, standard library only. Or open `index.html` directly — no server, framework, or dependencies needed.

## Public-safe by design

No fraud rules, risk thresholds, scoring, internal procedures, or real customer/transaction data — just the arithmetic. Works entirely on synthetic or user-supplied figures.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/) *(this repo)*
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/)
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
