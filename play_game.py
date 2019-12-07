from noughts_and_crosses.game import SinglePlayerGame, MultiplayerGame

if __name__ == "__main__":
		
	print("Welcome to Noughts and Crosses! \n")

	selected_mode = int(input("--Select Game Mode--\n1. Single Player \n2. Multiplayer \n \nEnter 1 or 2: "))

	if selected_mode == 1:
		
		new_game = SinglePlayerGame()
		new_game.start()

	elif selected_mode == 2:

		new_game = MultiplayerGame()
		new_game.start()
