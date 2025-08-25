import random

# Import words from words.py
from words import hangman_words
from stages import hangman_stage
from constants import *


def game_instructions():
    """Detailed instructions for user on how to play the game"""
    print(
        """

Here are the games instructions:\n
1. A random word has been generated, you'll need to guess the word one
letter at a time, before you run out of lives.\n
2. For each incorrect answer, parts of your hangman will appear.\n
3. When the hangman is complete, you have lost the game! Guess the word
    correctly before your hangman has built, and you've won the game!\n

Time to start playing...
    """
    )


def chosen_word():
    """Choose a random word"""
    return random.choice(hangman_words)


game_word = chosen_word()


def display_game():
    """
    Create the hangman space,
    Show the number of letters in the word to be guessed
    """
    word = game_word
    length = " _ " * len(word)
    print(f"Word to be guessed (no. of letters: {len(word)}): {length}\n")


def play_game():
    """
    Starts the interactive hangman game.
    Shows input for user to input their letter; with validation to prevent
    numbers / multiple letters  / already guessed letters being entered

    Checks if user guess is the the word generated in chosen_word, if yes
    reveals the letter. If no, one life lost and part of the hangman is built
    """
    word = game_word
    guessed_letters = []
    lives = 7
    game_won = False

    while lives > 0:
        print("------------------------------------------------------------\n")
        # Allow user to enter a letter
        guess = input("Enter your guess (one letter only):\n").strip().lower()

        # makes sure one letter has been entered
        if len(guess) == 1 and guess.isalpha():
            # check if guess has been entered before
            if guess in guessed_letters:
                print(f"'{guess}' has already been guessed, try again.")
            else:
                guessed_letters.append(guess)
                print(f"Guessed letters: {', '.join(guessed_letters)}\n")
            # check if guess is in the word
            if guess in word:
                print(
                    f"""Good guess! Letter '{guess}' is in the word.
                {hangman_stage[7 - lives]}"""
                )
            else:
                lives -= 1
                print(
                    f"""
                    Incorrect guess! Try again...
                    {hangman_stage[7 - lives]}"""
                )
            if all(letter in guessed_letters for letter in word):
                game_won = True
                break
        else:
            print(f"You entered: '{guess}'. Please enter a single letter.\n")

        display = " ".join(
            [letter if letter in guessed_letters else "_" for letter in word]
        )
        print(f"Word to be guessed (no. of letters: {len(word)}): {display}\n")

    if game_won:
        print(f"""Congratulations, the word was '{word}'!\n""")
    else:
        print(f" Better luck next time! The word was: {word}.\n")

    if game_won == True or lives == 0:
        main_menu = input("Enter any key to go back to the main menu:\n")
        if main_menu == "":
            main()


def main():
    """
    Shows welcome message
    Allows user to decide how to proceed:
        1 = instructions
        2 = proceed to the game
        3 = exit the game
    """
    welcome_message()

    while True:
        choice = input("Enter a number to proceed:\n").strip()

        if choice.isdigit():
            chosen_step = int(choice)
            if chosen_step == 1:
                game_instructions()
                display_game()
                print(hangman_stage[0])
                play_game()
                break
            elif chosen_step == 2:
                display_game()
                print(hangman_stage[0])
                play_game()
                break
            elif chosen_step == 3:
                print("That's a shame... See you next time!!!!")
                break
            else:
                print("Please enter 1, 2 or 3.")
        else:
            print(f"You have entered '{choice}'. Please enter 1-3 to continue")


main()
