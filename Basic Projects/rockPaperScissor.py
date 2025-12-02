# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
# •	Rock beats scissors
# •	Scissors beats paper
# •	Paper beats rock

def get_winner(p1, p2):
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if p1 == p2:
        return "It's a tie!"
    elif rules[p1] == p2:
        return "Player 1 wins! 🎉"
    else:
        return "Player 2 wins! 🎉"

def is_valid(choice):
    return choice in ["rock", "paper", "scissors"]

while True:
    print("\n--- Rock Paper Scissors ---")
    player1 = input("Player 1, enter rock, paper, or scissors: ").lower()
    player2 = input("Player 2, enter rock, paper, or scissors: ").lower()

    if not (is_valid(player1) and is_valid(player2)):
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        continue

    print(f"\nPlayer 1 chose: {player1}")
    print(f"Player 2 chose: {player2}")
    print(get_winner(player1, player2))

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
