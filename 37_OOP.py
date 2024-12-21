# Object oriented programming
# Object = A "bundle" of related attributes (variables) and methods (functions)
# Ex. phone , cup , book
# Class = A template for creating objects
from classes import Car

car1 = Car("Audi A4", 2024, "Black", False)
car2 = Car("Mercedes C300", 2024, "White", True)
car3 = Car("Audi RS5", 2025, "Black", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car2.stop()