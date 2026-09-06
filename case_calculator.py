"""
Case Calculator

Enter a date range for the case and this pulls the flagged activity
in that window and does the math for you. You can still type in the
four figures by hand if you'd rather.

Public-safe demo using synthetic data only.
"""

from dataclasses import dataclass
from datetime import date


# ---------------------------------------------------------------------
# Sample case: flagged ACH activity from the `simulated-account` fixture.
# Synthetic data only — no real accounts, names, or transactions.
# ---------------------------------------------------------------------
SAMPLE_TRANSACTIONS = [
    {"date": "2026-09-01", "type": "deposit",    "amount": 2400.00, "status": "completed", "flagged": False, "reference": "ACH-88213"},
    {"date": "2026-08-31", "type": "withdrawal", "amount": 4800.00, "status": "pending",   "flagged": True,  "reference": "ACH-88300", "note": "New payee, added same week"},
    {"date": "2026-08-15", "type": "withdrawal", "amount": 500.00,  "status": "completed", "flagged": False, "reference": "ACH-88147"},
    {"date": "2026-08-01", "type": "deposit",    "amount": 2400.00, "status": "completed", "flagged": False, "reference": "ACH-88022"},
]

DEFAULT_START = "2026-08-01"
DEFAULT_END = "2026-09-05"


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


def pull_figures_for_range(start, end, transactions=SAMPLE_TRANSACTIONS):
    """Sum the flagged activity in [start, end] into the four case figures.

    Pending flagged withdrawals count as prevented loss (stopped before
    they settled). Completed flagged withdrawals count as confirmed loss.
    Everything else is left for the investigator to add manually.
    """
    start_d, end_d = date.fromisoformat(start), date.fromisoformat(end)

    gross = confirmed = prevented = recovered = 0.0
    for tx in transactions:
        tx_date = date.fromisoformat(tx["date"])
        if not (start_d <= tx_date <= end_d) or not tx.get("flagged"):
            continue
        amount = abs(tx["amount"])
        gross += amount
        if tx["status"] == "completed":
            confirmed += amount
        elif tx["status"] == "pending":
            prevented += amount
        elif tx["status"] == "recovered":
            recovered += amount

    return calculate_case(gross, confirmed, prevented, recovered)


def money(value):
    return f"${value:,.2f}"


def print_results(result, start=None, end=None):
    print("\nCASE CALCULATOR")
    print("=" * 45)
    if start and end:
        print(f"Case period:          {start} to {end}")

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
    # Defaults to the demo case's date range — press Enter twice to use it.
    start = input(f"Start date [{DEFAULT_START}]: ").strip() or DEFAULT_START
    end = input(f"End date   [{DEFAULT_END}]: ").strip() or DEFAULT_END

    case = pull_figures_for_range(start, end)
    print_results(case, start, end)
