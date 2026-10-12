import random

correct = False
comp_num = 0


def define_random():
    s_low = input("Pick a low number: ")
    s_high = input("Pick a high number: ")

    i_low = int(s_low)
    i_high = int(s_high)

    return random.randrange(i_low, i_high)


def guess():
    s_num = input("I am thinking of a number, what number am I thinking of? ")
    return int(s_num)


def check_guess(i_guess):
    if i_guess == comp_num:
        print("YOU WIN!!!")
        return True
    elif i_guess > comp_num:
        print("Your number is too high")
    else:
        print("Your number is too low")

    return False


comp_num = define_random()
while not correct:
    correct = check_guess(guess())
