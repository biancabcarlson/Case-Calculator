# Case Calculator

**🔗 Live demo:** https://biancabcarlson.github.io/Case-Calculator/

Pick a date range for a case and this pulls the flagged activity and
does the math — gross exposure, confirmed loss, prevented loss,
recovered, remaining exposure, and the percentages that go with them.
You can also type the four figures in by hand.

## Quick start

The page loads with a real example already filled in — a $4,800
withdrawal to a newly added payee, held before it settled. Change
the date range and hit **Pull Figures for This Period** to see it
recalculate, or edit the four numbers directly.

## The four figures

1. **Gross Exposure** — total amount at risk.
2. **Confirmed Loss** — the part that's actually gone.
3. **Prevented Loss** — the part stopped before it became a loss.
4. **Recovered** — funds gotten back after the fact.

From those, it works out total loss impact, total mitigation,
remaining exposure, and the recovery / prevention / mitigation rates.

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

Prompts for a start/end date (press Enter to use the example case's
range) and prints the same figures the web version shows.

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
