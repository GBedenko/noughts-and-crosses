"""Class to represent a game of Noughts and Crosses"""

from random import choice
from tkinter import messagebox

from noughts_and_crosses.ai import (computer_block_move, computer_first_move,
                                    computer_second_move, computer_win_move)
from noughts_and_crosses.move import Move
from noughts_and_crosses.player import ComputerPlayer, HumanPlayer
from noughts_and_crosses.ui import (draw_cross, draw_nought, draw_winning_line,
                                    setup_ui, text_input_box, turn_input_box)
from noughts_and_crosses.winning_states import WinningStates


class Game():
	"""TODO
	"""


	def __init__(self):
		"""TODO
		"""

		# Grid squares: -1 = ignored, 0 = empty, X = cross, O = nought
		self.grid = [-1,
					 0, 0, 0,
					 0, 0, 0,
					 0, 0, 0]

		self.game_status = ("incomplete", None)

		self.CROSSES_SYMBOL = "X"
		self.NOUGHTS_SYMBOL = "O"


	def select_game_mode(self):
		"""TODO
		"""

		# Ask user for single player or multiplayer game
		selected_mode = messagebox.askquestion(title="Select Game Mode", message="Do you want to play a multiplayer game?"
																		+ "\n"
																		+ "\nSelect 'Yes' for a multiplayer game,"
																		+" if not select 'No' for a game versus the computer")
		
		# Depending on user's choice, return correct subclass of Game
		return SinglePlayerGame() if selected_mode == "no" else MultiplayerGame()


	def update_game_status(self):

		# Check all winning scenarios for a crosses win
		if self.grid[1]=="X" and self.grid[4]=="X" and self.grid[7]=="X":
			self.game_status = ("crosses_win", WinningStates.TOP_LEFT_TO_BOTTOM_LEFT)
		elif self.grid[2]=="X" and self.grid[5]=="X" and self.grid[8]=="X":
			self.game_status = ("crosses_win", WinningStates.TOP_MIDDLE_TO_BOTTOM_MIDDLE)
		elif self.grid[3]=="X" and self.grid[6]=="X" and self.grid[9]=="X":
			self.game_status = ("crosses_win", WinningStates.TOP_RIGHT_TO_BOTTOM_RIGHT)
		elif self.grid[1]=="X" and self.grid[2]=="X" and self.grid[3]=="X":
			self.game_status = ("crosses_win", WinningStates.TOP_LEFT_TO_TOP_RIGHT)
		elif self.grid[4]=="X" and self.grid[5]=="X" and self.grid[6]=="X":
			self.game_status = ("crosses_win", WinningStates.MIDDLE_LEFT_TO_MIDDLE_RIGHT)
		elif self.grid[7]=="X" and self.grid[8]=="X" and self.grid[9]=="X":
			self.game_status = ("crosses_win", WinningStates.BOTTOM_LEFT_TO_BOTTOM_RIGHT)
		elif self.grid[1]=="X" and self.grid[5]=="X" and self.grid[9]=="X":
			self.game_status = ("crosses_win", WinningStates.TOP_LEFT_TO_BOTTOM_RIGHT)
		elif self.grid[3]=="X" and self.grid[5]=="X" and self.grid[7]=="X":
			self.game_status = ("crosses_win", WinningStates.TOP_RIGHT_TO_BOTTOM_LEFT)

		# Check all winning scenarios for a noughts win
		elif self.grid[1]=="O" and self.grid[4]=="O" and self.grid[7]=="O":
			self.game_status = ("noughts_wins", WinningStates.TOP_LEFT_TO_BOTTOM_LEFT)
		elif (self.grid[2]=="O" and self.grid[5]=="O" and self.grid[8]=="O"):
			self.game_status = ("noughts_wins", WinningStates.TOP_MIDDLE_TO_BOTTOM_MIDDLE)
		elif (self.grid[3]=="O" and self.grid[6]=="O" and self.grid[9]=="O"):
			self.game_status = ("noughts_wins", WinningStates.TOP_RIGHT_TO_BOTTOM_RIGHT)
		elif (self.grid[1]=="O" and self.grid[2]=="O" and self.grid[3]=="O"):
			self.game_status = ("noughts_wins", WinningStates.TOP_LEFT_TO_TOP_RIGHT)
		elif (self.grid[4]=="O" and self.grid[5]=="O" and self.grid[6]=="O"):
			self.game_status = ("noughts_wins", WinningStates.MIDDLE_LEFT_TO_MIDDLE_RIGHT)
		elif (self.grid[7]=="O" and self.grid[8]=="O" and self.grid[9]=="O"):
			self.game_status = ("noughts_wins", WinningStates.BOTTOM_LEFT_TO_BOTTOM_RIGHT)
		elif (self.grid[1]=="O" and self.grid[5]=="O" and self.grid[9]=="O"):
			self.game_status = ("noughts_wins", WinningStates.TOP_LEFT_TO_BOTTOM_RIGHT)
		elif (self.grid[3]=="O" and self.grid[5]=="O" and self.grid[7]=="O"):
			self.game_status = ("noughts_wins", WinningStates.TOP_RIGHT_TO_BOTTOM_LEFT)
			
		# Check for a draw
		elif 0 not in self.grid:
			self.game_status = ("draw", None)

		# If none of the previous scenarios are true, game must still be incomplete            
		else:
			self.game_status = ("incomplete", None)


	def update_grid(self, move):
		"""TODO
		"""

		# Update grid with new move, update game status to check if game is complete
		self.grid[move.grid_position] = move.symbol
		self.update_game_status()

		# Update ui with the new move
		if move.symbol == "X":
			draw_cross(move.grid_position)
		elif move.symbol == "O":
			draw_nought(move.grid_position)


	def end_game(self):
		"""TODO
		"""

		# Draw line if game was won, does nothing if game is a draw
		draw_winning_line(self.game_status[1])

		# Display message to user with result of the game
		if(self.game_status[0]=="crosses_win"):        
			messagebox.showinfo("Game Finished", "Crosses Wins!")
		elif(self.game_status[0]=="noughts_win"):
			messagebox.showinfo("Game Finished", "Noughts Wins!")			
		elif(self.game_status[0]=="draw"):
			messagebox.showinfo("Game Finished", "It's a Draw!")

		# Ask user if they want to play again
		play_again = messagebox.askquestion("Game Finished", "Play Again?")

		# If user wants to play a new game, restarts ui and creates new game instance
		if (play_again=="yes"):					
			setup_ui()		
			new_game = Game().select_game_mode()
			new_game.start()


	def player_turn(self, player):
		"""TODO
		"""

		# If it is a human player's turn
		if isinstance(player, HumanPlayer):

			# Move is taken from user input
			chosen_move = turn_input_box(player.name)
		
		# If it is the computer's turn
		elif isinstance(player, ComputerPlayer):
			
			# Create a list of all the possible moves the computer can choose
			possible_moves = []
			for i in range(1,10):
				if (self.grid[i] != "X") and (self.grid[i] != "O"):
					possible_moves.append(i)

			# Random move, just selects one of the available grid positions
			if player.difficulty == 1:
				chosen_move = choice(possible_moves)

			# Hard difficulty, computer's first move implemented, most of computer's second moves are implemented
			elif player.difficulty == 2:
				
				# If computer's first move, retrieve the implemented move
				if len(possible_moves) == 8:
					possible_moves = computer_first_move(self.grid)

				# If computer's second move and current scenario has implemented moves
				elif len(possible_moves)==6 and len(computer_second_move(self.grid)) >= 1:
					possible_moves = computer_second_move(self.grid)

				# If there is a move for the computer to win, choose this move
				if computer_win_move(self.grid) != None:
					chosen_move = computer_win_move(self.grid)
				
				# If computer can't win but must block human from winning, choose this move
				elif computer_block_move(self.grid) != None:
					chosen_move = computer_block_move(self.grid)

				# If computer can't win or block, choose from the possible moves list
				else:
					chosen_move = choice(possible_moves)

			# Impossible difficulty, all computer's moves implemented, player can draw at best
			elif player.difficulty == 3:

				# TODO Hard implemented moves for all cases, hard difficulty plus third move implemented
				chosen_move = choice(possible_moves)
		
		# Check that this move is valid, and hasn't already been made
		if (self.grid[chosen_move] == "X") or (self.grid[chosen_move] == "O"):
			
			# Prompt user to pick a different grid position
			messagebox.showinfo("Invalid Move", "This grid square has already been used please select another")
			self.player_turn(player)

		# If move is valid, update the grid with chosen move and corresponding symbol
		else:
			self.update_grid(Move(int(chosen_move), player.symbol))


