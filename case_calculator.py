from case_calculator import calculate_case

result = calculate_case(
    gross_exposure=12500,
    confirmed_loss=4000,
    prevented_loss=7000,
    recovered_amount=1500,
)

print(result.as_dict())
