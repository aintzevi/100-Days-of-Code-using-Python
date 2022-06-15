from art import logo
import random
import os


def draw_card():
    return random.choice(cards)


def calculate_score(cards_list):
    score = sum(cards_list)
    if cards_list.__contains__(11) and score > 21:
        cards_list[cards_list.index(11)] = 1
        score -= 10
    if score == 21:
        score = 0

    return score


print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Loop for BlackJack game when losing/winning
continue_game = True

while continue_game:
    user_cards = []
    computer_cards = []
    # Start user and computer hand with one card
    for _ in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())

    draw_next_card = True

    while draw_next_card:
        calculate_score(user_cards)
        print(f"Your cards are {user_cards}, your current score {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        if calculate_score(user_cards) == 0 and calculate_score(computer_cards) == 0:
            print(f"Computer's final hand is {computer_cards}, you both have a blackjack!")
            print("It it's a draw!")
            break
        elif calculate_score(user_cards) == 0:
            print(f"Computer's final hand is {computer_cards}, their final score {calculate_score(computer_cards)}.")
            print("You win with a blackjack!")
            break
        elif calculate_score(computer_cards) == 0:
            print(f"Computer's final hand is {computer_cards}, they have a blackjack!")
            print("You lose!")
            break
        elif calculate_score(user_cards) > 21:
            print(f"Computer's final hand is {computer_cards}, their final score {calculate_score(computer_cards)}")
            print("You drew over, you lose!")
            break
        elif calculate_score(computer_cards) > 21:
            print(f"Computer's final hand is {computer_cards}, their final score {calculate_score(computer_cards)}")
            print(f"Computer drew over, you win!")
            break
        else:
            while True:
                hit = input("Type 'h' to hit or 's' to stand: ").lower()
                if hit == 'h':
                    user_cards.append(draw_card())
                    # The computer follows a policy of drawing when under 17
                    if calculate_score(computer_cards) < 17:
                        computer_cards.append(draw_card())
                    break
                elif hit == 's':
                    print(f"Your final hand is {user_cards}, your final score {calculate_score(user_cards)}")
                    print(f"Computer's final hand is {computer_cards}, their final score {calculate_score(computer_cards)}")

                    if calculate_score(user_cards) < calculate_score(computer_cards):
                        print("You lose!")
                    elif calculate_score(user_cards) > calculate_score(computer_cards):
                        print("You win!")
                    else:
                        print("It's a draw!")
                    draw_next_card = False
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






