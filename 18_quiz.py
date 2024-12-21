print("Wazzzup pplzz!!! Welcome to the game ,,.")

questions = ("What is your name? ",
             "What is your race? ",
             "What do you think of your self? ",
             "Are you racist ? ")
options = (
            ("A. Alex", "B. Jaacob", "C. Tanner", "D. Jason"),
            ("A. White", "B. Black","C. Yellow","D. Brown"),
            ("A. One of one", "B. Superior","C. Know it all", "D. Dumb fuck"),
            ("A. maybe", "B. Yes", "C. NO", "D. Definetly")

)

question_no = 0
answers = ("D", "A", "D", "D")
guesses = []
score = 0
for question in questions:
    print("------------------------------")
    print(question)
    print()
    for option in options[question_no]:
        print(option)

        
    guess = input("Enter Your answer: ABCD: ").upper()
    guesses.append(guess)
    
    if guess == answers[question_no]:
        score += 1
        print("Correct")
    else:
        print(f"Incorrect mfrrr!! correct answer is {answers[question_no]}")
    print()
    question_no += 1

score = (score/question_no)*100
print(f"Your score is {score}")
