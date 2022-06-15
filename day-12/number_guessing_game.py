import random
from art import logo

EASY_MODE = 10
HARD_MODE = 5


def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {number}")

    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if mode == "easy":
        remaining_attempts = EASY_MODE
    else:
        remaining_attempts = HARD_MODE

    while remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print(f"You got it! The answer was {number}")
            break

        remaining_attempts -= 1

        if remaining_attempts == 0:
            print(f"You've run out of guesses, you lose. The number was {number}.")
        else:
            print("Guess again.")


main()