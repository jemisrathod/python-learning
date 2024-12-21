#This is a sample menu for a restaurent
#it is made using dictionary
# dictionary = {"Key":value}
#dictionary_name.get() - print the value of key
#dictionary_name.update({"pizza" : 15.50}) - update can be used to update current value or add a new one
#dictionary_name.pop("Pizza") - will remove that key
#dictionary_name.popitem() - will remove recent item in dictionary
#dictionary_name.clear() - clear the dictionary
#dictionary_name.key() - return all the keys within dictionary
#dictionary_name.value() - return all the values of a key
#dictionary_name.iems() - This will return a 2D list of all items like tupeles. Ex., [(),(),()]
menu = {"Pizza": 12.50,
        "Sub": 15,
        "Chips": 2.29,
        "Pop": 3.29,
        "Candy": 5.59,
        "Burger": 10.99,
        "Pop-corn": 16.99}

cart = {}

total = 0
print("+-+-+-+-+-+-+-MENU-+-+-+-+-+-+-+")
for key, value in menu.items():
    
    print(f"{key:10}: ${value:.2f}")

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

while True:
    food = input("Enter the item you would like to buy. (Press Q to Quit)").lower()
    food = food.capitalize()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        if food in cart:
            cart[food] += menu[food]
        else:            
            cart[food] = menu[food]

print("Your cart : ")
for food, price in cart.items():
    total += price
    print(f"{food:10}: ${price:.2f}")


print(f"Your total: ${total}")
