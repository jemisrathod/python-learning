number = float(input("Enter your number btw 0 - 15: "))

while number < 0 or number > 15:
    print("Your number is not valid ")
    number = float(input("Try again 0-15 "))
print(f"Your number is: {number}")