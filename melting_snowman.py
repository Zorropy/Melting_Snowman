import random
from ascii_stages import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list) -> None:
    """
    Displays the current hangman/snowman state and the partially guessed word.

    :param mistakes: The number of incorrect guesses made so far.
    :param secret_word: The word the player is trying to guess.
    :param guessed_letters: A list of letters the player has already guessed.
    :return: None
    """
    print(STAGES[mistakes])
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Secret Word is:", display)


def get_random_word() -> str:
    """
    Selects a random word from the list.

    :return: A randomly selected word string.
    """
    # Select a random word from the WORDS list
    return random.choice(WORDS)


def play_game() -> None:
    """
    The main game loop for 'Snowman Meltdown' (Hangman).

    :return: None
    """
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    guessed_letters = []
    mistakes = 0

    # Main game loop
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        # Prompt the user for a letter guess
        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            # Check for complete success
            word_guessed = all(letter in guessed_letters for letter in secret_word)
            if word_guessed:
                display_game_state(mistakes, secret_word, guessed_letters)
                print(f"Congratulations! You guessed the word '{secret_word}'! 🎉")
                break

        else:
            # Increment mistakes for an incorrect guess
            mistakes += 1

        # Check for game over (loss condition)
        if mistakes == len(STAGES) - 1:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Too many mistakes! The snowman has melted! The word was: {secret_word} 🥶")
            break


if __name__ == "__main__":
    play_game()