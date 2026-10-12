str_num = input("Enter the number: ")

try:
    float_num = float(str_num)
    if float_num == 0:
        print("This is zero")
    elif float_num > 0:
        print("This is positive")
    else:
        print("This is negative")
except:
    print("Enter a valid number")
