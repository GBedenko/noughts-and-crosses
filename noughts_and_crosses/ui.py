# Import turtle and tkinter for GUI
import turtle
from tkinter import messagebox
from noughts_and_crosses.winning_states import WinningStates


def display_rules():
	'''Displays the instructions and how to play in a messagebox to the user'''

	messagebox.showinfo("How to Play", "In this game you will take it in turns, either between two human players or between yourself and the computer,"
						+ " to enter a symbol into the grid. "
						+ "\n"
						+ "\nTo do this you need to enter a value between 1 to 9 to represent the 9 grid squares."
						+ "\n"
						+ "\n1 represents the top-left grid square, 2 represents the top-middle square and so on, reading from left to right for each row."
						+ "\n"
						+ "\nThe game is complete when it is won (if there are three of the same symbols in a row), or if it is a draw (the grid is complete"
						+ "\nwithout any winning scenario)"
						+ "\n"
						+ "\nIf you cancel your move the game will save automatically and you can finish the game later.")


def draw_grid():
	'''Draws the three-by-three grid for the game'''

	# Hide turtle so that you can't see the 'turtle' and the lines just appear
	# As the line is drawn there is a weird shape at the end, so this removes this
	turtle.hideturtle()
	
	turtle.pensize(5)
	turtle.shape("circle")
	
	# Set starting position
	turtle.penup()
	turtle.setposition(-80,250)
	turtle.pendown()

	# Draw first line
	turtle.right(90)
	turtle.forward(510)

	# Draw second line
	turtle.penup()
	turtle.setposition(90,250)
	turtle.pendown()
	turtle.forward(510)

	# Draw third line
	turtle.penup()
	turtle.setposition(-250,80)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(510)

	# Draw fourth line
	turtle.penup()
	turtle.setposition(-250,-90)
	turtle.pendown()
	turtle.forward(510)


def draw_cross(grid_position):
	'''Draws a blue cross in the given grid position'''

	positions_coords = {
						1: {"first_line": (-240,240),
							"second_line": (-240,100) },

						2: {"first_line": (-60,240),
							"second_line": (-60,100) },

						3: {"first_line": (100,240),
							"second_line": (100,100) },

						4: {"first_line": (-240,60),
							"second_line": (-240,-80) },

						5: {"first_line": (-60,60),
							"second_line": (-60,-80) },

						6: {"first_line": (100,60),
							"second_line": (100,-80) },

						7: {"first_line": (-250,-110),
							"second_line": (-250,-250) },

						8: {"first_line": (-60,-110),
							"second_line": (-60,-250) },

						9: {"first_line": (110,-110),
							"second_line": (110,-250) }
					}

	turtle.pensize(2)
	turtle.color("blue")

	# Draw 'X' in first box
	turtle.penup()
	turtle.setposition(positions_coords[grid_position]["first_line"])
	turtle.pendown()
	turtle.right(45)
	turtle.forward(200)

	turtle.penup()
	turtle.setposition(positions_coords[grid_position]["second_line"])
	turtle.pendown()
	turtle.left(90)
	turtle.forward(200)
		
	# Reset the angle turtle is facing to the original direction so that it doesn't affect
	# the next shape drawn (this is used in all grid positions)
	turtle.right(45)


def draw_nought(grid_position):
	'''Draws a red nought in the given grid position'''

	positions_coords = {1: (-175,90),
						2: (5,90),
						3: (175,90),
						4: (-175,-80),
						5: (5,-80),
						6: (175,-80),
						7: (-175,-250),
						8: (5,-250),
						9: (175,-250)
					}
	
	turtle.pensize(2)
	turtle.color("red")
	
	turtle.penup()
	turtle.setposition(positions_coords[grid_position])
	turtle.pendown()
	turtle.circle(75)


def draw_winning_line(winning_state):
	'''Draws a green line through the three winning grid positions'''
	# there are 8 possible winning scenarios
	
	turtle.pensize(7)
	turtle.color("green")

	positions_coords = {WinningStates.TOP_LEFT_TO_BOTTOM_LEFT: (-175,250),
						WinningStates.TOP_MIDDLE_TO_BOTTOM_MIDDLE: (5,250),
						WinningStates.TOP_RIGHT_TO_BOTTOM_RIGHT: (175,250),
						WinningStates.TOP_LEFT_TO_TOP_RIGHT: (-250,165),
						WinningStates.MIDDLE_LEFT_TO_MIDDLE_RIGHT: (-250,-5),
						WinningStates.BOTTOM_LEFT_TO_BOTTOM_RIGHT: (-250,-175),
						WinningStates.TOP_LEFT_TO_BOTTOM_RIGHT: (-250,250),
						WinningStates.TOP_RIGHT_TO_BOTTOM_LEFT: (-250,-250),
						}

	# Vertical lines
	if winning_state in [WinningStates.TOP_LEFT_TO_BOTTOM_LEFT, WinningStates.TOP_MIDDLE_TO_BOTTOM_MIDDLE, WinningStates.TOP_RIGHT_TO_BOTTOM_RIGHT]:

		turtle.penup()
		turtle.setposition(positions_coords[winning_state])
		turtle.pendown()
		turtle.right(90)
		turtle.forward(510)
		turtle.left(90)

	# Horizontal lines
	elif winning_state in [WinningStates.TOP_LEFT_TO_TOP_RIGHT, WinningStates.MIDDLE_LEFT_TO_MIDDLE_RIGHT, WinningStates.BOTTOM_LEFT_TO_BOTTOM_RIGHT]:

		turtle.penup()
		turtle.setposition(positions_coords[winning_state])
		turtle.pendown()
		turtle.forward(510)

	# Diagonal line
	elif winning_state == WinningStates.TOP_LEFT_TO_BOTTOM_RIGHT:
		
		turtle.penup()
		turtle.setposition(positions_coords[winning_state])
		turtle.pendown()
		turtle.right(45)
		turtle.forward(710)
		turtle.left(45)

	# Diagonal line
	elif winning_state == WinningStates.TOP_RIGHT_TO_BOTTOM_LEFT:

		turtle.penup()
		turtle.setposition(positions_coords[winning_state])
		turtle.pendown()
		turtle.left(45)
		turtle.forward(700)
		turtle.right(45)

	turtle.hideturtle()


def setup_ui():

	turtle.reset()
	turtle.setup(650,600)
	turtle.title("Noughts and Crosses by Genaro Bedenko")
	draw_grid()

	display_rules()	


def text_input_box(title, message):

	user_input = turtle.textinput(title, message)

	return user_input


def turn_input_box(player_name):

	user_input = int(turtle.numinput(player_name + "'s turn", "Enter your move:", minval = 1, maxval = 9))

	return user_input
