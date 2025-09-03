import random
import os
from colorama import Fore
from words import hangman_words
from stages import hangman_stage
from constants import *


def generate_word():
    """
    Allow player to input category of interest.
    Confirms the chosen category for the hangman game.
    Generates random word to be guessed, and shows number of letters in the
    word to be guessed as well as underscores per letter."""
    categories = {1: "animals", 2: "movies", 3: "flowers"}

    while True:
        print(
            Fore.RESET
            + """
You'll need to choose a category of words to play from...

Categories of words available:
    1: types of animals
    2: movie
    3: types of flowers

"""
        )

        category_choice = input("Choose your category (1, 2 or 3):\n").strip()
        if category_choice.isdigit():
            category_number = int(category_choice)

            if category_number in categories:
                selected_category = categories[category_number]
                word = random.choice(hangman_words[selected_category])
                length = " _ " * len(word)
                print(
                    Fore.CYAN
                    + f"""

You chose {selected_category}

Word to be guessed (no. of letters: {len(word)}): {length}\n"""
                )
                return word
            else:
                print(Fore.RED + "Please enter 1, 2 or 3 to continue.")
        else:
            print(Fore.RED + "Please enter 1, 2 or 3 to continue.")


def play_game(word):
    """
    Starts the interactive hangman game.
    Shows input for user to input their letter; with validation to prevent
    numbers / multiple letters  / already guessed letters being entered
    Checks if user guess is the the word generated in generate_word, if yes
    reveals the letter. If no, one life lost and part of the hangman is built
    """

    guessed_letters = []
    lives = 7
    game_won = False

    while lives > 0:
        print("************************************************************\n")
        # Allow user to enter a letter
        guess = input("Enter your guess (one letter only):\n").strip().lower()

        # makes sure one letter has been entered
        if len(guess) == 1 and guess.isalpha():
            # check if guess has been entered before
            if guess in guessed_letters:
                print(Fore.RED + f"'{guess}' has already been guessed.")
            else:
                guessed_letters.append(guess)
                print(f"Guessed letters: {', '.join(guessed_letters)}\n")
                # check if guess is in the word
                if guess in word:
                    print(
                        Fore.GREEN
                        + f"""
                Good guess! Letter '{guess}' is in the word.

                {Fore.RESET + hangman_stage[7 - lives]}"""
                    )
                else:
                    lives -= 1
                    print(
                        Fore.RED
                        + f"""
Incorrect guess! '{guess}' is not in the word, try again...
                {Fore.RESET + hangman_stage[7 - lives]}"""
                    )

                if all(letter in guessed_letters for letter in word):
                    game_won = True
                    break
        else:
            print(Fore.RED + f"Single letters only, you entered:'{guess}'.\n")

        display = " ".join(
            [letter if letter in guessed_letters else "_" for letter in word]
        )
        print(
            Fore.RESET
            + f"Word to be guessed (no. of letters: {len(word)}): {display}\n"
        )

    if game_won:
        print(Fore.GREEN + f"""Congratulations, the word was '{word}'!\n""")
    else:
        print(Fore.RED + f"Better luck next time! The word was: {word}.\n")

    if game_won or lives == 0:
        input(Fore.RESET + "Enter any key and/or enter to go to main menu:\n")
        os.system("cls" if os.name == "nt" else "clear")
        main()


def main():
    """
    Shows welcome message
    Allows user to decide how to proceed:
    If 1 selected, user shown instructions then asked to choose word category
    If 2 selected, user asked to choose word category
    If 3, user exits the game
    """

    welcome_message()

    while True:
        choice = input(Fore.RESET + "Enter a number to proceed:\n").strip()

        if choice.isdigit():
            chosen_step = int(choice)
            if chosen_step == 1:
                os.system("cls" if os.name == "nt" else "clear")
                game_instructions()
            elif chosen_step == 2:
                os.system("cls" if os.name == "nt" else "clear")
                word = generate_word()
                word = word.lower()
                print(Fore.RESET + hangman_stage[0])
                play_game(word)
                break
            elif chosen_step == 3:
                print(Fore.RED + "That's a shame... See you next time!!!!")
                break
            else:
                print(Fore.RED + "Please enter 1, 2 or 3.")
        else:
            print(Fore.RED + f"You entered '{choice}'. Enter 1-3 to continue")


if __name__ == "__main__":
    main()
