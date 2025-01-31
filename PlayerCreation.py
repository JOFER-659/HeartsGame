#Create names of players
player_names = ['You', 'Player 2', 'Player 3', 'Player 4']

#Define player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"{self.name}'s hand: {', '.join(str(card) for card in self.hand)}"

players = [Player(name) for name in player_names]

