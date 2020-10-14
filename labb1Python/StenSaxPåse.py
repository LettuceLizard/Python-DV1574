from random import choice

dict1 = {"stensax":True, "stenpåse":False,
        "påsesax":False, "påsesten":True,
        "saxsten":False, "saxpåse":True}

def decide_winner():
    try:
        winner = dict1[player_choice+computer_choice]

        if winner: print("player is the winner")
        else: print("computer is the winner")

    except KeyError:
        print("draw")

while True:
    player_choice = input("what is ur choice ")
    computer_choice = choice(("sten", "sax", "påse"))

    if player_choice == "quit" or player_choice == "q":
        print("thx for playing")
        break

    elif player_choice not in ["sten", "sax", "påse"]: print("dåligt svar skriv in det igen")
    else: decide_winner()
