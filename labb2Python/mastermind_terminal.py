from random import choice

CODE_LENGTH = 4
PLAYER_GUESSES = 8
MASTERMIND_COLORS = ("red", "blue", "green", "yellow", "white", "black", "purple", "orange")

computer_color_code =  []
player_color_code = []

#generate computer color code
for i in range(0, CODE_LENGTH):
    computer_color_code.append(choice(MASTERMIND_COLORS))

def give_feed_back(computer_color_code, player_color_code):
    #break om de är lika
    if computer_color_code == player_color_code: return True

    #lägg till index i white_pegs om computer_color_code[i] är lika med player_color_code[i]
    white_pegs = [i for i in range(0, CODE_LENGTH) if computer_color_code[i] == player_color_code[i]]

    #lägg till index i red_pegs om computer_color_code färgen finns i player_color_code
    red_pegs = [i for i in range(0, CODE_LENGTH) if computer_color_code[i] in player_color_code]

    print(f"White pegs:{len(white_pegs)} Red pegs:{len(red_pegs)}")


#total times the player can try to figure out the color code
for i in range(0, PLAYER_GUESSES):

    #generates list with player_color_code
    for i in range(0, CODE_LENGTH):
        player_color_code.append(input("enter ur guess: "))

    print(f"player color code {player_color_code}")
    print(f"computer color code {computer_color_code}")
    if give_feed_back(computer_color_code, player_color_code):
        print("congrats the player won")
        break
    player_color_code = []
