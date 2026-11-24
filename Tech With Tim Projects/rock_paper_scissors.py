import random
options = ["rock", "paper", "scissors"]

computer_wins = 0
player_wins = 0
ties = 0

while True:
    player_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player_choice == "q":
        break

    if player_choice not in options:
        continue

    computer_choice = random.choice(options)

    if computer_choice == player_choice:
        print("It's a tie!")
        ties += 1
    elif computer_choice == "rock" and player_choice == "scissors":
        print('Computer Won!')
        computer_wins += 1
    elif computer_choice == 'paper' and player_choice == 'rock':
        print('Computer Won!')
        computer_wins += 1
    elif computer_choice == 'scissors' and player_choice == 'paper':
        print('Computer Won!')
        computer_wins += 1
    else:
        print('You Won!')
        player_wins += 1

print("You won", player_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Game tied", ties, "times")
print("Goodbye!")

