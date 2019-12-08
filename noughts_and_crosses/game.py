"""Class to represent a game of Noughts and Crosses
"""
from noughts_and_crosses.winning_states import WinningStates
from noughts_and_crosses.move import Move
from noughts_and_crosses.player import HumanPlayer, ComputerPlayer
from noughts_and_crosses.ai import computer_first_move, computer_second_move, computer_win_move, computer_block_move
from noughts_and_crosses.ui import text_input_box, turn_input_box, draw_cross, draw_nought, draw_winning_line, setup_ui

from random import choice
from pickle import dump
from tkinter import messagebox

class Game():

	def __init__(self):

		self.game_status = ("incomplete", None)
		self.multiplayer = False

		# Grid squares: -1 = ignored, 0 = empty, X = cross, O = nought
		self.grid = [-1,
					 0, 0, 0,
					 0, 0, 0,
					 0, 0, 0]

		self.CROSSES_SYMBOL = "X"
		self.NOUGHTS_SYMBOL = "O"

		self.clear_board()


	def select_game_mode(self):

		selected_mode = messagebox.askquestion(title="Select Game Mode", message="Do you want to play a multiplayer game?"
																		+ "\n"
																		+ "\nSelect 'Yes' for a multiplayer game,"
																		+" if not select 'No' for a game versus the computer")
		
		return SinglePlayerGame() if selected_mode == "no" else MultiplayerGame()


	def clear_board(self):
		# Could be used to scrap game if player knows they can't win
		# Essentially starts the game again

		self.grid = [-1,
					 0, 0, 0,
					 0, 0, 0,
					 0, 0, 0]


	def save(self):
		# TODO Use this for a save game option

		# Open the file in write data mode
		f = open("saved_game.pickle", "wb")

		# Save the gridSquares list to the file
		dump(self.grid, f)

		# Save the game mode variable to the file
		dump(self.multiplayer, f)

		# Close the file once done with it
		f.close()


	def load(self):
		# TODO: Load game functionality
		pass


	def update_game_status(self):

		# Check for crosses win
		if self.grid[1]=="X" and self.grid[4]=="X" and self.grid[7]=="X":
			# drawWinningLine(1)
			self.game_status = ("crosses_win", WinningStates.TOP_LEFT_TO_BOTTOM_LEFT)

		elif self.grid[2]=="X" and self.grid[5]=="X" and self.grid[8]=="X":
			# drawWinningLine(2)
			self.game_status = ("crosses_win", WinningStates.TOP_MIDDLE_TO_BOTTOM_MIDDLE)

		elif self.grid[3]=="X" and self.grid[6]=="X" and self.grid[9]=="X":
			# drawWinningLine(3)
			self.game_status = ("crosses_win", WinningStates.TOP_RIGHT_TO_BOTTOM_RIGHT)

		elif self.grid[1]=="X" and self.grid[2]=="X" and self.grid[3]=="X":
			# drawWinningLine(4)
			self.game_status = ("crosses_win", WinningStates.TOP_LEFT_TO_TOP_RIGHT)

		elif self.grid[4]=="X" and self.grid[5]=="X" and self.grid[6]=="X":
			# drawWinningLine(5)
			self.game_status = ("crosses_win", WinningStates.MIDDLE_LEFT_TO_MIDDLE_RIGHT)

		elif self.grid[7]=="X" and self.grid[8]=="X" and self.grid[9]=="X":
			# drawWinningLine(6)
			self.game_status = ("crosses_win", WinningStates.BOTTOM_LEFT_TO_BOTTOM_RIGHT)

		elif self.grid[1]=="X" and self.grid[5]=="X" and self.grid[9]=="X":
			# drawWinningLine(7)
			self.game_status = ("crosses_win", WinningStates.TOP_LEFT_TO_BOTTOM_RIGHT)

		elif self.grid[3]=="X" and self.grid[5]=="X" and self.grid[7]=="X":
			# drawWinningLine(8)
			self.game_status = ("crosses_win", WinningStates.TOP_RIGHT_TO_BOTTOM_LEFT)

		# Check for noughts win
		elif self.grid[1]=="O" and self.grid[4]=="O" and self.grid[7]=="O":
			# drawWinningLine(1)
			self.game_status = ("noughts_wins", WinningStates.TOP_LEFT_TO_BOTTOM_LEFT)

		elif (self.grid[2]=="O" and self.grid[5]=="O" and self.grid[8]=="O"):
			# drawWinningLine(2)
			self.game_status = ("noughts_wins", WinningStates.TOP_MIDDLE_TO_BOTTOM_MIDDLE)
			
		elif (self.grid[3]=="O" and self.grid[6]=="O" and self.grid[9]=="O"):
			# drawWinningLine(3)
			self.game_status = ("noughts_wins", WinningStates.TOP_RIGHT_TO_BOTTOM_RIGHT)
			
		elif (self.grid[1]=="O" and self.grid[2]=="O" and self.grid[3]=="O"):
			# drawWinningLine(4)
			self.game_status = ("noughts_wins", WinningStates.TOP_LEFT_TO_TOP_RIGHT)
			
		elif (self.grid[4]=="O" and self.grid[5]=="O" and self.grid[6]=="O"):
			# drawWinningLine(5)
			self.game_status = ("noughts_wins", WinningStates.MIDDLE_LEFT_TO_MIDDLE_RIGHT)
			
		elif (self.grid[7]=="O" and self.grid[8]=="O" and self.grid[9]=="O"):
			# drawWinningLine(6)
			self.game_status = ("noughts_wins", WinningStates.BOTTOM_LEFT_TO_BOTTOM_RIGHT)
			
		elif (self.grid[1]=="O" and self.grid[5]=="O" and self.grid[9]=="O"):
			# drawWinningLine(7)
			self.game_status = ("noughts_wins", WinningStates.TOP_LEFT_TO_BOTTOM_RIGHT)
			
		elif (self.grid[3]=="O" and self.grid[5]=="O" and self.grid[7]=="O"):
			# drawWinningLine(8)
			self.game_status = ("noughts_wins", WinningStates.TOP_RIGHT_TO_BOTTOM_LEFT)
			
		# Check for a draw
		elif 0 not in self.grid:
			self.game_status = ("draw", None)

		# After going through all checks, game must still be incomplete            
		else:
			self.game_status = ("incomplete", None)


	def update_grid(self, move):

		self.grid[move.grid_position] = move.symbol
		self.update_game_status()

		if move.symbol == "X":
			draw_cross(move.grid_position)
		elif move.symbol == "O":
			draw_nought(move.grid_position)
		else:
			raise ValueError("Incorrect symbol used")


	def end_game(self):

		draw_winning_line(self.game_status[1])

		if(self.game_status[0]=="crosses_win"):        
			messagebox.showinfo("Game Finished", "Crosses Wins!")
		elif(self.game_status[0]=="noughts_win"):
			messagebox.showinfo("Game Finished", "Noughts Wins!")			
		elif(self.game_status[0]=="draw"):
			messagebox.showinfo("Game Finished", "It's a Draw!")

		play_again = messagebox.askquestion("Game Finished", "Play Again?")

		if (play_again=="yes"):
					
			setup_ui()		
			new_game = Game().select_game_mode()
			new_game.start()


	def player_turn(self, player):

		if isinstance(player, HumanPlayer):

			chosen_move = turn_input_box(player.name)
		
		elif isinstance(player, ComputerPlayer):
			
			# List for possible moves/ empty squares
			possible_moves = []

			# If it doesn't contain a 1 or 2 then it is empty and can be considered a possible move
			for i in range(1,10):
				if (self.grid[i] != "X") and (self.grid[i] != "O"):
					possible_moves.append(i)

			if player.difficulty == 1:
				# Random move
				chosen_move = choice(possible_moves)

			elif player.difficulty == 2:
				# Hard implemented moves, can win with luck
				
				# For each possible turn the human made, decide the best possible moves to go for the first turn
				# that will give the computer the most possible winning scenarios at this stage of the game
				if len(possible_moves)==8:

					# All first moves are implemented
					possible_moves = computer_first_move(self.grid)

				elif len(possible_moves)==6:
					
					# If there are hard implemented moves for second move, use them
					if len(computer_second_move(self.grid)) >= 1:
						possible_moves = computer_second_move(self.grid)

				if computer_win_move(self.grid) != None:
					chosen_move = computer_win_move(self.grid)
				
				elif computer_block_move(self.grid) != None:
					chosen_move = computer_block_move(self.grid)

				else:
					chosen_move = choice(possible_moves)

			elif player.difficulty == 3:
				# TODO Hard implemented moves for all cases, player can draw at best
				chosen_move = choice(possible_moves)
			
		else:
			raise TypeError("Incorrect player type created")
		
		# Check that this move is valid, and hasn't already been made
		if (self.grid[chosen_move] == "X") or (self.grid[chosen_move] == "O"):
			
			messagebox.showinfo("Invalid Move", "This grid square has already been used please select another")
			self.player_turn(player)

		else:
			self.update_grid(Move(int(chosen_move), player.symbol))



class SinglePlayerGame(Game):


	def start(self):

		# Create human_player instance based on user input
		player_name = text_input_box("Player Name", "Enter your name:")
		player_symbol = text_input_box("Player Symbol", "Choose your symbol. X or O:")
		human_player = HumanPlayer(player_name, player_symbol)

		# Choose difficulty of computer player
		selected_difficulty = int(text_input_box("Select Difficulty", "1. Easy \n2. Hard \n3. Impossible:"))

		# Create computer_player instance based on chosen difficulty
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
	"""Multiplayer implementation of two human players
	"""

	def start(self):
		"""Function called to start the game
		"""

		self.multiplayer = True

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

