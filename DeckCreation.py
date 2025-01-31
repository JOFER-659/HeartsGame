#Import libraries
import random

#Define values and suits
values = list(range(2,15))
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
face_cards = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
}

#Create class 'Card'
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        value_str = face_cards.get(self.value, self.value)
        return f"{value_str} of {self.suit}"

#Define generate deck function
def generate_deck(values, suits):
    deck = []
    for suit in suits:
        for value in values:
            deck.append(Card(suit, value))
    return deck

#Generate Deck and shuffle
deck = generate_deck(values, suits)
random.shuffle(deck)

