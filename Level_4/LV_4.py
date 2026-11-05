import json
import getpass
import random

def load_game_data():
    "Loads high scores and player stats from score.json."
    try:
        with open("score.json", "r") as file:
            data = json.load(file)
            high_scores = data.get("high_scores", [])
            player_stats = data.get("player_stats", {})
    except:
        high_scores = []
        player_stats = {}
        
    return high_scores, player_stats

def save_game_data(high_scores, player_stats):
    "Saves scores and stats back to score.json."
    data = {
        "high_scores": high_scores,
        "player_stats": player_stats
    }
    try:
        with open("score.json", "w") as file:
            json.dump(data, file, indent=4)
        print("\nScores and statistics successfully saved to score.json!")
    except:
        print("\nError saving scores and statistics to score.json.")

def load_word_bank():
    "Loads Player 1 categories and words from word_bank.json."
    try:
        with open("word_bank.json", "r") as file:
            data = json.load(file)
            word_bank = data.get("word_bank", {})
    except:
        word_bank = {}
        
    return word_bank

def save_word_bank(word_bank):
    "Saves Player 1 categories and words to word_bank.json."
    data = {
        "word_bank": word_bank
    }
    try:
        with open("word_bank.json", "w") as file:
            json.dump(data, file, indent=4)
        print("\nWord bank successfully saved to word_bank.json!")
    except:
        print("\nError saving word bank to word_bank.json.")

def manage_words_menu(word_bank):
    while True:
        print("\n--- WORD & CATEGORY MANAGER ---")
        print("1. Add a new category")
        print("2. Add a new word to an existing category")
        print("3. Back to Main Menu")
        choice = input("> ").strip()

        if choice == "1":
            new_cat = input("Enter the new category name: ").strip().title()
            if not new_cat:
                print("Category cannot be empty.")
                continue
            if new_cat in word_bank:
                print(f"Category '{new_cat}' already exists!")
            else:
                word_bank[new_cat] = []
                print(f"Category '{new_cat}' created successfully!")
                save_word_bank(word_bank)
        
        elif choice == "2":
            if not word_bank:
                print("No categories available. Create one first.")
                continue
            
            print("\nAvailable Categories:")
            cats = list(word_bank.keys())
            for i, cat in enumerate(cats, 1):
                print(f"{i}. {cat}")
            
            cat_choice = input("Select category number: ").strip()
            if not cat_choice.isdigit() or not (1 <= int(cat_choice) <= len(cats)):
                print("Invalid selection.")
                continue
            
            selected_cat = cats[int(cat_choice) - 1]
            new_word = input(f"Enter a new word for '{selected_cat}': ").strip().lower()
            
            if not all(new_word[i].isalpha() or new_word[i] in " -" for i in range(len(new_word))):
                print("Invalid entry! Words should only contain letters, spaces, or hyphens.")
                continue
            
            if new_word in word_bank[selected_cat]:
                print(f"'{new_word}' already exists in '{selected_cat}'! Duplicate rejected.")
            else:
                word_bank[selected_cat].append(new_word)
                print(f"Successfully added '{new_word}' to '{selected_cat}'!")
                save_word_bank(word_bank)
        
        elif choice == "3":
            break
        else:
            print("Invalid option, please choose 1, 2, or 3.")

def display_high_scores(high_scores):
    print("\n" + "*" * 20 + " TOP 5 HIGH SCORES " + "*" * 20)
    if not high_scores:
        print("No high scores recorded yet!")
    else:
        for i, entry in enumerate(high_scores[:5], 1):
            status = "Won" if entry["won"] else "Lost"
            print(f"{i}. {entry['player']} | Score: {entry['score']} pts | Status: {status}")
    print("~" * 50)

def display_statistics(player_stats):
    if not player_stats:
        print("\nNo player statistics recorded yet!")
        return
    
    print("\n" + "*" * 20 + " PLAYER STATISTICS " + "*" * 20)
    for player, stats in player_stats.items():
        games = stats["games_played"]
        wins = stats["wins"]
        losses = stats["losses"]
        win_rate = round((wins / games) * 100) if games > 0 else 0
        max_streak = stats["max_streak"]
        
        print(f"Player: {player}")
        print(f"Games Played: {games} | Wins: {wins} | Losses: {losses} | Win Rate: {win_rate}%")
        print(f"Longest Winning Streak: {max_streak}")
        
        cats_data = stats.get("categories", {})
        if cats_data:
            print("Category Stats:")
            for cat, c_data in cats_data.items():
                c_played = c_data["played"]
                c_wins = c_data["wins"]
                c_rate = round((c_wins / c_played) * 100) if c_played > 0 else 0
                print(f"{cat}: {c_wins}/{c_played} won ({c_rate}%)")

        if stats["missed_letters"]:
            most_missed = max(stats["missed_letters"], key=stats["missed_letters"].get)
            print(f"Most-Missed Letter: '{most_missed.upper()}' - {stats['missed_letters'][most_missed]} times")
        
    print("*" * 50)

