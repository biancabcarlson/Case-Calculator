Case Calculator

A lightweight investigator utility for quickly calculating and summarizing case-level financial figures without manually working through the math.

Why I Built This

Investigations often involve repeatedly calculating figures such as exposure, loss, prevention, recovery, and remaining impact. The math itself is simple, but doing it manually across multiple cases creates unnecessary work and increases the chance of calculation errors.

The Case Calculator handles the mechanical calculations so the investigator can spend their time interpreting the numbers rather than calculating them.

What It Does

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

Example

Given:

* Gross Exposure: $2,100
* Confirmed Loss: $400
* Prevented Loss: $300
* Recovered: $100

The calculator produces the corresponding case-level totals and percentages automatically.

Public-Safe by Design

This project is intentionally designed as a generic investigative utility.

It does not contain:

* Fraud detection rules
* Risk thresholds
* Scoring logic
* Internal investigation procedures
* Proprietary workflows
* Customer information
* Transaction data
* Credentials or API keys
* Evasion or fraud-enabling logic

The calculations are generic and can be applied to synthetic or user-provided figures.

Files

case-calculator/
├── README.md
├── case_calculator.py
└── index.html

Python

Requires Python 3.

Run:

python case_calculator.py

The Python version runs a synthetic example and prints the calculated results to the terminal.

Web Demo

Open index.html in a browser.

No server, framework, package installation, or external dependency is required.

Design Philosophy

The goal is simple: identify repetitive mechanical work within an investigation and remove it.

The investigator should not have to spend time performing calculations that a computer can complete instantly and consistently. The tool handles the arithmetic while the investigator remains responsible for interpreting the results and making the investigative decision.
