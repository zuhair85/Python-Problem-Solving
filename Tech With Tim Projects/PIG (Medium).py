import random

def roll():
    return random.randint(1,6)

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2 - 4 players.')
    else:
        print("Invalid, try again")

max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print(f'\nPlayer number {player_idx + 1} turn has just started!')
        print(f"Your total score is: {player_scores[player_idx]}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")

            print(f'Your score is: {current_score}')

        player_scores[player_idx] += current_score
        print(f'Your total score is: {player_scores[player_idx]}')

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player number {winning_idx + 1} is the winner with a score of {max_score}!")


# My implementation:

# def roll_dice():
#     return random.randint(1, 6)
#
# player1_total_score = 0
# player2_total_score = 0
#
# while player1_total_score < 50 and player2_total_score < 50:
#     print("Player 1's turn:")
#     player1_turn_score = 0
#     while True:
#         score = roll_dice()
#         if score == 1:
#             print("You rolled a 1, you lose your turn!")
#             player1_turn_score = 0
#             break
#         else:
#             print(f"You rolled a {score}")
#             player1_turn_score += score
#             if input("Do want to keep rolling? (y/n): ") == 'n':
#                 break
#     player1_total_score += player1_turn_score
#     if player1_turn_score >= 50:
#         print(f"Player1 has {player1_total_score} score. He won!")
#         break
#     print(f"Player 1's score so far {player1_total_score}")
#
#     # Player2's turn
#     print("Player 2's turn:")
#     player2_turn_score = 0
#     while True:
#         score = roll_dice()
#         if score == 1:
#             print("You rolled a 1, you lose your turn!")
#             player2_turn_score = 0
#             break
#         else:
#             print(f"You rolled a {score}")
#             player2_turn_score += score
#             if input("Do want to keep rolling? (y/n): ") == 'n':
#                 break
#     player2_total_score += player2_turn_score
#     if player2_turn_score >= 50:
#         print(f"Player2 has {player2_total_score} score. He won!")
#         break
#     print(f"Player 2's score so far {player2_total_score}")