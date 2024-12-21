# *args = allows you to pass multiplle non-key arguments
# **kwargs = allows you to pass  multiple keyword-arguments
#           * unpacking operator
#           1. Positional, 2. DEFAULT, 3. keyword, 4. arbitrary

#ex 1 for args
#def add(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total
#print(add(1,2,3,4))

#ex 2 for *args

#def display_name(*names):
#    for arg in names:
#        print(arg, end=" ")
#display_name("Spongebob", "harold", "squarepants"), 

# Ex 3 for **kwargs
#def print_address(**kwargs):
#    #print(type(kwargs))
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")
#
#print_address(street="123 main st", city="anytown", state="CA", zip_code="S4W 0B9")

#Ex 4 for **kwargs and *args

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    #for value in kwargs.values():
    #    print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Swuarepants", "III",
               street="123 main st", 
               city="anytown", 
               state="CA", 
               zip_code="S4W 0B9")
