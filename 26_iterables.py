# Iterables = An object/collection that can return its elements one at a time,
#            allowing it to be iterated over in a loop

#Ex with tuple
#number = (1,2,3,4,5)
#
#for num in reversed(number):
#    print(num, end="_")

#ex with sets - sets can not be reversed
#fruits = {"apple", "orange", "bsnsbs"}
#for fruit in fruits:
#    print(fruit, end=" ")

#ex with string 
#name = "Jemis Rathod"
#for x in name:
#    print(x, end=" ")

#example with dictionary
my_dict = {"A": 1, "B": 2, "C": 3}

for key, value in my_dict.items():
    print(key, value)