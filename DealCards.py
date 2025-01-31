#load libraries
from DeckCreation import generate_deck
from PlayerCreation import players, player_names
#Create function to deal cards
def Deal_Deck():
    deck = generate_deck()
    num_cards_per_player = len(deck) // len(players)

    for i, player in enumerate(players):
        hand = deck[i * num_cards_per_player:(i + 1) * num_cards_per_player]
        player.hand = hand


    for player in players:
        print(player)

Deal_Deck()
