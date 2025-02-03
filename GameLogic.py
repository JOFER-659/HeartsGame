from DeckCreation import generate_deck
from PlayerCreation import players
from DealCards import Deal_Deck
import random

class Game:
    def __init__(self):
        # Import Players
        self.players = players

        # Track Score
        self.scores = {player.name: 0 for player in self.players}

        # Stores current trick
        self.trick = []

        # Track won cards per player for scoring
        self.won_cards = {player: [] for player in self.players}

        # Track if hearts have been broken
        self.hearts_broken = False

        # Track if it's the first trick
        self.first_trick = True

    def find_two_of_clubs(self):
        """Find the player holding the 2 of Clubs and return them."""
        for player in self.players:
            for card in player.hand:
                if card.suit == "Clubs" and card.value == 2:
                    return player
        return None

    def play_first_trick(self):
        """Ensure the first trick starts with the 2 of Clubs."""
        first_player = self.find_two_of_clubs()

        if first_player:
            two_of_clubs = next(card for card in first_player.hand if card.suit == "Clubs" and card.value == 2)
            first_player.hand.remove(two_of_clubs)
            self.trick.append((first_player, two_of_clubs))
            print(f"{first_player.name} starts with {two_of_clubs}")

            self.first_trick = False  # After the first trick, this will be set to False
            return first_player
        else:
            raise ValueError("No player has the 2 of Clubs! Something went wrong.")

    def play_card(self, player):
        """Player must follow suit if possible and return the played card."""
        lead_suit = self.trick[0][1].suit if self.trick else None

        # If no hearts have been broken and the player tries to play a heart first, reject it
        if not self.hearts_broken and any(card.suit == "Hearts" for card in player.hand):
            if lead_suit is None:  # First card of the trick
                raise ValueError(f"{player.name} cannot play a Heart as the first card until hearts are broken.")

        # Check for Queen of Spades being played in the first trick
        if self.first_trick:
            for card in player.hand:
                if card.suit == "Spades" and card.value == 12:  # Queen of Spades
                    raise ValueError(f"{player.name} cannot play the Queen of Spades on the first trick!")

        # Determine valid cards
        valid_cards = [card for card in player.hand if card.suit == lead_suit]

        if valid_cards:
            chosen_card = valid_cards[0]  # AI picks first valid card
        else:
            chosen_card = player.hand[0]  # AI picks first card if no valid plays

        player.hand.remove(chosen_card)
        self.trick.append((player, chosen_card))
        print(f"{player.name} plays {chosen_card}")

        # Check if hearts are broken
        if chosen_card.suit == "Hearts" and lead_suit != "Hearts":
            self.hearts_broken = True
            print("Hearts have been broken!")

        return chosen_card  # Return the played card for tracking

    def determine_trick_winner(self):
        """Finds the highest card of the lead suit and determines the trick winner."""
        lead_suit = self.trick[0][1].suit
        valid_cards = [(player, card) for player, card in self.trick if card.suit == lead_suit]
        winner = max(valid_cards, key=lambda x: x[1].value)[0]  # Player with highest lead suit card wins
        print(f"{winner.name} wins the trick!")

        # Store won cards for scoring later
        self.won_cards[winner].extend([card for _, card in self.trick])

        return winner

    def play_round(self, starting_player):
        """Plays all tricks in the round."""
        current_player = starting_player

        while any(player.hand for player in self.players):
            self.trick = []  # Reset the trick for each round

            for _ in range(len(self.players)):
                self.play_card(current_player)
                current_player = self.next_player(current_player)

            winner = self.determine_trick_winner()
            current_player = winner  # Winner leads the next trick

    def calculate_scores(self):
        """Calculate scores (each heart = 1 point, Queen of Spades = 13)."""
        for player, won_cards in self.won_cards.items():
            self.scores[player.name] += sum(1 for card in won_cards if card.suit == "Hearts")
            self.scores[player.name] += sum(13 for card in won_cards if card.suit == "Spades" and card.value == 12)

        print("Final Scores:", self.scores)

    def next_player(self, current_player):
        """Finds the next player in the turn order."""
        index = self.players.index(current_player)
        return self.players[(index + 1) % len(self.players)]

    def play_game(self):
        """Run the full game."""
        Deal_Deck(self.players)

        # First Trick (2♣ must be played)
        first_player = self.play_first_trick()

        # Play remaining tricks starting from first_player
        self.play_round(first_player)

        # Score Calculation
        self.calculate_scores()
        print("Game Over!")