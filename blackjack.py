"""Projekt 4: Black Jack
Spelet spelas med en vanlig kortlek som blandas innan varje runda.
Varje spelare får två kort i början av spelet. Datorn visar bara upp ett av sina kort.
Spelaren kan välja att ta fler kort (hit) eller stanna på sina nuvarande kort (stand).
Spelaren kan fortsätta att ta kort tills hen når 21 poäng eller över.
Om spelaren går över 21 poäng förlorar hen direkt.
När spelaren stannar, spelar datorn sin tur. 
Datorn måste ta kort så länge summan av korten är mindre än 17 poäng 
    och stanna när datorns kortsumma är 17 poäng eller mer.
Om datorn går över 21 poäng vinner spelaren oavsett vilka kort spelaren har.
Om varken spelaren eller datorn går över 21 poäng så vinner den som har högst kortsumma.
 """
from random import shuffle

class Card:
    suits = {'c': '♣','d': '♦','h': '♥','s': '♠'}
    values = {
        "2": 2, "3": 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {Card.suits[self.suit]}"

    def value(self):
        return Card.values[str(self.rank)]

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in Card.suits.keys():
            for c in range(2,11):
                self.cards.append(Card(str(c),s))
            for f in ["Jack","Queen","King","Ace"]:
                self.cards.append(Card(f,s))
        shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() 

    def show(self):
        for card in self.cards:
            print(card)

class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.draw_card())
    
    def showhand(self, show_all=False):
        if self.name == "Dealer" and not show_all:
            print("Dealer's hidden card: ")
            print(self.hand[0])
        else:
            for card in self.hand:
                print(card)
    def total(self):
        total = sum(card.value() for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == 'Ace')
        #for card in self.hand:
        #    total += card.value()
        #    if card.rank == "Ace":
        #        aces += 1
        while total >21 and aces:
            total -= 10
            aces -= 1
        return total   

def dealer_turn(dealer, deck):
        print("Dealer's turn: ")
        dealer.showhand(show_all=True)
        while dealer.total() < 17:
            print(f"Dealer's hand: {dealer.total()}. Dealer draws a...")
            dealer.draw(deck)
            dealer.showhand(show_all=True)
        print(f"Dealer's final hand is {dealer.total()}")

def main():

    adeck = Deck()
    tomas = Player("Tomas")
    dealer = Player("Dealer")

    dealer.draw(adeck)
    dealer.draw(adeck)
    tomas.draw(adeck)
    tomas.draw(adeck)

    print("The dealer draws a hidden card and a ...")
    dealer.showhand(show_all = False)

    print("You draw ...")
    tomas.showhand()
    print (f"Your hand is {tomas.total()}")

    while True:
        if tomas.total() > 21:
            print("You're bust!")
            return

        play = input("Hit(h) or Stand(s)?: ")
        if play == "h":
            tomas.draw(adeck)
            print("You draw ...")
            tomas.showhand()
            print (f"Your hand is {tomas.total()}")
        elif play == "s":
            break
 
    dealer_turn(dealer, adeck)
    
    tomas_score = tomas.total()
    daeler_score = dealer.total()
        
    if dealer.total() > 21:
        print (f"Dealer's hand is {dealer.total()}, you win!")
        return
    if dealer.total() < tomas.total():
        print (f"Your hand is {tomas.total()} and Dealer's hand is {dealer.total()}, you win!")
    if dealer.total() > tomas.total():
        print (f"Your hand is {tomas.total()} and Dealer's hand is {dealer.total()}, you lose!")
    if dealer.total() == tomas.total():
        print(f"It's a draw!")
        
if __name__ == "__main__":
    main()