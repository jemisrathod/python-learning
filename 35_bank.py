#python banking program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposite(balance):
    amount = float(input("Enter the amount to deposite: $"))

    if amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount
    pass

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))

    if amount > balance:
        print("Insufficient balance.")
        return 0
    elif amount < 0:
        print("Invalid amount. Please enter a positive number.")
        return 0
    else:
        return amount
    pass


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choise 1-4 : ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposite(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice. Please choose a valid option.")
    print("Thank YUH ! ")

if __name__ == '__main__':
    main()