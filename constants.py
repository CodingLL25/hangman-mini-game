from colorama import Fore


def welcome_message():
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

 Welcome to Hangman! Game instructions shown below:\n

    1. A random word has been generated, you'll need to guess the word one
    letter at a time, before you run out of lives.\n
    2. For each incorrect answer, parts of your hangman will appear.\n
    3. When the hangman is complete, you have lost the game! Guess the word
    correctly before your hangman has built, and you've won the game!\n

    Time to start playing...
    """
    )
