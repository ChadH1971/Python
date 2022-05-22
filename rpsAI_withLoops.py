from random import randint
print("Rock...")
print("Paper...")
print("Scissors...\n")
games = input("How many games in the series? ")
print(f"This will be a 'BEST OF' {games} series")
game_count = 0
player_score = 0
computer_score = 0
while game_count < int(games):

    player1 = input("Player, make your move: (q to quit)").lower()
    rand_num = randint(0, 2)
    game_count += 1
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else: computer = "scissors"
    
    if player1 == computer:
        print("It's a tie")
    elif player1 == "rock":
        if computer == "scissors":
            print("Player 1 wins")
            player_score += 1
        elif computer == "paper":
            print("Computer wins")
            computer_score += 1
    elif player1 == "paper":
        if computer == "rock":
            print("Player 1 wins")
            player_score += 1
        elif computer == "scissors":
            print("Computer wins")
            computer_score += 1
    elif player1 == "scissors":
        if computer == "paper":
            print("Player 1 wins")
            player_score += 1
        elif computer == "rock":
            print("Computer wins")
            computer_score += 1
    elif player1 == "q":
        break
    else:
        print("Please play a valid move or q to quit")
        game_count -= 1

print(f"\nFINAL SCORE: Player: {player_score} to Computer: {computer_score}\n")
if player_score > computer_score:
    print("Congratulations! YOU WIN!!!")
else:
    print("Sorry, the computer wins")