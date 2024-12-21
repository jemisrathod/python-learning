# match-case statement (switch): An alternative to using many 'elif' statements
#               Execute some code if a value matches a 'case'
#               Benifits: cleaner and syntex is more readable
# Ex. 1
def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _: # _ is wild card 
            return "Invalid day"
print(day_of_week(4))