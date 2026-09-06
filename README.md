# Case Calculator

**🔗 Live demo:** https://biancabcarlson.github.io/Case-Calculator/

Check off which transactions are fraud and it adds up the exposure,
loss, and recovery for you — declines, returns, and reversals all
included. No manual math.

## Quick start

The page loads with a real example already filled in: five withdrawals,
oldest to newest, with the one that's actually fraud pre-checked.
Check or uncheck any transaction and the figures below update
automatically. You can also edit the four numbers directly.

## How it sums things up

For each transaction you check:

| Status | Counts as |
|---|---|
| Completed | Confirmed loss (money's gone) |
| Pending, declined, or returned | Prevented loss (it never left) |
| Reversed | Recovered (it left, then came back) |

From those it works out total loss impact, total mitigation, remaining
exposure, and the recovery / prevention / mitigation rates.

## Public-safe by design

Generic investigative utility — no fraud rules, risk thresholds,
scoring, internal procedures, real customer data, or credentials.
Runs entirely client-side; nothing is uploaded.

## Files

```
case-calculator/
├── README.md
├── case_calculator.py
└── index.html
```

## Python version

Requires Python 3, standard library only.

```
python case_calculator.py
```

Walks through each transaction and asks fraud y/n (Enter accepts the
suggestion), then prints the same figures the web version shows.

## Web demo

Open `index.html` in a browser, or use the live demo link above. No
install needed.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/) *(this repo)*
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/)
- [OSINT Query Fanout](https://biancabcarlson.github.io/OSINT-Query-Fanout/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
