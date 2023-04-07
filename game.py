winning_options = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
# First user input
player1_option = input("Player 1 : Pick your weapon (Rock, paper scissors)\n")

# Option one for looping
while player1_option.lower() not in winning_options:
    print("This is not a option, please choose a valid option\n")
    player1_option = input(
        "Player 1 : Pick your weapon (Rock, paper scissors)\n")

# Second user input
player2_option = input("Player 2 : Pick your weapon (Rock, paper scissors)\n")

# Option two for looping
if player2_option.lower() not in winning_options:
    while True:
        print("This is not a option, please choose a valid option\n")
        player2_option = input(
            "Player 2 : Pick your weapon (Rock, paper scissors)\n")
        if player2_option.lower() in winning_options:
            break

if player1_option.lower() == player2_option.lower():
    print("It´s a tie\n")
elif winning_options[player1_option.lower()] == player2_option.lower():
    print("\nPlayer 1 wins!\n")
elif winning_options[player2_option.lower()] == player1_option.lower():
    print("\nPlayer 2 wins!\n")

print("Player 1 option:", player1_option)
print("Player 2 option:", player2_option)
