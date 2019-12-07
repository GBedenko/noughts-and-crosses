from noughts_and_crosses.game import SinglePlayerGame, MultiplayerGame
from noughts_and_crosses.ui import display_rules, draw_grid, draw_cross, draw_nought, draw_winning_line
from noughts_and_crosses.winning_states import WinningStates

if __name__ == "__main__":
		
	print("Welcome to Noughts and Crosses! \n")

	draw_grid()
	display_rules()

	for i in WinningStates:
		draw_winning_line(i)

	selected_mode = int(input("--Select Game Mode--\n1. Single Player \n2. Multiplayer \n \nEnter 1 or 2: "))

	if selected_mode == 1:
		
		new_game = SinglePlayerGame()
		new_game.start()

	elif selected_mode == 2:

		new_game = MultiplayerGame()
		new_game.start()
