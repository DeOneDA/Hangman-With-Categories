import random

words = ["TEST", "EXAM", "TASK", "QUIZ", "SHEEP", "DOG", "LION", "CAT", "LIZARD", "TIGER"]

def hangman_lv1():
    lives = 6
    max_wrong_attempts = 5
    correct = random.choice(words)

    print("Welcome to Hangman Level 1 Game.")
    print(f"The word you need to guess is {len(correct)} letters long, and you have {lives} lives.")
    print("Please guess a single letter at a time.")
    display = ["_" for _ in range(len(correct))]
    print(f"{display}")
    print()

    while True:
        if max_wrong_attempts < 1:
            print("Nice one, your playing has put you in trouble. Since you're not ready to play then goodnight.")
            return
        
        if lives < 1:
            print(f"""*********************** YOU'RE OUT OF LIVES, IT WAS {correct.upper()} ***********************""")
            print(f"""*********************** YOU LOSE ***********************""")
            print()
            break

        print(f"****************************{lives}/6 LIVES LEFT****************************")
        print()

        user = input("> ")

        if not user.isalpha():
            print("Error: Oga! Put in a letter joor.")
            max_wrong_attempts -= 1
            print()
            continue

        if len(user) != 1:
            print("Error: You can only put in a single character at a time.")
            max_wrong_attempts -= 1
            print()
            continue

        if user.upper() in correct:
            if user.lower() in display:
                print("You've guessed this already.")
                print()
                continue

            print("That was a correct guess, very nice.")

            for i in range(len(display)):
                if correct[i] == user.upper():
                    display[i] = correct[i].lower()

            print(f"{display}")

            if "_" not in display:
                print("**************************** CONGRATULATIONS, YOU WIN ****************************")
                print()
                break

            print()
            continue

        if user.upper() not in correct:
            print("Wrong guess.")
            lives -= 1
            print(f"You have {lives} lives left.")
            print()
            continue
        
    print("Thank you for playing")
    print()


hangman_lv1()