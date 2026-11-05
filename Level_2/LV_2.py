import random

animals = ["elephant", 
           "penguin", 
           "kangaroo", 
           "dolphin", 
           "cheetah", 
           "octopus", 
           "hedgehog", 
           "giraffe", 
           "platypus", 
           "chimpanzee"]

foods = ["pizza", 
        "sushi", 
        "tacos", 
        "burger", 
        "lasagna", 
        "ramen", 
        "falafel", 
        "burrito", 
        "paella", 
        "gnocchi"]

countries = ["brazil", 
             "japan", 
             "kenya", 
             "canada", 
             "australia", 
             "thailand", 
             "egypt", 
             "france", 
             "argentina", 
             "iceland"]

hangman_pics = [
r"""
   +---+
       |
       |
       |
       |
       |
=========
""",
r"""
    +---+
    |   |
        |
        |
        |
        |
==========
""",
r"""
    +---+
    |   |
    O   |
        |
        |
        |
==========
""",
r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
==========
""",
r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
==========
""",
r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
==========
""",
r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
==========
""",
r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
==========
""",
]

def hangman_lv2():
    print("Welcome to Hangman Level 2 Game.")
    print("Please pick a number to play from")
    print("1. Animals")
    print("2. Foods")
    print("3. Countries")

    max_wrong_attempts = 5

    while True:
        if max_wrong_attempts < 1:
            print("Nice one, your playing has put you in trouble. Since you're not ready to play then goodnight.")
            return

        cat = input("> ")

        try:
            cat = int(cat)
        except:
            print("Error: Why you dey play with your future Oga! Enter an integer.")
            print()
            max_wrong_attempts -= 1
            continue

        if cat < 1 or cat > 3:
            print("Error: Oga, what's your problem. Enter a proper integer between 1 and 3.")
            print()
            continue
        
        print()
        break

    if cat == 1:
        correct = random.choice(animals)
        print(f"Categories: Animals")
    elif cat == 2:
        correct = random.choice(foods)
        print(f"Categories: Foods")
    elif cat == 3:
        correct = random.choice(countries)
        print(f"Categories: Countries")

    display_word = ["_" for _ in range(len(correct))]
    display = " ".join(display_word)

    print(hangman_pics[0])
    print(f"Word: {display}")
    print("Please type one letteer at a time.")
    

    guessed = []
    guessed_word = ""
    wrong = []
    wrong_word = ""
    lives = 7

    while True:
        if max_wrong_attempts < 1:
            print("Nice one, your playing has put you in trouble. Since you're not ready to play then goodnight.")
            return
        
        if "_" not in display_word:
            print("**************************** CONGRATULATIONS, YOU WIN ****************************")
            break

        if lives < 1:
            print(f"*********************** YOU'RE OUT OF LIVES, IT WAS {correct.upper()} ***********************")
            print(f"*********************** YOU LOSE ***********************")
            break

        print()
        print(f"****************************{lives}/7 LIVES LEFT****************************")

        user = input("> ")

        if not user.isalpha():
            print()
            print("Please put in only letters")
            max_wrong_attempts -= 1
            continue

        if len(user) != 1:
            print()
            print("You can only put in a single character.")
            max_wrong_attempts -= 1
            continue

        if user.lower() in correct:
            print()
            if user.lower() in guessed:
                print("You've guessed this already.")
                continue

            print("That was a correct guess, very nice.")

            for i in range(len(correct)):
                if correct[i] == user.lower():
                    display_word[i] = correct[i].upper()
            
            display = " ".join(display_word)

            if user.lower() not in guessed:
                guessed.append(user.lower())
                guessed_word = ", ".join(guessed)

            print(hangman_pics[0+len(wrong)])
            print(f"Word: {display}")
            print(f"Wrong guesses: {wrong_word} (Lives left: {lives})")
            print(f"Guessed so far: {guessed_word}")
            

        elif user.lower() not in correct:
            print()
            if user.lower() not in wrong:
                print("Ouch that's a wrong guess, you loose a life.")
                lives -= 1
                wrong.append(user.lower())
                wrong_word = ", ".join(wrong)
            elif user.lower() in wrong:
                print("You've guessed this before.")
                continue

            print(hangman_pics[0+len(wrong)])
            print(f"Word: {display}")
            print(f"Wrong guesses: {wrong_word} (Lives left: {lives})")
            print(f"Guessed so far: {guessed_word}")
        
        print()

    print("Thank you for playing.")

hangman_lv2()