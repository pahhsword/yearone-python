def calc_amount_per_mile(s_fuel, f_capacity):
    amount_per = 0
    if s_fuel == "petrol" and f_capacity > 1.6:
        amount_per = 0.32
    elif s_fuel == "petrol" and f_capacity <= 1.6:
        amount_per = 0.25
    elif s_fuel == "diesel" and f_capacity > 1.5:
        amount_per = 0.36
    elif s_fuel == "diesel" and f_capacity <= 1.5:
        amount_per = 0.29

    return amount_per


print(calc_amount_per_mile("petrol", 1.6))
print(calc_amount_per_mile("petrol", 1.7))
print(calc_amount_per_mile("diesel", 1.5))
print(calc_amount_per_mile("diesel", 1.6))
