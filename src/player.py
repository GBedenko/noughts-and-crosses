class Player():

    def __init__(self, name, symbol):

        self.name = name
        self.symbol = symbol


class HumanPlayer(Player):
    pass


class ComputerPlayer(Player):

    def __init__(self, name, symbol, difficulty):
        
        Player.__init__(self, name, symbol)
        
        self.difficulty = difficulty
