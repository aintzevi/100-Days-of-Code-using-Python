from art import logo
import random

import os

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Loop for BlackJack game when losing/winning
continue_game = True

while continue_game:
    # Start user and computer hand with one card
    user_cards = [random.choice(cards)]
    computer_cards = [random.choice(cards)]
    new_card_user = random.choice(cards)
    new_card_computer = random.choice(cards)

    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)

    # TODO turn this check into helper function
    # Change 11 to 1 if needed
    if new_card_user == 11 and user_sum > 10:
        new_card_user = 1
    if new_card_computer == 11 and computer_sum > 10:
        new_card_computer = 1

    user_cards.append(new_card_user)
    computer_cards.append(new_card_computer)

    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)

    draw_card = True

    while draw_card:
        print(f"Your cards are {user_cards}, your current score {user_sum}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_sum == 21 and computer_sum == 21:
            print(f"Computer's final hand is {computer_cards}, their final score {computer_sum}")
            print("It it's a draw!")
            break
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
            while True:
                hit = input("Type 'h' to hit or 's' to stand: ").lower()
                if hit == 'h':
                    new_card_user = random.choice(cards)
                    if new_card_user == 11 and user_sum > 10:
                        new_card_user = 1
                    user_cards.append(new_card_user)
                    # The computer follows a policy of drawing when under 17
                    if computer_sum < 17:
                        new_card_computer = random.choice(cards)
                        if new_card_computer == 11 and computer_sum > 10:
                            new_card_computer = 1
                        computer_cards.append(new_card_computer)
                        computer_sum = sum(computer_cards)

                    user_sum = sum(user_cards)
                    break
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
                    break
                else:
                    print("There is no option for this letter, try again!")
    while True:
        should_continue_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

        if should_continue_game == 'y':
            continue_game = True
            os.system('clear')
            break
        elif should_continue_game == 'n':
            continue_game = False
            print("Goodbye!")
            break
        else:
            print("There is no option for this letter, try again!")






