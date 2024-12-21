# Membership operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

#word = "APPLE"

#letter = input("Guess the letter in the secret word: ")
#ex for (1) in = using string
#
#if letter in word:
#    print(f"There is a {letter}")
#else:
#    print(f"There is no {letter}")

#ex 2 for (2) not in = using string
#
#if letter not in word:
#    print(f"There is no {letter}"
#else:
#    print(f"There is a {letter}")

#students = {"Spongebob","Patrick","Sandy"}
#student = input("Enter the name of a student: ")
#ex for (1) in = using set
#if student in students:
#    print(f"{student} is a student")
#else:
#    print(f"{student} is not a student")

#ex for (2) not in = using set
# if student not in students:
#     print(f"{student} is not a student")
# else:
#     print(f"{student} is a student")

# example using dictionary
# ex for (1) in = using dictionary

#grades = {"Sandy": "A",
#          "Squidward": "B",
#          "Spongebob": "C",
#          "Patrick": "D"}
#student = input("Enter the name of a student: ")
#if student in grades:
#    print(f"{student} has a grade of {grades[student]}")
#else:
#    print(f"{student} is not a student")

email = "Email@gmail.com"

if "@" in email and "." in email:
    print("This is a valid email")
else:
    print("This is not a valid email")