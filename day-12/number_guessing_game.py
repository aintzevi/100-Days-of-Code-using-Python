import random
from art import logo

EASY_MODE = 10
HARD_MODE = 5

def set_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if mode == "easy":
        return EASY_MODE
    else:
        return HARD_MODE


def check_answer(guess, answer, remaining_attempts):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}")

    return remaining_attempts - 1


def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {number}")

    remaining_attempts = set_difficulty()

    guess = 0

    while guess != number and remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        remaining_attempts = check_answer(guess, number, remaining_attempts)

        if remaining_attempts == 0:
            print(f"You've run out of guesses, you lose. The number was {number}.")
        else:
            print("Guess again.")


main()