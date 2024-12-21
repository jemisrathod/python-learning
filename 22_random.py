#number = random.randint(1, 6)
#number = rando,.random() - this will give you s random float
#option = random.choice(option) - this will select random word from choise list.\
import random
num_low = 0
num_high = 100

rand = random.randint(num_low, num_high)

no_guess = 0
is_running = True
while is_running:
    guess = input("ENter your guess ")

    if guess.isdigit():
        guess = int(guess)
        no_guess += 1
        if guess < num_low or guess > num_high :
            print("Your guess is out of range")
        elif guess > rand:
            print("HIGH ")
        elif guess < rand:
            print("LOW ")
        else: 
            print(f"CORRECT, attempts {no_guess}")
            is_running = False
    else:
            print("Incorrect")
            


print(f"Weelll dun! U MADE {no_guess} attempts  ")