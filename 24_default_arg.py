# default arguments = A default value for certain parameters
#                   default is used when that argument is ommited
#                   make your functions more flexible, reduce # of args.
#                   1. Positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(1, 123, 456, 6789)

print(phone_num)