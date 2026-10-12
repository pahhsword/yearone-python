COST_EACH = 0.50
VAT_PERCENT = 0.2
PAD_STR = "%0.2f"
PADDED_COST_EACH = PAD_STR % COST_EACH

# Yummy Gummies Purchasing - Ask user for amount
str_amount = input("How many Yummy Gummies would you like to purchase? ")
try:
    # Ensures the amount is a valid integer
    int_amount = int(str_amount)

    # Calculate the price using the constants of how much each Gummy bear costs and how much % VAT is
    float_price = int_amount * COST_EACH
    float_vat = float_price * VAT_PERCENT
    float_total = float_price + float_vat

    # Pad the numbers to ensure atleast 2 d.p.
    padded_vat = PAD_STR % float_vat
    padded_price = PAD_STR % float_price
    padded_total = PAD_STR % float_total

    # Output the information for the user to see
    print(f"\nPRICE: £{padded_price} ({str_amount}x £{PADDED_COST_EACH})")
    print(f"VAT:   £{padded_vat} ({VAT_PERCENT * 100}%)") 
    print(f"TOTAL: £{padded_total}")
except:
    print("You must enter a number amount")