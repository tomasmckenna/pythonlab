"""
Projekt 1: Hangman
Skapa en version av det klassiska spelet Hangman.
Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.
Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.
Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.
Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.
"""
import random
def main():
    word_list = ["banana", "apple", "orange", "pineapple"]
    word = random.choice(word_list)
    print (f"{len(word)}")
    word_unique = set(word)
    guess_list = []
    while len(guess_list) != len(word_unique):
        guess = input("\n What letter?: ")
        if guess in word:
            guess_list.append(guess)
        for char in word:
            if char in guess_list:
                print (f"{char}", end = "")
            else:
                print(f" _ ", end = "")

if __name__ == "__main__":
    main()