#List comprehension = A consise way to create lists in python
#                   compact and easier to read than traditional loops
#                   [expression for value in iterable if condition]
#ex 1
# doubles = [x*2 for x in range(1,11)]
# triples = [y*3 for y in range(1,11)]
# squares = [z*z for z in range(1,11)]
# print(doubles) # [2, 4, 6, 8, 10,...
# print(triples) # [3, 6, 9, 12, 15,...
# print(squares) # [1, 4, 9, 16, 25,...

# ex 2
#fruits = ["apple", "banana", "coconut"]
#fruit_char = [fruit[0] for fruit in fruits]
#print(fruit_char)

#ex 3 
# numbers = [1,-2,3,-4,5,-6, 8, -7]
# positive = [num for num in numbers if num >= 0]
# negative = [num for num in numbers if num <= 0]
# even = [num for num in numbers if num%2 == 0]
# odd = [num for num in numbers if num%2 != 0]
# print(positive) # [1, 3, 5]
# print(negative) # [-2, -4, -6]
# print(even)
# print(odd)

#ex 4
grades = [85, 42, 78, 54, 32, 87]
passing_grades = [grade for grade in grades if grade>= 50]
print(passing_grades)