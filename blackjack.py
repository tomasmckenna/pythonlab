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
def main():
    class Card:
        suits = {'c': '♣','d': '♦','h': '♥','s': '♠'}
        
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

        def show(self):
            print (f"The {self.rank} of {Card.suits[self.suit]}")
    acard = Card(1, 's')
    acard.show()

if __name__ == "__main__":
    main()