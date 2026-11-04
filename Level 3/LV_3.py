import random
import json

def hangman_lv3():
    print("Welcome to Hangman Level 3 Game.")
    print("Please pick a number to play from")
    print("1. Animals")
    print("2. Foods")
    print("3. Countries")

    while True:
        cat = input("> ")
        try:
            cat = int(cat)
        except:
            print("Enter an integer.")
            print()
            continue
        if cat < 1 or cat > 3:
            print("Enter a proper integer between 1 and 3.")
            print()
            continue
        print()
        break

    print("Please specify the difficulty level number you would like to play.")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        level = input("> ")
        try:
            level = int(level)
        except:
            print("Enter an integer.")
            print()
            continue
        if level < 1 or level > 3:
            print("Enter a proper integer between 1 and 3.")
            print()
            continue
        print()
        break

    choices = []

    if cat == 1:
        print("Category: Animals")
        try:
            with open("Animals.txt", "r") as file:
                if not file:
                    print("The Animals.txt file is empty, please fill it appropriately")
                    return hangman_lv3()
                
                for line in file:
                    line = line.strip()
                
                    if not line:
                        continue

                    if ":" in line:
                        parts = line.split(":")
                    elif "-" in line:
                        parts = line.split("-")
                    else:
                        continue

                    if parts[0].strip().lower() == "easy" and level == 1:
                        choices.extend(parts[1].strip().lower().split(", "))
                    elif parts[0].strip().lower() == "medium" and level == 2:
                        choices.extend(parts[1].strip().lower().split(", "))
                    elif parts[0].strip().lower() == "Hard" and level == 3:
                        choices.extend(parts[1].strip().lower().split(", "))
        except:
            print("Sorry there's no 'Animals.txt' file in the directory, Please create a text file and fill it with the proper syntax")
    
    if cat == 2:
        print("Category: Foods")
        try:
            with open("Foods.txt", "r") as file:
                if not file:
                    print("The Foods.txt file is empty, please fill it appropriately")
                    return hangman_lv3()
                
                for line in file:
                    line = line.strip()
                
                    if not line:
                        continue

                    if ":" in line:
                        parts = line.split(":")
                    elif "-" in line:
                        parts = line.split("-")
                    else:
                        continue

                    if parts[0].strip().lower() == "easy" and level == 1:
                        choices.extend(parts[1].strip().lower().split(", "))
                    elif parts[0].strip().lower() == "medium" and level == 2:
                        choices.extend(parts[1].strip().lower().split(", "))
                    elif parts[0].strip().lower() == "Hard" and level == 3:
                        choices.extend(parts[1].strip().lower().split(", "))
        except:
            print("Sorry there's no 'Foods.txt' file in the directory, Please create a text file and fill it with the proper syntax")

    if cat == 3:
        print("Category: Country")
        try:
            with open("Countries.txt", "r") as file:
                if not file:
                    print("The Countries.txt file is empty, please fill it appropriately")
                    return hangman_lv3()
                
                for line in file:
                    line = line.strip()
                
                    if not line:
                        continue

                    if ":" in line:
                        parts = line.split(":")
                    elif "-" in line:
                        parts = line.split("-")
                    else:
                        continue

                    if parts[0].strip().lower() == "easy" and level == 1:
                        choices.extend(parts[1].strip().lower().split(", "))
                    elif parts[0].strip().lower() == "medium" and level == 2:
                        choices.extend(parts[1].strip().lower().split(", "))
                    elif parts[0].strip().lower() == "hard" and level == 3:
                        choices.extend(parts[1].strip().lower().split(", "))
        except:
            print("Sorry there's no 'Countries.txt' file in the directory, Please create a text file and fill it with the proper syntax")

    correct = random.choice(choices)
    if level == 1:
        lives = 3
    elif level == 2:
        lives = 5
    elif level == 3:
        lives = 7

    with open("Stages.json", "r") as file:
        hangman_art = json.load(file)

    display_word = ["_" for _ in range(len(correct))]
    display = " ".join(display_word)

    print(hangman_art[str(level)]["0"])
    print(f"Word: {display}")
    print("Please type one letter at a time.")
    print("If you'd like a hint, enter 'hint'")

    guessed = []
    guessed_word = ""
    wrong = []
    wrong_word = ""
    hint_used = False
    total_points = 0

    while True:
        if "_" not in display_word:
            print("**************************** CONGRATULATIONS, YOU WIN ****************************")
            break

        if lives < 1:
            print(f"""*********** YOU'RE OUT OF LIVES, IT WAS {correct.upper()} ***********""")
            print(f"""*********************** YOU LOSE ***********************""")
            break

        user = input("> ")

        if not user.isalpha():
            print()
            print("Please put in only letters")
            continue

        if user.lower() == "hint" and not hint_used:
            for i in range(len(display_word)):
                if display_word[i] == "_":
                    display_word[i] = correct[i]
                    wrong.append(correct[i])
                    wrong_word = ", ".join(wrong)
                    break
            display = " ".join(display_word)
            print("You used a hint, a life will be taken.")
            lives -= 1
            print(hangman_art[str(level)][str(len(wrong))])
            print(f"Word: {display}")
            print(f"Wrong guesses: {wrong_word} (Lives left: {lives})")
            print(f"Guessed so far: {guessed_word}")
            hint_used = True
            continue
        elif user.lower() == "hint" and hint_used:
            print("You have already used your hint for this round.")
            continue


        if len(user) != 1:
            print()
            print("You can only put in a single character.")
            continue

        if user.lower() in correct:
            print()
            if user.lower() in guessed:
                print("You've guessed this already.")
                continue

            print("That was a correct guess, very nice.")

            if level == 1:
                total_points += 2
            elif level == 2:
                total_points +=  5
            elif level == 3:
                total_points += 10

            for i in range(len(correct)):
                if correct[i] == user.lower():
                    display_word[i] = correct[i].upper()
            
            display = " ".join(display_word)

            if user.lower() not in guessed:
                guessed.append(user.lower())
                guessed_word = ", ".join(guessed)

            print(hangman_art[str(level)][str(len(wrong))])
            print(f"Word: {display}")
            print(f"Wrong guesses: {wrong_word} (Lives left: {lives})")
            print(f"Guessed so far: {guessed_word}")
        else:
            print()
            if user.lower() not in wrong:
                print("Ouch that's a wrong guess, you loose a life.")
                lives -= 1
                wrong.append(user.lower())
                wrong_word = ", ".join(wrong)
            elif user.lower() in wrong:
                print("You've guessed this before.")
                continue
                
            print(hangman_art[str(level)][str(len(wrong))])
            print(f"Word: {display}")
            print(f"Wrong guesses: {wrong_word} (Lives left: {lives})")
            print(f"Guessed so far: {guessed_word}")

        print()
    print(f"Your Total Points = {total_points} points.")
    print("Thank you for playing.")


hangman_lv3()