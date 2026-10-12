import random

EXIT_CODE = "exit"
BOUND_LOWER = 1
BOUND_UPPER = 10

correct_count = 0
total_guesses = 0
str_number = ""

# Function to generate random number
def generate_number():
    return random.randint(BOUND_LOWER, BOUND_UPPER)

random_number = generate_number()

# Main Loop
while not (str_number == EXIT_CODE):
    str_number = input(f"Please enter in a number between {BOUND_LOWER} and {BOUND_UPPER}: ")
    try:
        # Sanatize input and increment if success
        int_number = int(str_number)
        total_guesses += 1

        # Handle logic
        if int_number == random_number:
            correct_count += 1
            print("Correct! A new number has been picked.\n")
            random_number = generate_number()
        elif int_number < random_number:
            print("Your number was lower!")
        else:
            print("Your number was higher!")
    except:
        if str_number != EXIT_CODE:
            print("Please enter in a valid number.")

# Output Results

float_percent = total_guesses > 0 and correct_count/total_guesses * 100 or 0
print(f"\nCorrect: {correct_count}/{total_guesses} ({float_percent:.02f}%)")