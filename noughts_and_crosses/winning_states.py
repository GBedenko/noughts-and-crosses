from enum import Enum

class WinningStates(Enum):
	"""Enumerator to represent the 8 possible ways of winning a game"""

	TOP_LEFT_TO_BOTTOM_LEFT = 1
	TOP_MIDDLE_TO_BOTTOM_MIDDLE = 2
	TOP_RIGHT_TO_BOTTOM_RIGHT = 3
	TOP_LEFT_TO_TOP_RIGHT = 4
	MIDDLE_LEFT_TO_MIDDLE_RIGHT = 5
	BOTTOM_LEFT_TO_BOTTOM_RIGHT = 6
	TOP_LEFT_TO_BOTTOM_RIGHT = 7
	TOP_RIGHT_TO_BOTTOM_LEFT = 8
