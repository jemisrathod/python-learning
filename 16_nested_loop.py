rows = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol you like to use: ")

for x in range(column):
    for y in range(rows):
        print(symbol, end = "")# Here end="" is used to print output in same line, you can add anything btw the ""s
    print()#This function will create a new line