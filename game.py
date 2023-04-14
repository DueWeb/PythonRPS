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
    global player1_name, player2_name
    while True:
        if not game_started:
            send(f"({player1_name} and {player2_name} are ready to play. Type 'start' to begin.")
            while True:
                choice = input().strip().lower()
                if choice == "start":
                    game_started = True
                    break
                else:
                    send("Invalid choice. Type 'start' to begin.")
            # Prompt player 1 to choose option
            send(f"{player1_name}, choose your option (rock, paper, or scissors):")
        else:
            if not player1_option:
                send(f"{player1_name}, choose your option (rock, paper, or scissors):")
            elif not player2_option:
                send(f"{player2_name}, choose your option (rock, paper, or scissors):")
            else:
                choose_winner()
                reset_game()
                # Prompt player 1 to choose option
                send(f"{player1_name}, choose your option (rock, paper, or scissors):")


def game_initiation():
    global player1_option, player2_option
    # Prompt player 1 for their weapon choice
    player1_option = input(
        "Player 1: Pick your weapon (rock, paper, scissors)\n").strip().lower()
    while player1_option not in winning_options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player1_option = input(
            "Player 1: Pick your weapon (rock, paper, scissors)\n").strip().lower()

    # Prompt player 2 for their weapon choice
    player2_option = input(
        "Player 2: Pick your weapon (rock, paper, scissors)\n").strip().lower()
    while player2_option not in winning_options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player2_option = input(
            "Player 2: Pick your weapon (rock, paper, scissors)\n").strip().lower()


def choose_winner():
    global player1_option, player2_option
    if player1_option == player2_option:
        print("It's a tie!")
    elif winning_options[player1_option] == player2_option:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


def reset_game():
    global player1_name, player2_name, player1_option, player2_option, game_started
    player1_name = None
    player2_name = None
    player1_option = None
    player2_option = None
    game_started = False


player_name = input("Enter your name: ")
channel = input("Enter channel name: ")

connect(channel, player_name, handle_game_message)

player1_name = player_name
player2_name = input("Enter player 2 name: ")

game_started = False
player1_option = None
player2_option = None

while True:
    reset_game()
    game_loop()
    game_initiation()
    choose_winner()
