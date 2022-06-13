from art import logo
import random

import os

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Loop for BlackJack game when losing/winning
continue_game = True

while continue_game:
    # Start user and computer hand with one card
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)

    # TODO Format print to show A instead of 11 and J, Q, K sometimes instead of 10?
    draw_card = True

    while draw_card:
        print(f"Your cards are {user_cards}, your current score {user_sum}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_sum == 21 and computer_sum == 21:
            print(f"Computer's final hand is {computer_cards}, their final score {computer_sum}")
            print("It is a draw!")
        elif user_sum == 21:
            print(f"Computer's final hand is {computer_cards}, their final score {computer_sum}")
            print("You win!")
            break
        elif computer_sum == 21:
            print(f"Computer's final hand is {computer_cards}, their final score {computer_sum}")
            print("You lose!")
            break
        elif user_sum > 21:
            print(f"Computer's final hand is {computer_cards}, their final score {computer_sum}")
            print("You drew over, you lose!")
            break
        elif computer_sum > 21:
            print(f"Computer's final hand is {computer_cards}, their final score {computer_sum}")
            print(f"Computer drew over, you win!")
            break
        else:
            hit = input("Type 'h' to hit or 's' to stand: ").lower()
            if hit == 'h':
                user_cards.append(random.choice(cards))
                # TODO add a check for 11 or 1
                # The computer follows a policy of drawing when under 17
                if computer_sum < 17:
                    computer_cards.append(random.choice(cards))
                    computer_sum = sum(computer_cards)

                user_sum = sum(user_cards)

            elif hit == 's':
                print(f"Your final hand is {user_cards}, your final score {user_sum}")
                print(f"Computer's final hand is {computer_cards}, their final score {computer_sum}")

                if user_sum < computer_sum:
                    print("You lose!")
                elif user_sum > computer_sum:
                    print("You win!")
                else:
                    print("It's a draw!")
                draw_card = False
            # TODO Add loop here for invalid character

    should_continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

    if should_continue_game == 'y':
        continue_game = True
        os.system('clear')
    elif should_continue_game == 'n':
        continue_game = False
        print("Goodbye!")
    # TODO Handle case of invalid character input






