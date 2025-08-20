import random

# Import words from words.py
from words import hangman_words
from stages import hangman_stage

print(
    """
===============================================================================
|                                                                             |
|                             Welcome to Hangman!                             |
|                                                                             |
===============================================================================
"""
)


def game_instructions():
    """Detailed instructions for user on how to play the game"""
    print(
        """
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
    print(
        """
    []==============
    []             |
    []
    []
    []
    []
    []
    []
    []
    ==============================
    """
    )

    word = game_word
    print(word)  # added for testing purposes
    length = " _ " * len(word)
    print(f"Word to be guessed (no. of letters: {len(word)}): {length}")


def main():
    game_instructions()
    display_game()


main()
