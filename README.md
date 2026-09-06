# Case-Calculator
# Case Calculator

A lightweight investigative utility that handles the repetitive arithmetic investigators perform when quantifying case impact.

## The Problem

Investigators routinely calculate things like:

- Gross exposure
- Confirmed loss
- Prevented loss
- Recovered funds
- Net loss
- Loss percentage
- Prevention percentage
- Recovery percentage
- Remaining exposure

None of that is investigation.

It is arithmetic.

Case Calculator turns those figures into a standardized case-impact snapshot so the investigator can spend their time interpreting the case instead of repeatedly calculating it.

## What It Does

Enter four figures:

1. Gross Exposure
2. Confirmed Loss
3. Prevented Loss
4. Recovered Amount

The calculator automatically produces:

- Net Loss
- Loss Rate
- Prevention Rate
- Recovery Rate
- Remaining Exposure
- Avoided Loss
- Overall Case Outcome

The tool also validates the relationships between the figures and prevents mathematically inconsistent inputs.

## Example

Given:

- Gross Exposure: `$12,500`
- Confirmed Loss: `$4,000`
- Prevented Loss: `$7,000`
- Recovered Amount: `$1,500`

The calculator produces:

- Net Loss: `$2,500`
- Loss Rate: `32.00%`
- Prevention Rate: `56.00%`
- Recovery Rate: `37.50%`
- Remaining Exposure: `$1,500`
- Avoided Loss: `$7,000`

## Files

```text
case-calculator/
├── README.md
├── case_calculator.py
└── index.html
