# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

player1 = input("PLAYER 1: Rock Paper or Scissors?? ")
player1 = player1.lower()
while player1 not in ['rock', 'paper', 'scissors']:
    player1 = input("PLAYER 1: Rock Paper or Scissors?? ").lower()
    player1 = player1.lower()

player2 = input("PLAYER 2: Rock Paper or Scissors?? ").lower()
while player2 not in ['rock', 'paper', 'scissors']:
    player2 = input("PLAYER 2: Rock Paper or Scissors?? ").lower()

if player1 == player2:
    print("It's a draw")
elif (player1 == "rock" and player2 == "scissors") or (
        player1 == "scissors"
        and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
    print(f'Player 1 wins! {player1} beats {player2}')
else:
    print(f'Player 2 wins! {player2} beats {player1}')