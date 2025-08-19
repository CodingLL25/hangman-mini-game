# Import words from words.py
from words import hangman_words

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


def main():
    game_instructions()


main()
