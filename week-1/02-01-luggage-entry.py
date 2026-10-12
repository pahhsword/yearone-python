MAX_LUGGAGE = 100
LUGGAGE_INCREMENT = 5
LUGGAGE_CHARGE = 1

str_kg = input("How much kg does your luggage weigh? ")

try:
    # Sanatize Input
    float_kg = float(str_kg)
    int_price = 0

    # If KG is over the max free luggage amount, calculate price
    if float_kg > MAX_LUGGAGE:
        # Define how much kg the bag is over the max
        float_over = float_kg - MAX_LUGGAGE

        # Use the amount over max divided by the increment to calculate the fee
        price = LUGGAGE_CHARGE * (float_over // LUGGAGE_INCREMENT)
    else:
        price = 0

    # Output Price
    print(f"Price: £{price:.02f} (£{LUGGAGE_CHARGE:.02f} for every {LUGGAGE_INCREMENT}kg over {MAX_LUGGAGE}kg)")
except:
    print("Please input a number")