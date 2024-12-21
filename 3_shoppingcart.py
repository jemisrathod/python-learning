item = input("What item would you like to buy: ")
price = float(input("What is the price ? :"))
qty = int(input("how many would you like to buy ? :"))
total = price * qty
print(f"You have bought {qty} {item}")
print(f"the total price is ${ total} ")