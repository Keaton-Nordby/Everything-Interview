import random


# card class
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        
    def __repr__(self):
        return f"{self.val} of {self.suit}"



# deck class
class Deck:
    def __init__(self):
        self.deck = []
        self.suit = ["diamonds", "hearts", "clubs", "spades"]
        self.val = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        
        for suit in self.suit:
            for val in self.val:
                self.deck.append(Card(suit, val))
                
    def print_deck(self):
        for card in self.deck:
            print(card)
                
                
    # shuffle
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
        
    # draw card
    def draw_card(self):
        return self.deck.pop()
    

# example usage
d = Deck()

d.print_deck()
print("---- shuffled ----")
d.shuffle_deck()
d.print_deck()

print("---- draw ----")
print(d.draw_card())
    
    