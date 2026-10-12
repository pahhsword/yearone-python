COST_EACH = 0.50
VAT_PERCENT = 0.2

# Yummy Gummies Purchasing - Ask user for amount
str_amount = input("How many Yummy Gummies would you like to purchase? ")
try:
    # Ensures the amount is a valid integer
    int_amount = int(str_amount)

    # Calculate the price using the constants of how much each Gummy bear costs and how much % VAT is
    float_price = int_amount * COST_EACH
    float_vat = float_price * VAT_PERCENT
    float_total = float_price + float_vat

    # Output the information for the user to see
    print(f"\nPRICE: £{float_price:.2f} ({str_amount}x £{COST_EACH:.2f})")
    print(f"VAT:   £{float_vat:.2f} ({VAT_PERCENT * 100}%)") 
    print(f"TOTAL: £{float_total:.2f}")
except:
    print("You must enter a number amount")