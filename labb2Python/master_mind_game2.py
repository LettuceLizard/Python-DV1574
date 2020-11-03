import master_mind_GUI
from random import randint

my_game_window = master_mind_GUI.create_GUI()

#SETTINGS
CHEATS = True #if cheats are allowed True = cheats are on

#SETTINGS if the library was modular
PLAYER_GUESSES = 7
CODE_LENGTH = 4
NUMBER_OF_DIFFERENT_COLORS = 5

#Dont change aka (DO NOT FUCK WITH THESE SETTINGS)
STANDINGS = "Loser"
correct_place = 0
current_loop = 0

#computer_color_code = list with the length of CODE_LENGTH = 4 ex [2, 3, 1, 4]
computer_color_code = [randint(0, NUMBER_OF_DIFFERENT_COLORS) for e in range(0, CODE_LENGTH)]

#lägg till index i white_pegs om computer_color_code[i] är lika med player_color_code[i]
def number_of_white_pegs(computer_color_code, player_color_code):
    white_pegs = [i for i in range(0, CODE_LENGTH) if computer_color_code[i] == player_color_code[i]]
    return len(white_pegs)

#lägg till index i red_pegs om computer_color_code färgen finns i player_color_code
def number_of_red_pegs(computer_color_code, player_color_code):
    red_pegs = [i for i in range(0, CODE_LENGTH) if computer_color_code[i] in player_color_code]
    return len(red_pegs)

if CHEATS: print(f"The computer chose: {computer_color_code}")



while STANDINGS == "Loser" and current_loop <= PLAYER_GUESSES:
    player_color_code = master_mind_GUI.make_guess(current_loop, my_game_window)

    correct_place = number_of_white_pegs(computer_color_code, player_color_code)
    wrong_place = number_of_red_pegs(computer_color_code, player_color_code) - correct_place
    master_mind_GUI.peg_feedback(current_loop, correct_place, wrong_place, my_game_window)

    print(correct_place, CODE_LENGTH)
    if correct_place == CODE_LENGTH: STANDINGS = "Winner"
    current_loop += 1

master_mind_GUI.gameover_screen(current_loop, STANDINGS)
