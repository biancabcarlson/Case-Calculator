# Case Calculator & Cross-Reference

A lightweight investigative utility that combines two repetitive case tasks into one workflow:

1. Calculate basic case financials.
2. Cross-reference identifiers across case events.

The goal is simple: reduce the manual busywork investigators perform after collecting case information so more time can be spent actually investigating it.

---

## Why I Built This

Investigators routinely have to do small calculations and manually compare information across notes, events, and evidence.

That often means:

- Adding exposure and loss figures by hand
- Calculating recovery or prevention rates
- Scanning events repeatedly for the same device, IP, email, phone number, or other identifier
- Keeping track of which events contain the same identifier
- Building a basic cross-reference matrix manually

None of that requires investigative judgment, but it still takes time.

This tool automates the mechanical portion of that work.

> Give me the information I already have. I'll organize the math and surface the repeated connections.

The investigator remains responsible for determining what those connections mean.

---

## Features

### Case Calculator

Enter:

- Gross exposure
- Confirmed loss
- Prevented loss
- Recovered amount

The calculator produces:

- Net loss
- Total financial mitigation
- Loss rate
- Prevention rate
- Recovery rate

For calculation purposes, confirmed loss and prevented loss are treated as non-overlapping portions of the gross exposure.

---

### Evidence Cross-Reference

Paste case events using a simple format:

```text
Event 1 | Device | DEVICE-A
Event 1 | IP | IP-EXAMPLE-01
Event 2 | Email | investigator@example.invalid
Event 2 | Device | DEVICE-B
Event 3 | Device | DEVICE-A
Event 3 | Email | investigator@example.invalid
