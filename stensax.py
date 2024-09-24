"""Projekt 3: Sten-sax-påse
Datorn slumpar vilken av sten, sax eller påse den ska välja.
Spelaren väljer också sten, sax eller påse.
Datorn och spelaren visar sedan upp sina val samtidigt.
Reglerna är enligt följande: sten vinner över sax, sax vinner över påse, 
och påse vinner över sten. 
Om båda väljer samma alternativ blir det oavgjort.
Spelaren spelar tills hen vinner eller förlorar mot datorn.
"""
import random
def main():
    options = ["sten", "sax", "påse"]
    state = False
    while state == False:
        computer_choice = random.choice(options)
        player_choice = input("sten, sax eller påse?: ")    
        if computer_choice == player_choice:
            print(f'Tie!') 
        if computer_choice == "sten" and player_choice == "sax":
            print('You lose!')
            state = True
        if computer_choice == "påse" and player_choice == "sax":
            print('You win!')
            state = True
        if computer_choice == "sten" and player_choice == "påse":
            print('You win!')
            state = True
        if computer_choice == "påse" and player_choice == "sten":
            print('You win!')
            state = True
        if computer_choice == "sax" and player_choice == "påse":
            print('You lose!')
            state = True
        if computer_choice == "sax" and player_choice == "sten":
            print('You win!')
            state = True

if __name__ == "__main__":
    main()