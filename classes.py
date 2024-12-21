class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the car: {self.model} ")
    
    def stop(self):
        print(f"You stop the car: {self.model}")


class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("spongebob", 30)
student2 = Student("Nob", 33)
student3 = Student("Squid", 39)
student4 = Student("Crab", 79)


print(f"My graduating class of {Student.class_year} has {Student.num_students} people")