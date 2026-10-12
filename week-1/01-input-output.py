full_name = input("Please enter your full name: ")
age = input("Please enter your age: ")


try:
    int(age)
    print(f"The name you entered was {full_name} and you are {age} years old")
except:
    print("Please enter a valid age")
