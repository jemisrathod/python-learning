menu = { "Pizza": 12,
        "Sub": 23,
        "Pop": 34 }

cart = {}
total = 0

print("--------------------------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")

while True:
    food = input("Enter the food u wanna buy. press q to quitt: ")
    food = food.capitalize()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        if food in cart:
            cart[food] += menu[food]
        else:
            cart[food] = menu[food]
    else:
        print(f"Sorry, {food} is not available in our menu.")
for food, price in cart.items():
    print(f"{food:10}: ${price:.2f}")
    total += price
print(f"Your total is ${total}")