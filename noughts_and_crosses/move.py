class Move():
	"""Move consists of two parts: grid position and symbol"""

	def __init__(self, grid_position, symbol):
		self.grid_position = grid_position
		self.symbol = symbol
		