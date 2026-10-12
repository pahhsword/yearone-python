import csv

ATTEMPTS = 3

class Cashpoint:
    balance = 0
    pin = 0000
    attempts = ATTEMPTS

    def displayBalance(this):
        print(f"Balance: £{this.balance}")

    def cashWithdrawl(this):
        try:
            i_cash_amount = int(input("How much cash would you like to withdraw?: £"))
            if i_cash_amount <= 0:
                raise Exception("Balance amount must be above £0.00")
            
            if this.balance - i_cash_amount <= 0:
                raise Exception("You do not have enough money to withdraw")

            this.balance -= i_cash_amount
            this.save()

            print(f"Withdrawing £{i_cash_amount:.2f}\nNew Balance: £{this.balance:.2f}")
        except Exception as e:
            print(f"Exception: {e}")

    def changePin(this):
        try:
            i_pin = int(input("Confirm your current pin: "))
            if i_pin != this.pin:
                raise Exception("Pin does not match with the current pin")

            i_new_pin = int(input("Enter a new pin: "))
            i_new_pin_confirm = int(input("Confirm a new pin: "))
            if i_new_pin != i_new_pin_confirm:
                raise Exception("Pins do not match")

            this.pin = i_new_pin
            this.save()
        
        except Exception as e:
            print(f"Exception: {e}")

    def save(this):
        with open('cashpoint.csv', 'w', newline='') as csvfile:
            fieldnames = ['balance', 'pin']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'balance': str(this.balance), 'pin': str(this.pin)})

    def attemptLogin(this):
        while this.attempts > 0:
            try:
                i_attempted_pin = int(input("Enter your pin: "))
                if i_attempted_pin != this.pin:
                    this.attempts -= 1
                    print(f"Incorrect, you have {this.attempts} attempts left")
                    continue

                print("Correct, welcome.")
                break
            except Exception as e:
                print(f"Exception: {e}")

        if this.attempts == 0:
            print("Too many attempts.")
            exit(0)

    def exitCashpoint(this):
        this.save()
        exit()

    def __init__(this):
        with open('cashpoint.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                this.balance = int(row["balance"])
                this.pin = int(row["pin"])

cashpoint_var = Cashpoint()

cashpoint_var.attemptLogin()

l_options = [
    ["0", "Exit", cashpoint_var.exitCashpoint],
    ["2", "Cash withdrawl", cashpoint_var.cashWithdrawl],
    ["3", "Display the balance", cashpoint_var.displayBalance],
    ["5", "Change pin", cashpoint_var.changePin]
]

while True:
    s_main = ""
    for i in range(len(l_options)):
        s_main = f"{l_options[i][0]}. {l_options[i][1]}\n{s_main}"

    s_option = input(f"What would you like to do: \n{s_main} >> ")
    for i in range(len(l_options)):
        if s_option == l_options[i][0]:
            l_options[i][2]()
            print("---------------------------\n")