class SinglePlayerGame(Game):
	"""TODO
	"""


	def start(self):
		"""TODO
		"""

		# Create human player based on user input
		player_name = text_input_box("Player Name", "Enter your name:")
		player_symbol = text_input_box("Player Symbol", "Choose your symbol. X or O:")
		human_player = HumanPlayer(player_name, player_symbol)

		# Choose difficulty of computer player
		selected_difficulty = int(text_input_box("Select Difficulty", "1. Easy \n2. Hard \n3. Impossible"))

		# Create computer player instance based on chosen difficulty
		computer_symbol = "O" if player_symbol == "X" else "X"
		computer_player = ComputerPlayer("Computer", computer_symbol, selected_difficulty)

		# Human player starts, current_player will alternate after each turn
		# TODO: Ask human user if they want to go first or second
		current_player = human_player

		# While no win or draw, ask current_player for a turn
		while self.game_status[0] == "incomplete":

			# For the current player, they input position for their symbol
			self.player_turn(current_player)
			
			# Update current_player based on who just had their turn
			current_player = computer_player if current_player == human_player else human_player

		# Once out of while loop, game is complete so display outcome
		self.end_game()


class MultiplayerGame(Game):
	"""TODO Multiplayer implementation of two human players
	"""


	def start(self):
		"""TODO Function called to start the game
		"""

		# Create player1 instance based on user input
		player1_name = text_input_box("Player 1 Name", "Player 1, enter your name:")
		player1_symbol = text_input_box("Player 1 Symbol", "Player 1, choose your symbol. X or O:")
		player1 = HumanPlayer(player1_name, player1_symbol)
		
		# Create player2 based on input and remaining symbol
		player2_name = text_input_box("Player 2 Name", "Player 2, enter your name:")
		player2_symbol = "O" if player1_symbol == "X" else "X"
		player2 = HumanPlayer(player2_name, player2_symbol)

		# player1 starts, current_player will alternate after each turn
		current_player = player1

		# While no win or draw, ask current_player for a turn
		while self.game_status[0] == "incomplete":

			# For the current player, they input position for their symbol
			self.player_turn(current_player)
			
			# Update current_player based on who just had their turn
			current_player = player2 if current_player == player1 else player1

		# Once out of while loop, game is complete so display outcome
		self.end_game()
