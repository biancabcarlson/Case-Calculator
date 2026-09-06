"""
Case Calculator

A lightweight investigator utility for calculating
case-level financial figures.

Public-safe demo using synthetic data only.
"""

from dataclasses import dataclass


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


def calculate_case(
    gross_exposure,
    confirmed_loss,
    prevented_loss,
    recovered
):
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


def money(value):
    return f"${value:,.2f}"


def print_results(result):
    print("\nCASE CALCULATOR")
    print("=" * 45)

    print(f"Gross Exposure:       {money(result.gross_exposure)}")
    print(f"Confirmed Loss:       {money(result.confirmed_loss)}")
    print(f"Prevented Loss:       {money(result.prevented_loss)}")
    print(f"Recovered:            {money(result.recovered)}")

    print("\nCALCULATED RESULTS")
    print("-" * 45)

    print(f"Total Loss Impact:    {money(result.total_loss_impact)}")
    print(f"Total Mitigation:     {money(result.total_mitigation)}")
    print(f"Remaining Exposure:   {money(result.remaining_exposure)}")

    print("\nPERCENTAGES")
    print("-" * 45)

    print(f"Recovery Rate:        {result.recovery_percentage:.2f}%")
    print(f"Prevention Rate:      {result.prevention_percentage:.2f}%")
    print(f"Mitigation Rate:      {result.mitigation_percentage:.2f}%")


if __name__ == "__main__":
    # Synthetic demonstration data
    case = calculate_case(
        gross_exposure=2100.00,
        confirmed_loss=400.00,
        prevented_loss=300.00,
        recovered=100.00,
    )

    print_results(case)
