weight = float(input("Entr your weight: "))
unit = input("Enter the UNIT KGs or Lbs. (K or L) ")

if unit == "K":
    weight = weight * 2.20462
    unit = "Lbs"
    print(f"Your weight is {round(weight, 2)} {unit} .")
elif unit == "L":
    weight = weight * 0.453592
    unit = "Kgs"
    print(f"Your weight is {round(weight, 2)} {unit} .")
else:
    print(f"{unit} is invalid. ")