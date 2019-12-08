from noughts_and_crosses.game import Game
from noughts_and_crosses.ui import display_rules, draw_grid, draw_cross, draw_nought, draw_winning_line, setup_ui
from noughts_and_crosses.winning_states import WinningStates

from tkinter import messagebox


if __name__ == "__main__":
		
	setup_ui()
	new_game = Game().select_game_mode()
	new_game.start()
		
	# playSavedGame = messagebox.askquestion(title="Play Previous Game?", message="Do you want to play a previously saved game?")

	# if(playSavedGame=="yes"):
	# 	try:
	# 		loadGame(gridSquares)

	# 	# If the user clicks yes to play a saved game but their isn't one saved in the directory. Display a message to tell them
	# 	# this and move on to starting a new game
	# 	except FileNotFoundError:
	# 		messagebox.showinfo(title="No Saved Game Available", message="There isn't a currently saved game available to play")
	# 		gameModeSelection()
	# else:
	# 	gameModeSelection()
