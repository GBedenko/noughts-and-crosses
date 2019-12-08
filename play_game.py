from noughts_and_crosses.game import Game
from noughts_and_crosses.ui import display_rules, draw_grid, draw_cross, draw_nought, draw_winning_line, setup_ui
from noughts_and_crosses.winning_states import WinningStates

from tkinter import messagebox


if __name__ == "__main__":
		
	setup_ui()
	new_game = Game().select_game_mode()
	new_game.start()
