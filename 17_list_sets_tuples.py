# collection = single "Variable" used to store multiple value
# List = [] ordered and changable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No Duplicates
# Tuple = () ordered and unchangeble. Duplicated OK. Faster

fruits = []
price = []
total = 0
print("Press A to add:")
print("Press R to remove: ")
print("press Q to quit: ")
print("print C to clear your list: ")
while True:
    inp = input("Enter the operation you would like to do: ")
    if inp == "A" or inp == "a":
        fruits.append(input("Enter the fruit you would like to add:"))
        price.append(int(input("Enter the price of the fruit:")))
    elif inp == "R" or inp == "r":
        fruits.remove(input("Enter the fruit you would like to remove:"))
        price.remove(input("Enter the price of the fruit:"))
    elif inp == "C" or inp == "c":
        fruits.clear()
        price.clear()
        print(fruits)
    elif inp == "Q" or inp == "q":
        break
    
print("$$$---Your Cart---$$$")
for i in fruits:
    print(f"{i} - ${price[fruits.index(i)]}")
for y in price:
    total += y
    
print(f"Your cart total is: $ {total}")