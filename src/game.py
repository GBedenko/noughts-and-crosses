"""Class to represent a game of Noughts and Crosses
"""

from winning_states import WinningStates
from move import Move
from player import Player

class Game():

	def __init__(self, difficulty):

		self.difficulty = difficulty

		self.game_status = ("incomplete", None)

		# Grid squares: -1 = ignored, 0 = empty, X = cross, O = nought
		self.grid = [-1,
					 0, 0, 0,
					 0, 0, 0,
					 0, 0, 0]
							 

	def clear_board(self):
		# Could be used to scrap game if player knows they can't win
		# Essentially starts the game again

		self.grid = [-1,
					 0, 0, 0,
					 0, 0, 0,
					 0, 0, 0]

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


	def display(self):
		
		print("\n")
		
		for i in range(1, 10, 3):
			
			print(self.grid[i], self.grid[i+1], self.grid[i+2])

	
	def player_turn(self, player):

		player_move = input(player.name + ", enter grid position: ")

		self.update_grid(Move(int(player_move), player.symbol))

		self.display()
		


class SinglePlayerGame(Game):

	def computer_turn(self):

		if self.difficulty == "easy":
			# Random moves
			pass
		elif self.difficulty == "hard":
			# Hard implemented moves, except possible lucky ways
			pass
		elif self.difficulty == "impossible":
			# Hard implemented moves for all cases, player can draw at best
			pass

		self.display()


	def start(self):

		player_name = input("Enter your name:")

		player_symbol = input("Choose your symbol. X or O:")

		new_player = Player(player_name, player_symbol)
		
		while self.game_status[0] == "incomplete":

			self.player_turn(new_player)
			self.computer_turn()


class MultiplayerGame(Game):

	def start(self):

		player1_name = input("Player 1, enter your name:")

		player1_symbol = input("Player 1, choose your symbol. X or O:")

		player1 = Player(player1_name, player1_symbol)
		
		player2_name = input("Player 2, enter your name:")

		player2_symbol = "O" if player1_symbol == "X" else "X"

		player2 = Player(player2_name, player2_symbol)

		while self.game_status[0] == "incomplete":

			self.player_turn(player1)
			
			if(self.game_status[0] != "incomplete"):
				break

			self.player_turn(player2)

		print("Game Result: " + self.game_status[0])


if __name__ == "__main__":
		
	print("\n Welcome to Noughts and Crosses!")
	selected_mode = int(input("\n --Select Game Mode--\n 1. Single Player \n 2. Multiplayer \n \n Enter 1 or 2: "))

	if selected_mode == 1:
		
		selected_difficulty = int(input("\n --Select Difficulty--\n 1. Easy \n 2. Hard \n 3. Impossible \n \n Enter 1 or 2 or 3: "))
		
		new_game = SinglePlayerGame(selected_difficulty)
		new_game.start()

	elif selected_mode == 2:

		new_game = MultiplayerGame(None)
		new_game.start()
