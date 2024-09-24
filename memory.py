"""Projekt 2: Memory
Spelet fortsätter tills spelaren har gissat rätt ordning.
Datorn väljer ett antal slumpmässiga siffror eller bokstäver 
(beroende på svårighetsgrad) och visar dem i en viss ordning.
Sedan visar datorn samma siffror eller bokstäver igen, men denna gång blandat.
Spelaren ska gissa i vilken ordning siffrorna eller bokstäverna visades första gången.
"""
import random
from itertools import chain 

def main():
    original = [random.randrange(1,10) for _ in range(5)]
    print(f"{original}")
    guess = []
    randomised = random.sample(original, 5)
    print (f"{randomised}")
    while guess != original:
        guess = input("Guess the original sequence: ")
        guess = [int(x) for x in guess.split()]
    print("Correct!")
if __name__ == "__main__":
    main()