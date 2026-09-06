from collections import defaultdict


def calculate_case(gross_exposure, confirmed_loss, prevented_loss, recovered):
    """Calculate basic case financial metrics."""

    values = {
        "gross_exposure": gross_exposure,
        "confirmed_loss": confirmed_loss,
        "prevented_loss": prevented_loss,
        "recovered": recovered,
    }

    for name, value in values.items():
        if value < 0:
            raise ValueError(f"{name} cannot be negative.")

    if confirmed_loss + prevented_loss > gross_exposure:
        raise ValueError(
            "Confirmed loss + prevented loss cannot exceed gross exposure."
        )

    net_loss = max(confirmed_loss - recovered, 0)
    total_mitigation = prevented_loss + recovered

    loss_rate = (
        confirmed_loss / gross_exposure * 100
        if gross_exposure
        else 0
    )

    prevention_rate = (
        prevented_loss / gross_exposure * 100
        if gross_exposure
        else 0
    )

    recovery_rate = (
        recovered / confirmed_loss * 100
        if confirmed_loss
        else 0
    )

    return {
        "gross_exposure": gross_exposure,
        "confirmed_loss": confirmed_loss,
        "prevented_loss": prevented_loss,
        "recovered": recovered,
        "net_loss": net_loss,
        "total_mitigation": total_mitigation,
        "loss_rate": loss_rate,
        "prevention_rate": prevention_rate,
        "recovery_rate": recovery_rate,
    }


def normalize(value):
    """Normalize a value for basic comparison."""

    return " ".join(value.strip().split()).casefold()


def parse_events(event_text):
    """
    Parse events in the format:

    Event ID | Field | Value
    """

    records = []

    for line_number, line in enumerate(event_text.splitlines(), start=1):

        line = line.strip()

        if not line:
            continue

        parts = [part.strip() for part in line.split("|", 2)]

        if len(parts) != 3:
            raise ValueError(
                f"Line {line_number} must use: "
                "Event ID | Field | Value"
            )

        event_id, field, value = parts

        if not event_id or not field or not value:
            raise ValueError(
                f"Line {line_number} contains an empty field."
            )

        records.append({
            "event_id": event_id,
            "field": field,
            "value": value,
            "normalized_value": normalize(value),
        })

    return records


def cross_reference(event_text):
    """
    Find values that appear more than once
    across case events.
    """

    records = parse_events(event_text)

    grouped = defaultdict(list)

    for record in records:
        grouped[record["normalized_value"]].append(record)

    repeated = []

    for matches in grouped.values():

        if len(matches) < 2:
            continue

        events = []
        fields = []

        for match in matches:

            if match["event_id"] not in events:
                events.append(match["event_id"])

            if match["field"] not in fields:
                fields.append(match["field"])

        repeated.append({
            "value": matches[0]["value"],
            "fields": fields,
            "occurrences": len(matches),
            "events": events,
        })

    repeated.sort(
        key=lambda item: (
            -item["occurrences"],
            item["value"].lower()
        )
    )

    return repeated


def build_matrix(event_text):
    """
    Build an identifier-to-event matrix.
    """

    records = parse_events(event_text)

    event_ids = []

    for record in records:

        if record["event_id"] not in event_ids:
            event_ids.append(record["event_id"])

    grouped = defaultdict(list)

    for record in records:
        grouped[record["normalized_value"]].append(record)

    matrix = []

    for matches in grouped.values():

        if len(matches) < 2:
            continue

        matching_events = {
            match["event_id"]
            for match in matches
        }

        matrix.append({
            "value": matches[0]["value"],
            "events": {
                event_id: event_id in matching_events
                for event_id in event_ids
            },
        })

    matrix.sort(
        key=lambda item: item["value"].lower()
    )

    return event_ids, matrix


if __name__ == "__main__":

    print("=" * 60)
    print("CASE CALCULATOR")
    print("=" * 60)

    case = calculate_case(
        gross_exposure=12500,
        confirmed_loss=4800,
        prevented_loss=3200,
        recovered=1500,
    )

    for key, value in case.items():

        label = key.replace("_", " ").title()

        if key.endswith("_rate"):
            print(f"{label}: {value:.2f}%")
        else:
            print(f"{label}: ${value:,.2f}")

    print()
    print("=" * 60)
    print("EVIDENCE CROSS-REFERENCE")
    print("=" * 60)

    sample_events = """
Event 1 | Device | DEVICE-A
Event 1 | IP | IP-EXAMPLE-01
Event 2 | Email | investigator@example.invalid
Event 2 | Device | DEVICE-B
Event 3 | Device | DEVICE-A
Event 3 | Email | investigator@example.invalid
Event 4 | IP | IP-EXAMPLE-02
Event 5 | Device | DEVICE-C
"""

    repeated = cross_reference(sample_events)

    if not repeated:
        print("No repeated values found.")

    else:

        for item in repeated:

            print()
            print(f"Identifier: {item['value']}")
            print(f"Type(s): {', '.join(item['fields'])}")
            print(f"Occurrences: {item['occurrences']}")
            print(f"Events: {', '.join(item['events'])}")

    print()
    print("=" * 60)
    print("EVIDENCE MATRIX")
    print("=" * 60)

    event_ids, matrix = build_matrix(sample_events)

    print("Identifier".ljust(35), end="")

    for event_id in event_ids:
        print(event_id.ljust(15), end="")

    print()

    print("-" * (35 + len(event_ids) * 15))

    for row in matrix:

        print(row["value"].ljust(35), end="")

        for event_id in event_ids:

            marker = (
                "✓"
                if row["events"][event_id]
                else ""
            )

            print(marker.ljust(15), end="")

        print()
