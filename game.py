from command_line_chat import *
from network import *


winning_options = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def handle_game_message(timestamp, user, message):
    global player1_option, player2_option, game_started
    react_on_messages(timestamp, user, message)
    if user != player1_name and user != player2_name:
        return
    elif user == player1_name:
        player1_option = message
    elif user == player2_name:
        player2_option == message

# prompt players to start game


def game_loop():
    while True:
        if not game_started:
            send(
                f"{player1_name} and {player2_name} are ready to play. Type 'start' to begin.")
            while True:
                choice = input().strip().lower()
                if choice == "start":
                    game_started = True
                    break
                else:
                    send("Invalid choice. Type 'start' to begin.")


def game_initiation():
    # First user input
    player1_option = input(
        "Player 1 : Pick your weapon (Rock, paper scissors)\n")
    # Option one for looping
    while player1_option.lower() not in winning_options:
        print("This is not a option, please choose a valid option\n")
        player1_option = input(
            "Player 1 : Pick your weapon (Rock, paper scissors)\n")
    # Second user input
    player2_option = input(
        "Player 2 : Pick your weapon (Rock, paper scissors)\n")
    # Option two for looping
    if player2_option.lower() not in winning_options:
        while True:
            print("This is not a option, please choose a valid option\n")
            player2_option = input(
                "Player 2 : Pick your weapon (Rock, paper scissors)\n")
            if player2_option.lower() in winning_options:
                break


def choose_winner():
    global player1_option, player2_option
    if player1_option.lower() == player2_option.lower():
        print("It´s a tie!\n")
    elif winning_options[player1_option.lower()] == player2_option.lower():
        print("\nPlayer 1 wins!\n")
    elif winning_options[player2_option.lower()] == player1_option.lower():
        print("\nPlayer 2 wins!\n")

# Reset


def reset_game():
    global player1_name, player2_name, player1_option, player2_option, game_started
    player1_name = None
    player2_name = None
    player1_option = None
    player2_option = None
    game_started = False


player_name = input("Enter your name: ")
channel = input("Enter channel name: ")

connect(channel, player_name, react_on_messages)

print("Player 1 option:", player1_option)
print("Player 2 option:", player2_option)
