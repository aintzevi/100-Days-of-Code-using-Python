from game_data import data
import art
import random
import os


def generate_random_account():
    """Get random account from a data file and return it"""
    return random.choice(data)


def format_data(account):
    """Format the account data into a printable form"""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}."


def check_answer(guess, a_followers, b_followers):
    """Checks if the user guessed the correct option based on the max followers of each option.
    :returns True if the user was correct, or False if the user was wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    # Get two random accounts - possible that they even are the same account
    account_a = generate_random_account()

    is_correct = True

    while is_correct:
        print(art.logo)

        account_b = generate_random_account()

        # Format account data into printable format.
        print("Compare A: " + format_data(account_a))
        print(art.vs)
        print("Against B: " + format_data(account_b))

        guess = input("Who has more followers? Type 'A' or 'B': ")

        is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")

        account_a = account_b


def main():
    while True:
        game()
        continue_game = input("Would you like to continue? Type 'yes' or 'no': ").lower()

        if continue_game == "no":
            print("Bye-bye!")
            break
        os.system('clear')


main()