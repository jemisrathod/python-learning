#slot machine for beginner
import random
def spin_row():
    symbols = ['+','-','=','/','|']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):   
    print("______") 
    print(" ".join(row))
    print("______")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '+':
            return bet * 2
        elif row[0] == '-':
            return bet * 4
        elif row[0] == '=':
            return bet * 8
        elif row[0] == '/':
            return bet * 16
        elif row[0] == '|':
            return bet * 32
    return 0
        
    
    
def main():
    
    balance = 100

    print("********************")
    print("Welcome to the Slot ")
    print("Symbols: + - = / |")
    print("********************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Invalid bet amount. Please enter a number.")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient balance. Please place a bet within your balance.")
            continue

        if bet <=0:
            print("Bet must be > 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning..\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost your bet")

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print(f"You lost ${bet}")
        
        balance += payout

        play_again = input("DO you want to play again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print(f"Game over! Your final balance is ${balance}")

if __name__ == '__main__':
    main()