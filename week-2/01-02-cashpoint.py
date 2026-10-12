valid = True

file = open("workfile.txt", "r+")
i_balance = int(file.readline())

def exit_fn():
    valid = False

def mobile_top_up():
    print("1")

def cash_withdrawl():
    s_withdraw = input("How much would you like to withdraw >> ")
    i_withdraw = int(s_withdraw)

    global i_balance
    if i_withdraw > i_balance:
        print("You do not have enough money to withdraw")
    else:
        i_balance -= i_withdraw


def display_balance():
    global i_balance
    print(f"Balance: £{i_balance:.2f}")

def order_statement():
    print("4")

def change_pin():
    print("5 fn")

tbl = [
    ["0", "Exit", exit_fn],
    ["1", "Mobile phone top-up", mobile_top_up],
    ["2", "Cash withdrawl", cash_withdrawl],
    ["3", "Display the balance", display_balance],
    ["4", "Order statement", order_statement],
    ["5", "Change pin", change_pin]
]

while valid:
    s_main = ""
    for i in range(len(tbl)):
        s_main = f"{tbl[i][0]}. {tbl[i][1]}\n{s_main}"

    s_option = input(f"What would you like to do: \n{s_main} >> ")
    for i in range(len(tbl)):
        if s_option == tbl[i][0]:
            tbl[i][2]()
            print("---------------------------")

file.writelines([str(i_balance)])
file.close()