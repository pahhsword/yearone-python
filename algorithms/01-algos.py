# Linear Search

# Create a list of bad passwords:
lPoorPasswords = ["abc", "12345", "password", "admin", "letmein", "qwerty"]

# Get the desired input word
sDesiredWord = input("Pasword >> ")

# Linear Algo Flag:
# Used to check whether we have completed the algorithm
bLinearFound = False

# Linear Algorithm:
# Searches through the list one by one
for iCount in range(0, len(lPoorPasswords)):
    if sDesiredWord == lPoorPasswords[iCount]:
        bLinearFound = True
        print(f"{sDesiredWord} is at {iCount}")

# Expand the program with the following
# 1 - All inputted passwords, must be a min of 8 letters/numbers
# 2 - You must have a capital
# 3 - You must use numbers

iWordLen = len(sDesiredWord)
bMeetsMinimum = iWordLen >= 8
bHasCapital = sDesiredWord.lower() != sDesiredWord
bHasNumbers = False
for i in range(0, 9):
    if sDesiredWord.find(str(i)) != -1:
        print(f"has {i}")
        bHasNumbers = True

if not bMeetsMinimum or not bHasCapital or not bHasNumbers:
    print("------------------")
    print("Errors: ")
if not bHasNumbers:
    print(" >> ! Need numbers")
if not bHasCapital:
    print(" >> ! Need capital")
if not bMeetsMinimum:
    print(f" >> ! Need atleast 8 characters {iWordLen}/8")
