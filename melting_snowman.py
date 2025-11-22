import random
from ascii_stages import STAGES

# Liste der geheimen Wörter
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt den aktuellen Galgenmännchen-Zustand und das teilweise erratene Wort an."""
    print(STAGES[mistakes])
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Secret Word is:", display)


def get_random_word():
    """Wählt ein zufälliges Wort aus der Liste."""
    return random.choice(WORDS)


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    guessed_letters = []
    mistakes = 0

    # Hauptschleife des Spiels
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        # Validierung der Eingabe
        if len(guess) != 1 or not guess.isalpha():
            print("Ungültige Eingabe. Bitte gib einen einzelnen Buchstaben ein.")
            continue

        if guess in guessed_letters:
            print(f"Du hast den Buchstaben '{guess}' bereits geraten.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            # Überprüfung auf vollständigen Erfolg
            word_guessed = all(letter in guessed_letters for letter in secret_word)
            if word_guessed:
                display_game_state(mistakes, secret_word, guessed_letters)
                print(f"Glückwunsch! Du hast das Wort '{secret_word}' erraten! ")
                break

        else:
            mistakes += 1
        # Überprüfung auf Spielende (Niederlage)
        if mistakes == len(STAGES) - 1:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Zu viele Fehler! Der Schneemann ist geschmolzen! Das Wort war: {secret_word}")
            break


if __name__ == "__main__":
    play_game()