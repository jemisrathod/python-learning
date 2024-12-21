#variable scope = where a variable is visible and accesible
# scope resolution = (LEGB) Local -> Enclose-> Global -> Built-in
# Local scope = inside a function
# Enclose scope = inside a nested function
# Global scope = outside a function
# Built-in scope = python built-in functions and variables

def func1():
    a = 1
    print(a)
    
def func2():
    b = 10
    print(b)

func1()
func2()