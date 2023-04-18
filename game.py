from threading import Thread
from network import connect, send

winning_options = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def send_message():
    while True:
        send(input())


def react_on_messages(timestamp, user, message):

    global me, opponent, myChoice, opponentChoice, winning_options

    # listen to who joins the channel...
    if user == 'system' and 'joined channel' in message:
        player = message.split(' ')[1]
        if player != me:
            opponent = player
            print(opponent + ' has joined!\n')
            print('Let us play!\n')
            print('Choose paper, rock or scissors:')

    # If your choice is invalid
    if user == me and message not in ['paper', 'rock', 'scissors']:
        print('You must choose paper, rock or scissors!\n')

    # Remember my choice
    if user == me and message in ['paper', 'rock', 'scissors']:
        myChoice = message

    if user == opponent and message not in ['paper', 'rock', 'scissors']:
        print('You must choose paper, rock or scissors!\n')

    # Remember the opponent's choice
    if user == opponent and message in ['paper', 'rock', 'scissors']:
        opponentChoice = message

    # Both me and my opponent have made choices
    if myChoice != '' and opponentChoice != '':
        print('\nYou chose ' + myChoice)
        print('and ' + opponent + ' chose ' + opponentChoice)
        # now we can determine who has won (this round)
        if myChoice.lower() == opponentChoice.lower():
            print("It´s a tie!\n")
        elif winning_options[myChoice.lower()] == opponentChoice.lower():
            print("\nPlayer 1 wins!\n")
        elif winning_options[opponentChoice.lower()] == myChoice.lower():
            print("\nPlayer 2 wins!\n")
        else:
            print('Not sure who won :(')
        # # reset choices
        myChoice = ''
        opponentChoice = ''
        print('\nChoose paper, rock or scissors:')


# START -> Wait for player to enter name and channel
opponent = ''
myChoice = ''
opponentChoice = ''
me = input('Your name: ')
channel = input('Channel to join or create: ')
# connect to (or create) a channel, with a user name
connect(channel, me, react_on_messages)
# start non-blocking thread to input and send messages
Thread(target=send_message).start()
