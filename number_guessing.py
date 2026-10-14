import random

def get_guess(min_number, max_number):
    """Get a valid number from the user."""
    while True:
        try:
            guess = int(input(f"Enter your guess ({min_number}-{max_number}): "))
            if min_number <= guess <= max_number:
                return guess
            print(f"Please enter a number between {min_number} and {max_number}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_round():
    """Run one round of the number guessing game."""
    minimum = 1
    maximum = 100
    attempts = 7
    secret_number = random.randint(minimum, maximum)

    print("\n--- Number Guessing Game ---")
    print(f"I have chosen a number between {minimum} and {maximum}.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        guess = get_guess(minimum, maximum)
        attempts_left = attempts - attempt

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempt} attempt(s).")
            return

        if guess > secret_number:
            print("Too High! Try a smaller number.")
        else:
            print("Too Low! Try a bigger number.")

        print(f"Attempts left: {attempts_left}")

    print(f"Sorry, you are out of tries. The secret number was {secret_number}.")


def main():
    """Start the game and allow the user to play again."""
    while True:
        play_round()
        while True:
            again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if again in ("yes", "y"):
                break
            if again in ("no", "n"):
                print("Thanks for playing!")
                return
            print("Please enter yes or no.")


if __name__ == "__main__":
    main()
