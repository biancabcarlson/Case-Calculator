"""
Case Calculator

Answer y/n for each transaction ("is this fraud?") and it adds it all
up for you — declines, returns, and reversals included. You can still
call calculate_case() directly if you'd rather enter the four figures
by hand.

Public-safe demo using synthetic data only.
"""

from dataclasses import dataclass


# ---------------------------------------------------------------------
# Sample case: withdrawal activity from the `simulated-account` fixture,
# oldest to newest. `fraud` is just the starting suggestion — the
# investigator decides for real. Synthetic data only.
# ---------------------------------------------------------------------
SAMPLE_TRANSACTIONS = [
    {"date": "2026-05-18", "reference": "ACH-87255", "amount": 5000.00, "status": "pending",   "fraud": False},
    {"date": "2026-06-30", "reference": "ACH-87650", "amount": 300.00,  "status": "completed", "fraud": False},
    {"date": "2026-07-22", "reference": "ACH-87911", "amount": 1200.00, "status": "returned",  "fraud": False, "note": "R01 - insufficient funds"},
    {"date": "2026-08-15", "reference": "ACH-88147", "amount": 500.00,  "status": "completed", "fraud": False},
    {"date": "2026-08-31", "reference": "ACH-88300", "amount": 4800.00, "status": "pending",   "fraud": True,  "note": "New payee, added same week"},
]


@dataclass
class CaseResult:
    gross_exposure: float
    confirmed_loss: float
    prevented_loss: float
    recovered: float

    @property
    def total_loss_impact(self):
        return self.confirmed_loss + self.prevented_loss

    @property
    def total_mitigation(self):
        return self.prevented_loss + self.recovered

    @property
    def remaining_exposure(self):
        return self.gross_exposure - self.confirmed_loss - self.prevented_loss - self.recovered

    @property
    def recovery_percentage(self):
        if self.confirmed_loss == 0:
            return 0.0
        return (self.recovered / self.confirmed_loss) * 100

    @property
    def prevention_percentage(self):
        if self.gross_exposure == 0:
            return 0.0
        return (self.prevented_loss / self.gross_exposure) * 100

    @property
    def mitigation_percentage(self):
        if self.gross_exposure == 0:
            return 0.0
        return (self.total_mitigation / self.gross_exposure) * 100


def calculate_case(gross_exposure, confirmed_loss, prevented_loss, recovered):
    values = {
        "Gross Exposure": gross_exposure,
        "Confirmed Loss": confirmed_loss,
        "Prevented Loss": prevented_loss,
        "Recovered": recovered,
    }
    for label, value in values.items():
        if value < 0:
            raise ValueError(f"{label} cannot be negative.")

    return CaseResult(
        gross_exposure=gross_exposure,
        confirmed_loss=confirmed_loss,
        prevented_loss=prevented_loss,
        recovered=recovered,
    )


def calculate_case_from_marked(transactions):
    """Sum whichever transactions are marked ``fraud`` into the four figures.

    completed  -> confirmed loss (money's gone)
    pending, declined, returned -> prevented loss (never left)
    reversed   -> recovered (left, then came back)
    """
    gross = confirmed = prevented = recovered = 0.0
    for tx in transactions:
        if not tx.get("fraud"):
            continue
        amount = abs(tx["amount"])
        gross += amount
        if tx["status"] == "completed":
            confirmed += amount
        elif tx["status"] in ("pending", "declined", "returned"):
            prevented += amount
        elif tx["status"] == "reversed":
            recovered += amount

    return calculate_case(gross, confirmed, prevented, recovered)


def money(value):
    return f"${value:,.2f}"


def print_results(result):
    print("\nCASE CALCULATOR")
    print("=" * 45)

    print(f"Gross Exposure:       {money(result.gross_exposure)}")
    print(f"Confirmed Loss:       {money(result.confirmed_loss)}")
    print(f"Prevented Loss:       {money(result.prevented_loss)}")
    print(f"Recovered:            {money(result.recovered)}")

    print("\nRESULTS")
    print("-" * 45)
    print(f"Total Loss Impact:    {money(result.total_loss_impact)}")
    print(f"Total Mitigation:     {money(result.total_mitigation)}")
    print(f"Remaining Exposure:   {money(result.remaining_exposure)}")
    print(f"Recovery Rate:        {result.recovery_percentage:.2f}%")
    print(f"Prevention Rate:      {result.prevention_percentage:.2f}%")
    print(f"Mitigation Rate:      {result.mitigation_percentage:.2f}%")


if __name__ == "__main__":
    print("Mark each transaction as fraud or not (Enter accepts the suggestion in brackets).\n")

    for tx in SAMPLE_TRANSACTIONS:
        default = "y" if tx["fraud"] else "n"
        note = f" — {tx['note']}" if tx.get("note") else ""
        prompt = f"{tx['date']}  {tx['reference']}  {money(tx['amount'])}  ({tx['status']}){note}  fraud? [{default}]: "
        answer = input(prompt).strip().lower() or default
        tx["fraud"] = answer.startswith("y")

    case = calculate_case_from_marked(SAMPLE_TRANSACTIONS)
    print_results(case)
