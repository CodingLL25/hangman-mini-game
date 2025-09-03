from colorama import Fore


def welcome_message():
    """
    Welcome message shown at the start of the game
    Describes what the game is, and how to proceed to next step"""
    print(
        Fore.RESET
        + """
===============================================================================
|                                                                             |
|                             Welcome to Hangman!                             |
|                                                                             |
===============================================================================


Enter 1 to see the instructions, 2 to start the game, or 3 to exit the game.\n
"""
    )


def game_instructions():
    """Detailed instructions for user on how to play the game"""
    print(
        Fore.RESET
        + """

Welcome to Hangman! Game instructions shown below:

    1. Choose a category to play from based on your interests.

    2. A random word will be generated from this category, you'll need to guess
    the word one letter at a time, before you run out of lives.

    3. For each incorrect answer, parts of your hangman will appear.

    4. When the hangman is complete, you have lost the game! Guess the word
    correctly before your hangman has built, and you've won the game!

    Time to start playing...
    """
    )
