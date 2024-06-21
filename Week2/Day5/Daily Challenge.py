import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.deck_cards()

    def deck_cards(self):
        self.cards = [(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Example usage:
deck = Deck()
deck.shuffle()
print('Shuffled deck:')
for suit, value in deck.cards:
    print(f"{value} {suit}")
print("\nDealing a card:")
dealt_card = deck.deal()
print("Dealt Card:", dealt_card[1], dealt_card[0])
print("\nNumber of remaining cards in deck:", len(deck.cards))
