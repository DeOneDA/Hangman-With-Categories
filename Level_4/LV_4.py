import json
import getpass

def hangman_lv4():
    try:
        with open("score.json", "r") as file:
            scores = json.load(file)
    except:
        scores = {}

    try:
        with open("Art.json", "r") as file:
            hangman_art = json.load(file)
    except:
        print("Please put the Art.json file for the ASCII Art of the hangman in the same directory as this file.")
        print("Confirm if you're currently at the directory of where this file is before running it.")
        return

    print("Welcome to Hangman Level 4 Game.")
    print("This version of the game works with two players.")
    print("""The format is that Player 1 inputs the word to be
guessed and can add a hint of their choice while Player 2 guesses the word""")
    print("Player 1, kindly input your name.")

    while True:
        player1 = input("> ")
        if not player1.strip():
            print("Please input a proper name.")
            continue

        break

    secret_word = getpass.getpass("Player 1, enter your secret word: ")
    print()
    print("Would you like to add a categorical hint for Player 2?")
    print("Y/N")

    while True:
        holder = input("> ").lower().strip()
        if holder == "n" or holder == "y" or holder == "yes" or holder == "no":
            break

        print("Please either type 'Yes', 'No', 'Y' or 'N'")
        continue

    if holder == "yes" or holder == "y":
        hint = input("What hint would you like them to know? ")
        print("Hint has been stored.")

    print("Player 1's data has been stored.")
    print("Player 2, kindly input your name:")

    while True:
        player2 = input("> ")
        if not player2.strip():
            print("Please input a proper name.")
            continue

        break

    lives = 7
    display_word = [" " if secret_word[i] == " " else "-" if secret_word[i] == "-" else "_" for i in range(len(secret_word))]
    display = " ".join(display_word)
    guessed = []
    guessed_word = ""
    wrong = []
    wrong_word = ""
    hint_used = False
    total_points = len(secret_word) * 5
    game_over = False

    print(f"*********************** You have {lives} lives, Have Fun. ***********************")

    while True:
        if game_over:
            break

        print(hangman_art[str(len(wrong))])
        
        if lives < 1:
            print(f"""*********** YOU'RE OUT OF LIVES, IT WAS {secret_word.upper()} ***********""")
            print(f"""*********************** YOU LOSE ***********************""")
            game_over = True
            break

        print("Please pick how you'd like to guess?")
        print("W - Word(s), L - Letter")

        guess_category = input("> ").lower()

        valid_inputs = ["l", "w", "word", "letter", "words"]
        
        if guess_category not in valid_inputs:
            print("I thought you had sense but I guess I was wrong. Pardon me for assuming so.")
            continue

        if guess_category == "l" or guess_category == "letter":
            while True:
                if not hint_used:
                    print("If you would like a hint, input 'H'")

                guess = input("> ")
                
                if not guess.isalpha():
                    print("At this point you might actually have a reading problem becauser why? Just why?")
                    continue

                if len(guess) > 1 and guess not in valid_inputs:
                    print("But you explicitly said that you want to guess letter by letter earlier, did you drink something ni?")
                    continue

                if guess.lower() in guessed:
                    print("You've guessed this already.")
                    continue

                break

            if holder == "yes" or holder == "y":
                if guess.lower().strip() == "h" and not hint_used:
                    print(hint)
                    hint_used = True
                elif hint_used:
                    print("Oga you've used your hint already joor.")
                    continue
            elif (holder == "no" or holder == "n") and guess.strip().lower() == "h":
                print("Sorry Player 1 didn't leave a hint for you.")
                continue


            if guess.lower() in secret_word.lower():
                print("That was a correct guess, very nice.")
                for i in range(len(secret_word)):
                    if secret_word[i].lower() == guess.lower():
                        display_word[i] = secret_word[i]

                display = " ".join(display_word)
                guessed.append(guess.lower())
                guessed_word = ", ".join(guessed)
                
                if "_" not in display_word:
                    print("**************************** CONGRATULATIONS, YOU WIN ****************************")
                    game_over = True
                    break

                print(hangman_art[str(len(wrong))])
                print(f"Word: {display}")
                print(f"Wrong guesses: {wrong_word} (Lives left: {lives})")
                print(f"Guessed so far: {guessed_word}")
            else:
                if guess.lower() not in wrong:
                    print("Ouch that's a wrong guess, you loose a life.")
                    lives -= 1

                    if total_points > 0:
                        total_points -= 5

                    wrong.append(guess.lower())
                    wrong_word = ", ".join(wrong)
                else:
                    print("You've guessed this before.")
                    continue
                
                print(hangman_art[str(len(wrong))])
                print(f"Word: {display}")
                print(f"Wrong guesses: {wrong_word} (Lives left: {lives})")
                print(f"Guessed so far: {guessed_word}")
        elif guess_category == "w" or guess_category == "word" or guess_category == "words":
            while True:
                if not hint_used:
                    print("If you would like a hint, input 'H'")
                
                w_guess = input("> ")
                if len(w_guess) < 2:
                    print("Wow, so you're telling me that what you wrote is a word abi? Are you sure you went to school?.")
                    continue
                if w_guess.lower() in guessed:
                    print("You've guessed this already.")
                    continue

                break

            if holder == "yes" or holder == "y":
                if w_guess.lower().strip() == "h" and not hint_used:
                    print(hint)
                    hint_used = True
                elif hint_used:
                    print("Oga you've used your hint already joor.")
                    continue
            elif (holder == "no" or holder == "n") and w_guess.strip().lower() == "h":
                print("Sorry Player 1 didn't leave a hint for you.")
                continue

            if w_guess.lower() == secret_word.lower():
                print("**************************** WOW! You actually got it. Impressive. ****************************")
                game_over = True
                break
            else:
                if w_guess.lower() not in wrong:
                    print("Wrong, you will receive a heavy penalty.")
                    if total_points > 10:
                        total_points -= 10
                    elif total_points > 5:
                        total_points -= 5
                    elif total_points > 0:
                        total_points -= 1
                    
                    if lives > 1:
                        lives -= 2
                    else:
                        lives -= 1

                    if len(wrong) < 6:
                        wrong.extend([w_guess.lower(), "penalty"])
                    else:
                        wrong.append(w_guess.lower())
                        
                    wrong_word = ", ".join(wrong)

                    print(hangman_art[str(len(wrong))])
                    print(f"Word: {display}")
                    print(f"Wrong guesses: {wrong_word} (Lives left: {lives})")
                    print(f"Guessed so far: {guessed_word}")
                else:
                    print("You've guessed this before.")
                    continue

    if player1 not in scores.keys():
        scores[player1] = [[player2, total_points]]
    else:
        scores[player1].append([player2, total_points])
    
    print()

    try:
        with open("score.json", "w") as file:
            json.dump(scores, file, indent=4)
        print("Score successfully saved to score.json!")
    except:
        print("Error saving score to score.json.")

    