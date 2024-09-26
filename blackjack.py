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

def main():

    class Card:
        suits = {'c': '♣','d': '♦','h': '♥','s': '♠'}
        values = {"2": 2, "3": 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                  'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

        def show(self):
            print (f"{self.rank} of {Card.suits[self.suit]}")

        def value(self):
            return Card.values[str(self.rank)]

    class Deck:
        def __init__(self):
            self.cards = []
            self.build()

        def build(self):
            for s in ["c","d","h","s"]:
                for c in range(2,11):
                    self.cards.append(Card(str(c),s))
                for f in ["Jack","Queen","King","Ace"]:
                    self.cards.append(Card(f,s))
            shuffle(self.cards)

        def draw_card(self):
            return self.cards.pop() 

        def show(self):
            for card in self.cards:
                card.show()

    class Player:
        def __init__(self, name):
            self.hand = []
            self.name = name

        def draw(self, deck):
            self.hand.append(deck.draw_card())
            return self
        
        def showhand(self, game):
            if self.name == "Dealer" and game == True:
                    self.hand[0].show()
            else:
                for card in self.hand:
                    card.show()
        def total(self):
            total = 0
            aces = 0
            for card in self.hand:
                total += card.value()
                if card.rank == "Ace":
                    aces += 1
            while total >21 and aces:
                total -= 10
                aces -= 1
            return total                
    game = True
    adeck = Deck()
    print("The dealer draws a hidden card and a ...")
    dealer = Player("Dealer")
    dealer.draw(adeck).draw(adeck)
    dealer.showhand(game=True)

    tomas = Player("Tomas")
    print("You draw ...")
    tomas.draw(adeck).draw(adeck)
    tomas.showhand(game=True)
    print (f"Your hand is {tomas.total()}")

    while game == True:
        play = input("Hit(h) or Stand(s)?: ")
        if play == "h":
            tomas.draw(adeck)
            tomas.showhand(game=True)
            print (f"Your hand is {tomas.total()}")
        if tomas.total() > 21:
            print("You're bust!")
            game = False
        if play == "s" and dealer.total() < tomas.total():
            dealer.draw(adeck)
            dealer.showhand(game=False)
            print (f"Dealer's hand is {dealer.total()}")
        if dealer.total() > 21:
            print (f"Dealer's hand is {dealer.total()}, you win!")
            game = False
        if dealer.total() > 17:
            dealer.draw(adeck)
        if dealer.total() < tomas.total():
            print (f"Your hand is {tomas.total()} and Dealer's hand is {dealer.total()}, you win!")
            game = False
        if dealer.total() == tomas.total():
            print(f"It's a draw!")
            game = False
if __name__ == "__main__":
    main()