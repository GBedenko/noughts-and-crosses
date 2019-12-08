class Player():
    """Player object consists of two attributes: a name and their symbol"""

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class HumanPlayer(Player):
    """HumanPlayer is an instance of a Player, no new attributes or overrides"""
    pass


class ComputerPlayer(Player):
    """ComputerPlayer is and instance of Player, adds extra attribute of difficulty"""

    def __init__(self, name, symbol, difficulty):        
        Player.__init__(self, name, symbol)        
        self.difficulty = difficulty