def hangman_lv4():
    high_scores, player_stats = load_game_data()
    word_bank = load_word_bank()

    try:
        with open("Art.json", "r") as file:
            hangman_art = json.load(file)
    except:
        print("Please put the Art.json file for the ASCII Art of the hangman in the same directory as this file.")
        print("Confirm if you're currently at the directory of where this file is before running it.")
        return

    while True:
        print("\n" + "=" * 15 + " MAIN MENU " + "=" * 15)
        print("1. Play Game (Two-Player Mode)")
        print("2. Word & Category Manager")
        print("3. View Top 5 High Scores")
        print("4. View Player Statistics")
        print("5. Exit")
        
        menu_choice = input("> ").strip()
        
        if menu_choice == "2":
            manage_words_menu(word_bank)
            continue
        elif menu_choice == "3":
            display_high_scores(high_scores)
            continue
        elif menu_choice == "4":
            display_statistics(player_stats)
            continue
        elif menu_choice == "5":
            print("Exiting game. Goodbye!")
            return
        elif menu_choice == "1":
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

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

    has_words = any(word_bank.values())
    if has_words:
        print("\nHow would you like to set the secret word?")
        print("1. Pick randomly from stored Word Bank categories")
        print("2. Enter a custom word manually")
        word_choice = input("> ").strip()
        
        if word_choice == "1":
            valid_categories = [cat for cat, words in word_bank.items() if words]
            if valid_categories:
                chosen_category = random.choice(valid_categories)
                secret_word = random.choice(word_bank[chosen_category])
                hint = f"The category is: {chosen_category}"
                holder = "yes"
                print(f"Random word selected successfully from category '{chosen_category}'!")
            else:
                print("No words found in categories. Switched to manual entry.")
                secret_word = getpass.getpass("Player 1, enter your secret word: ")
                print()
                holder = "no"
        else:
            secret_word = getpass.getpass("Player 1, enter your secret word: ")
            print()
            holder = "no"
    else:
        print("\n[Word bank is empty. Please enter your secret word manually.]")
        secret_word = getpass.getpass("Player 1, enter your secret word: ")
        print()
        holder = "no"

    if holder == "no":
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

    print(f"Player 1 ({player1})'s data has been stored.")
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

    print("*" * 15 + f" You have {lives} lives, Have Fun. " + "*" * 15)

    while True:
        if game_over:
            break

        print(hangman_art[str(len(wrong))])
        
        if lives < 1:
            print("*" * 15 + f" YOU'RE OUT OF LIVES, IT WAS {secret_word.upper()} " + "*" * 15)
            print("*" * 15 + f" YOU LOSE " + "*" * 15)
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

                if guess.lower().strip() == "h":
                    break
                
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

            if guess.lower().strip() == "h":
                if holder == "yes" or holder == "y":
                    if not hint_used:
                        print(f"Category Hint was given as: {hint}")
                        hint_used = True
                        continue
                    else:
                        print("Oga you've used your hint already joor.")
                        continue
                else:
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
                    print("*" * 15 + " CONGRATULATIONS, YOU WIN " + "*" * 15)
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

                if w_guess.lower().strip() == "h":
                    break

                if len(w_guess) < 2:
                    print("Wow, so you're telling me that what you wrote is a word abi? Are you sure you went to school?.")
                    continue

                if w_guess.lower() in guessed:
                    print("You've guessed this already.")
                    continue

                break

            if w_guess.lower().strip() == "h":
                if holder == "yes" or holder == "y":
                    if not hint_used:
                        print(f"Category Hint was given as: {hint}")
                        hint_used = True
                        continue
                    else:
                        print("Oga you've used your hint already joor.")
                        continue
                else:
                    print("Sorry Player 1 didn't leave a hint for you.")
                    continue

            if w_guess.lower() == secret_word.lower():
                print("*" * 15 + " WOW! You actually got it. Impressive. " + "*" * 15)
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

    won = "_" not in display_word
    final_score = total_points if won else 0

    high_scores.append({"player": player2, "score": final_score, "won": won})
    high_scores = sorted(high_scores, key=lambda x: x["score"], reverse=True)[:5]

    if player2 not in player_stats:
        player_stats[player2] = {
            "games_played": 0, "wins": 0, "losses": 0, "categories": {},
            "current_streak": 0, "max_streak": 0, "missed_letters": {}
        }
    
    stats = player_stats[player2]
    stats["games_played"] += 1
    
    if 'chosen_category' in locals():
        if "categories" not in stats:
            stats["categories"] = {}
        if chosen_category not in stats["categories"]:
            stats["categories"][chosen_category] = {"played": 0, "wins": 0}
        stats["categories"][chosen_category]["played"] += 1
        if won:
            stats["categories"][chosen_category]["wins"] += 1

    if won:
        stats["wins"] += 1
        stats["current_streak"] += 1
        if stats["current_streak"] > stats["max_streak"]:
            stats["max_streak"] = stats["current_streak"]
    else:
        stats["losses"] += 1
        stats["current_streak"] = 0

    for char in wrong:
        if len(char) == 1 and char.isalpha():
            stats["missed_letters"][char] = stats["missed_letters"].get(char, 0) + 1

    save_game_data(high_scores, player_stats)

    display_high_scores(high_scores)
    display_statistics(player_stats)