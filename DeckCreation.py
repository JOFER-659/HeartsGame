#Import libraries
import random

#Create class 'Card'
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        face_cards = {
            11: 'J',
            12: 'Q',
            13: 'K',
            14: 'A',
        }
        value_str = face_cards.get(self.value, self.value)
        return f"{value_str} of {self.suit}"

#Define generate deck function
def generate_deck():
    values = list(range(2, 15))
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    face_cards = {
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A',
    }
    deck = []
    for suit in suits:
        for value in values:
            card_value = face_cards.get(value, value)
            deck.append(Card(suit, card_value))
            random.shuffle(deck)
    return deck
