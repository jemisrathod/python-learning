p = 0
r = 0
t = 0

while p <= 0:
    p = float(input("Enter principle ammount : "))
    if p <= 0:
        print("can not be less than or equal to zero: ")
while r <= 0:
    r = float(input("Enter rate ammount : "))
    if r <= 0:
        print("can not be less than or equal to zero: ")
while t <= 0:
    t = float(input("Enter time ammount in years: "))
    if t <= 0:
        print("can not be less than or equal to zero: ")

total = p * pow((1 + r/100), t)
print(f"Your invested amount is {p} with {r} percent interest for {t} years")
print(f"Your balance after {t} years is {total:.2f}")