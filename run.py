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

    while not game_won and lives > 0:
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
                        f"""
                    Good guess! Letter '{guess}' is in the word.

                    {hangman_stage[7 - lives]}
                    """
                    )
                else:
                    lives -= 1
                    print(
                        f"""
                Incorrect guess! Try again...

                    {hangman_stage[7 - lives]}
                    """
                    )

                if all(letter in guessed_letters for letter in word):
                    game_won = True
        else:
            print(f"Invalid input: '{guess}'. Please enter a single letter.\n")

        # Loop through each letter in word, if not included show underscore
        # If correct guess reveal letter
        # Join utilised to show spaces between letters
        display = " ".join(
            [letter if letter in guessed_letters else "_" for letter in word]
        )
        print(f"Word to be guessed (no. of letters: {len(word)}): {display}\n")

    if game_won:
        print(f"Congratulations, you have correctly guessed the word: {word}!")
    else:
        print(f"Better luck next time! The word was: {word}")


def main():
    game_instructions()
    display_game()
    play_game()


main()
