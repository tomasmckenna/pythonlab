"""
x = 30
y = 3.1415
name = "Bertil"

print (type(x))
z = str(x)
print(type(z))

a = "10"
b = float(a) + 1
print (b)

print(len("Bertil"))
print(name.upper())
print(name.lower())
print("   spaces  ".strip())

print(f"My name is {name} and I'm {x} years old")
print("pi is approx {:.2f}".format(y))

#LISTS []
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("date")
print(fruits[0])

#DICTS {}
person_dict = {"name":"Alice", "age":30, "city":"New York"}
print(person_dict["name"])
person_dict["job"] = "Developer"
print(person_dict)
person_dict2 = {"name":"Bob", "age":20, "city":"New York"}
person_list.append(person_dict)
person_list.append(person_dict2)

#SETS 
fruits = ["apple", "banana", "cherry"]
unique_numbers = {1,2,3,4,5,6,5,6,}
print(unique_numbers)
unique_numbers = set(unique_numbers)
unique_fruits = set(fruits)
print(unique_numbers)

print("Range Loop")
for i in range(5):
    print (i)

def greet(name):
    print(f"Hello, {name}")
    return f"Hello, {name}!"

print(greet("Calle")) # greeting = greet("Calle")


Uppgift 1
Skriv ett program som emot en sträng som input och skriver ut längden på strängen. 
Exempel-input: "thisIsAString" Förväntad output: 13

def main():
    string = input('What is your string?: ')
    str_length = 0
    for _ in string:
        str_length += 1
    print(f'{str_length}')


if __name__ == "__main__":
    main()

Uppgift 2
Skriv ett program som skriver ut frekvensen av tecken i en given sträng. 
Exempel-input: "banana" Förväntad output: {"b":1, "a":3, "n":2}

def main():
    sentence = input("What is your sentence?: " )
    char_list = {}
    for _ in sentence:
        if _ in char_list:
            char_list[_] += 1
        else:
            char_list[_] = 1
    print (f'{char_list}')

if __name__ == "__main__":
    main()

Uppgift 3
Skriv ett program som för en given sträng skriver ut de två första och de två sista tecknen i strängen 
(på valfritt format) Exempel-input: "banana" Förväntad output: "ba na"

def main():
    sentence = input('What is your sentence?: ')
    sent = sentence[0] + sentence[1] # sentence[0:2] + sentence[-2:]
    ence = sentence[-2] + sentence[-1]
    print (f'{sent}{ence}')

if __name__ == "__main__":
    main()

Uppgift 4
Skriv ett program som tar två strängar som input och skapar EN ny sträng där de 
två första tecken i varje sträng bytts ut. Exempel-input: "abc", "xyz" Förväntad output: "xyc abz"

def main():
    sent_1 = input('What is your sentence?: ')
    sent_2 = input('What is your second sentence?: ')
    sent = sent_1[0] + sent_1[1]
    ence = sent_2[0] + sent_2[1]
    fixed_sent_1 = sent + sent_2[2:]
    fixed_sent_2 = ence + sent_1[2:]
    
    print (f'{fixed_sent_2} {fixed_sent_1}')

if __name__ == "__main__":
    main()


Uppgift 5
Skriv ett program som lägger till "ing" i slutet av en given sträng, 
om strängen är kortare än 3 tecken ska den lämnas ofärndrad. Expempel-input: 
"Python" Förväntad output: "Pythoning"

def main():
    sentence = input('What is your sentence?: ')
    if len(sentence) > 3:
        print(f'{sentence}ing')
    else:
        print(f'{sentence}')
    
if __name__ == "__main__":
    main()

Uppgift 6
Skriv ett program som först tar bort all whitespace 
(mellanslag, tab (\t), newline(\n)), och sedan även tar bort alla tecken på ojämna indexvärden, 
från given sträng. Exempel-input: "a string with spaces and a newline character\n" 
Förväntad output: "atigihpcsnaelncaatr"

def main():
    sentence = input('What is your sentence?: ')
    sent = sentence.replace(" ", "")
    sent2 = sent.replace("\t", "")
    sent3 = sent2.replace("\n", "") 
    sent4 = sent3[::2]
    print(f'{sent4}')

if __name__ == "__main__":
    main()

Uppgift 7
Skriv ett program som tar en komma-separerad sekvens av ord och skriver ut de unika orden 
i alfabetisk ordning. Exempel-input: "red, white, black, red, green, black" 
Förväntad output: "black, green, red, white"

def main():
    list_1 = input("What are your words (CSV)?: ").split(',',)
    list_2 = []
    for _ in list_1:
        if _ not in list_2:
            list_2.append(_)    
    sorted_list = sorted(list_2)
    print(f'{sorted_list}')

if __name__ == "__main__":
    main()

def main():
    list_1 = input("What are your words (CSV)?: ").split(',',)
    list_2 = set(list_1)
    sorted_list = sorted(list_2)
    print(f'{sorted_list}')

if __name__ == "__main__":
    main()


Uppgift 8
Skriv en funktion som konverterar en given sträng till versaler (uppercase) om den 
innehåller minst 2 versaler bland de 4 första tecknen.

def main():
    sentence = input('What is your sentence?: ')
    first_2 =  sentence[0] + sentence[1]
    if first_2.isupper():
        sent = sentence.upper()
    else:
        sent = sentence
    print(f'{sent}')

if __name__ == "__main__":
    main()

Uppgift 9
Skriv en funktion som vänder (reverse) på en sträng om dess längd är en multipel av 4.

def main():
    sentence = input('What is your sentence?: ')
    if len(sentence) % 4 == 0:
        ecnetnes = sentence[::-1]
        print(f'{ecnetnes}')

if __name__ == "__main__":
    main()

Uppgift 10
Skriv en funktion som skapar en ny sträng bestående av 4 kopior av de två sista tecken 
i en given sträng. Exempel-input: "Python" Förväntad output: "onononon"
/
def main():
    sentence = input("What is your sentence?: ")
    ce = sentence[-2:] * 4
    print(f"{ce}")

if __name__ == "__main__":
    main()

Uppgift 11
Skriv en funktion som tar emot en lista med ord och returnerar det längsta ordet samt dess längd

def main():
    list_1 = input("What are your words (CSV)?: ").split(',',)
    #print(f'{list_1}')
    list_2 = sorted(list_1, key = len)
    #print(f'{list_2}')
    longest = list_2[-1]
    print(f'{longest} is {len(longest)} chars long')

if __name__ == "__main__":
    main()

Uppgift 12
Skriv ett program som genererar en enkel multiplikationsmodell för tal 1-10. 
Hur snyggt kan du få tabellen? Läs på om sträng-formattering i Python.

def main():
    for i in range(1, 11):
        print("{:6d} {:6d} {:6d} {:6d} {:6d} {:6d} {:6d} {:6d} {:6d} {:6d}"
                .format(i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10))

if __name__ == "__main__":
    main()


def main():
    for i in range(1, 11):
        print("______________________________________________________________________")
        print("|{:5d} |{:5d} |{:5d} |{:5d} |{:5d} |{:5d} |{:5d} |{:5d} |{:5d} |{:5d}|"
                .format(i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10))
    print("______________________________________________________________________")
if __name__ == "__main__":
    main()


Uppgift 13
Skriv en funktion som beräknar fakulteten av ett givet tal

def main():
    number = int(input("What is your int?: "))
    result = 1
    for _ in range(1, number):
        result = result * _
    print (f'{result}')
if __name__ == "__main__":
    main()

Uppgift 14
Skapa ett enkelt gissningsspel där datorn väljer ett slumpmässigt tal mellan 1-100
 (eller annat intervall), och låt användaren gissa tills de hittar rätt nummer. 
 För varje felaktig gissning berättar datorn om det rätta svaret är högre eller lägre än spelarens gissning.

import random
def main():
    number = int(input("What level would you like to play (1-100)?: "))
    random_int = random.randint(1,number)
    guess = int()
    while guess != random_int:
        guess = int(input("What is your guess?: "))
        if guess > random_int:
            print (f'Too high!')
        elif guess < random_int:
            print (f'Too low!')
    print (f"That's the right answer!")
if __name__ == "__main__":
    main()

Uppgift 15
Skriv ett program som kontrollerar om ett givet ord är ett palindrom 
(läses likadant framifrån som bakifrån).

def main():
    def is_pal():
        sentence = input("What is your word?: ")
        rev_sentence = reverse(sentence)
        if rev_sentence == sentence:
            print(f'{sentence} is a palindrome')
        else:
            print(f'{sentence} is not a palindrome')
    def reverse(sentence):
        rev_sentence = ""
        index = len(sentence)
        while index:
            index -= 1
            rev_sentence += sentence[index]
        return rev_sentence
    
    is_pal()
    
if __name__ == "__main__":
    main()


Write a program that asks for the name of the user and then prints the message:

Hi name

Name should be the name the user entered. 

name = input("What's your name?: ")
print (f"Hi {name}")

Write a program that asks the user for two numbers and store them in two variables called num1 and num2. Add them together and store the result in a variable called result and print the result back to the user.

NOTE! All input we get from the input function will be stored as strings so num1 and num2 must first be converted to integers with the int() function. 

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
result = num1 + num2
print(f"{result}")

Write a program that gives an answer to the following problem:

In a group there are three girls and two boys. 
If we have 5 more identical groups how many persons will there be?
Let the program add 3 and 2 and multiply it with 6. 
Do this in one line and store the result in a variable
 then print the result. 

girls = 3
boys = 2
group = girls + boys
total_groups = group * 6
print(f"{total_groups}")

Selection

Write a program that takes a character (i.e. a string of length 1) and
 tells the user if the character is a vowel or not.

character = str(input("What is your char?: "))
if character in ["a", "e", "i", "o", "u"]:
    print(f"Char is a vowel")
else:
    print(f"Char is not a vowel")

Write a program that asks how old the user is and then 
tells the user if she is a teen or not.

age = int(input("What is your age?: "))
if age in range(13,19):
    print(f"You are a teenager")
else:
    print(f"You are not a teenager")

It is common for images of a country’s previous leaders, or other individuals of historical significance, to appear on its money. The individuals that appear on banknotes in the United States are listed in the table below.
Write a program that begins by reading the denomination of a banknote from the user. 
Then your program should display the name of the individual that appears on the banknote of the entered amount. 
An appropriate error message should be displayed if no such note exists.

Individual	Amount
George Washington	$1
Thomas Jefferson	$2
Abraham Lincoln	$5
Alexander Hamilton	$10
Andrew Jackson	$20
Ulysses S. Grant	$50
Benjamin Franklin	$100
Hint:
The solution given will use a dictionary. 

notes = {"1": "Washington", "2": "Jefferson", "5": "'Lincoln", "10": "Hamilton", "20": "Jackson", "50": "Grant", "100": "Franklin"}
note = input("What is your denomination?: ")
if note in notes:
    print(f"Your note shows {notes[note]}")
else:
    print(f"No note found")

Using only simple variables and if statements, 
you should be able to get this to work; a loop is not needed.

Given 3 numbers ( X , Y , Z ), 
assign variables x, y, z so that x ≤ y ≤ z 
and x, y, and z are from X , Y , and Z . 
Use only a series of if-statements and assignment statements.

Hint:
You must define the conditions under which you choose between x← X , x← Y or x← Z. 
You will do a similar analysis for assigning values to y and z. 
Note that your analysis for setting y will depend on the value set for x; 
similarly, your analysis for setting z will depend on values set for x and y. 

#x, y, z = sorted([X, Y, Z])

X = int(input("What is your first number?: "))
Y = int(input("What is your second number?: "))
Z = int(input("What is your third number?: "))

if X <= Y <= Z:
    x = X 
    y = Y 
    z = Z
elif Y <= X <= Z:
    x = Y
    y = X
    z = Z
elif Y <= Z <= X:
    x = Y
    y = Z
    z = X
elif X <= Z <= Y:
    x = X
    y = Z
    z = Y
elif Z <= Y <= X:
    x = Z
    y = Y
    z = X
elif Z <= X <= Y:
    x = Z
    y = X
    z = Y

print (f"{x} is <= {y} is <= {z}")

A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
				
The numbers after the direction are steps. 
Please write a program to compute the distance from current position 
after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.

Example:
If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2
					
Then, the output of the program should be: 2

Hint:
In case of input data being supplied to the question, 
it should be assumed to be a console input.
The solution for this exercise uses functions. 
If you are not familiar with them yet you should wait with 
this exercise until you are. Look at solution

import math

def main():
    distance()

def distance():
    up_dist = int(input("up: "))
    down_dist = int(input("down: "))
    left_dist = int(input("left: "))
    right_dist = int(input("right: "))
    result = int(math.sqrt((up_dist-down_dist)**2 + (left_dist-right_dist)**2))
    print(f"{result}")

if __name__ == "__main__":
    main()

Iteration

Write a program that capitalizes all the vowels in a string.

Hint:
It is up to you to diecide if you want to consider Y a vowel or not.
Remeber that a string is immutable and can therefor not be changed so 
you will need to create a new string. Look at solution

sentence = input('What is your sentence?: ' )
upper_sentence = ""
for _ in sentence:
    if _ in ["a", "e", "i", "o", "u"]:
        upper_sentence += _.upper()
    else:
        upper_sentence += _
print(f"{upper_sentence}")

Write a program which will find all such numbers 
which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included).
The numbers obtained should be printed in a 
comma-separated sequence on a single line.

Hint:
Consider use range(#begin, #end) method Look at solution
num_list = list(range(2000,3201))
print (f'{num_list}')
final_list = []
for _ in num_list:
    if _ % 7 == 0:
        final_list .append(_)
for _ in final_list:
    if _ % 5 == 0:
        final_list .remove(_)
print (f'{final_list}')


num_list = list(range(2000,3201))
print (f'{num_list}')
final_list = []
final_list_2 = []
for _ in num_list:
    if _ % 7 == 0:
        final_list .append(_)
for _ in final_list:
    if _ % 5 != 0:
        final_list_2 .append(_)
print (f'{final_list_2}')


With a given number n, write a program to generate a dictionary
 that contains (i, i*i). 
The dictionary shall include all integer values 
for i from 1 to n (both included). 
Then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
        	
Hint:
As this exercise assume you are familiar with dictionaries y
ou should wait to do it until you know how dictionaries work.
In case of input data being supplied to the question, 
it should be assumed to be a console input. 
Consider use dict() Look at solution

number = int(input("What is your number?: "))
num_list = range(number + 1)
square_list = {}
for _ in num_list:
    square_list[_] = _ * _
print(f'{square_list}')


Write a program, which will find all such numbers between 1000 and 3000 
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence
 on a single line.

Convert the number into a string and use list(converted_number) on
 the string to get a list of digits Look at solution

num_list = list(range(1000,3001,2))
string_list = ", ".join(map(str, num_list))
print (f'{string_list}')

Functions

Define a function max() that takes two numbers as arguments 
 returns the largest of them. Use the if-else construct available
  in Python. (It is true that Python has the max()
   function built in, but writing it yourself is nevertheless
    a good exercise.) Look at solution


def main():
    def max():
        num1 = int(input('What is your first number?: '))
        num2 = int(input('What is your second number?: '))
        if num1 > num2:
            print(f'{num1} is larger')
        else:
            print(f'{num2} is larger')
    max()
if __name__ == "__main__":
    main()


Define a function max_of_three() that takes three numbers as arguments
 and returns the largest of them. Look at solution
def main():
    def max_of_three():
        num1 = int(input('What is your first number?: '))
        num2 = int(input('What is your second number?: '))
        num3 = int(input('What is your third number?: '))
        num_list = sorted([num1, num2, num3])
        print(f'{num_list[-1]}')

    max_of_three()
if __name__ == "__main__":
    main()

Define a function that computes the length of a given list or string. 
(It is true that Python has the len() function built in, 
but writing it yourself is nevertheless a good exercise.) 

def main():
    def string_length():
        sentence = input("What is your sentence?: ")
        sen_len = 0
        for _ in sentence:
            sen_len += 1
        print (f"{sen_len}")
    
    string_length()

if __name__ == "__main__":
    main()


Write a function that takes a character 
(i.e. a string of length 1) and 
returns True if it is a vowel, False otherwise. Look at solution

def main():
    def char_check():
        char = input("What is your character?: ")
        if char in ['a', 'e', 'i', 'o', 'u']:
            return True
        else:
            return False

    result = char_check()
    print(result)
if __name__ == "__main__":
    main()

Write a function translate() that will translate a text into "rövarspråket" 
(Swedish for "robber's language"). That is, double every consonant and place
 an occurrence of "o" in between. For example, 
 translate("this is fun") should return the string 
 "tothohisos isos fofunon". 

def main():
    def rovar():
        sentence = input("What is your sentence?: ")
        rov_sentence = ""
        for _ in sentence:
            if _ not in ['a', 'e', 'i', 'o', 'u', ' ']:
                rov_sentence += (_ + "o" + _)
            else:
                rov_sentence += _
        print(f'{rov_sentence}')
    rovar()

if __name__ == "__main__":
    main()        

Define a function sum() and a function multiply() 
that sums and multiplies (respectively) 
all the numbers in a list of numbers. For example, 
sum([1, 2, 3, 4]) should return 10, and 
multiply([1, 2, 3, 4]) should return 24. Look at solution

def main():
    def summa():
        sum_list = input("Give your list of numbers, csv: ").split(',', )
        int_sum_list = [int(x) for x in sum_list]
        summed = sum(int_sum_list)
        print(f'{summed}')

    summa()
    def mult():
        m_list = input("Give your list of numbers, csv: ").split(',', )
        int_m_list = [int(x) for x in m_list]
        multiplied = 1
        for _ in int_m_list:
            multiplied = multiplied * _
        print(f'{multiplied}')

    mult()
if __name__ == "__main__":
    main()
        

Define a function reverse() that computes the reversal of a string. 
For example, reverse("I am testing") should return the string "gnitset ma I". 

def main():
    def reverse():
        sentence = input("What is your sentence?: ")
        rev_sentence = ""
        index = len(sentence)
        while index:
            index -= 1
            rev_sentence += sentence[index]
        print(f'{rev_sentence}')
    
    reverse()

if __name__ == "__main__":
    main()

Define a function is_palindrome() that recognizes palindromes 
(i.e. words that look the same written backwards). 
For example, is_palindrome("radar") should return True. 

def main():
    def is_pal():
        sentence = input("What is your word?: ")
        rev_sentence = reverse(sentence)
        if rev_sentence == sentence:
            print(f'{sentence} is a palindrome')
        else:
            print(f'{sentence} is not a palindrome')
    def reverse(sentence):
        rev_sentence = ""
        index = len(sentence)
        while index:
            index -= 1
            rev_sentence += sentence[index]
        return rev_sentence
    
    is_pal()
    
if __name__ == "__main__":
    main()

Define a function overlapping() that takes two lists and returns
 True if they have at least one member in common,
  False otherwise. You may use your the in operator,
   but for the sake of the exercise, you should (also) 
   write it using two nested for-loops. That two for-loops are
    nested means that one loop is placed inside the other loop. 
   
def main():
    def overlap():
        list1 = input("Give your list of numbers, csv: ").split(',', )
        list2 = input("Give your second list of numbers, csv: ").split(',', )
        #print(f'{list1}')
        #list1 = [x.strip() for x in list1]
        #list2 = [x.strip() for x in list2]
        #print(f'{list1}')
        for _a in list1:
            #print(f'{_a}')
            for _b in list2:
                #print(f'{_b}')
                if _a == _b:
                    return True
        else:
            return False
    result = overlap()
    print (f'{result}')
if __name__ == "__main__":
    main()

Define a function generate_n_chars() that takes an integer n and a character c 
and returns a string, n characters long, consisting only of c:s. 
For example, generate_n_chars(5,"x") should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression 5 * "x" 
that will evaluate to "xxxxx". For the sake of the exercise you should 
ignore that the problem can be solved in this manner.) 
def main():
    def gen_n():
        n_int = int(input("What is your integer?: "))
        c_char = (input("What is your character?: "))
        while n_int:
            print (f'{c_char}', end='')
            n_int -= 1

    gen_n()
if __name__ == "__main__":
    main()

Define a function histogram() that takes a list of integers and 
prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
def main():
    def histo():
        histo_list = input('What is your list of ints (csv)?: ').split(',')
        for _ in histo_list:
            _ = int(_)
            hist = '*'
            print (_ * hist)

    histo()
if __name__ == "__main__":
    main()


The function max(), from exercise 13, and the function max_of_three(), 
from exercise 14, will only work for two and three numbers, respectively. 
But suppose we have a much larger number of numbers, or suppose we cannot tell 
in advance how many they are? Write a function max_in_list() that takes a list 
of numbers and returns the largest one. Look at solution

def main():
    def max_list():
        num_list = input("What is your list (csv)?: ").split(',')
        sort_list = sorted(num_list)
        print (f'{sort_list[-1]}')

    max_list()
if __name__ == "__main__":
    main()

In a particular jurisdiction, taxi fares consist of a base fare of $4.00,
 plus $0.25 for every 140 meters traveled. Write a function that takes
  the distance traveled (in kilometers) as its only parameter and
   returns the total fare as its only result. Write
    a main program that demonstrates the function.
Taxi fares change over time. Use constants to represent the base fare
 and the variable portion of the fare so that the program can be updated
  easily when the rates increase. Look at solution

def main():
    def taxi():
        dist = input('How far was the ride?: ')
        dist = float(dist)
        base_cost = 4.00
        var_cost = 0.25
        ride_cost = base_cost + (dist * 7.14285714286 * var_cost)
        return ride_cost
    ride_cost = round(taxi(),2)
    print (f'${ride_cost}')
if __name__ == "__main__":
    main()
# end main

Write a function that takes a string of characters as its first parameter,
 and the width of the terminal in characters as its second parameter.
  Your function should return a new string that consists of the original string and 
  the correct number of leading spaces so that the original string will appear centered
   within the provided width when it is printed. 
   Do not add any characters to the end of the string. Look at solution

import os
def main():
    char_string = input("Give your character string: ")
    char_len = len(char_string)
    #print (f'{char_len}')
    term_width = (os.get_terminal_size()[0])
    lead_space = ((term_width - char_len) // 2) 
    cent_string = (' ' * lead_space) + char_string
    print (f'{cent_string}')
    #print (f'{term_width}')
    #print (f'{lead_space}')


if __name__ == "__main__":
    main()

Write a function find_longest_word() that takes a list of words and
 returns the length of the longest one. Look at solution

def main():
    def find_long():
        words = input('What are your words, csv?: ').split(',')
        sorted_words = sorted(words, key = len)
        longest = len(sorted_words[-1])
        print(f'{longest}')
    
    find_long()

if __name__ == "__main__":
    main()

Write a function filter_long_words() that takes a list of words and
 an integer n and returns the list of words that are longer than n

def main():
    def filt():
        words = input('What are your words, csv?: ').split(',')
        word_int = int(input('What is your int?: '))
        output_list = []
        for _ in words:
            word_len = len(_)
            if word_int < word_len:
                output_list.append(_)
        print (f'{output_list}')

    filt()
if __name__ == "__main__":
    main()


A prime number is an integer greater than 1 that is only divisible by one and itself
. Write a function that determines whether or not its parameter is prime, returning
 True if it is, and False otherwise. Write a main program that reads an integer
  from the user and displays a message indicating whether or not it is prime. Ensure
   that the main program will not run if the file containing your solution is imported
    into another program.
Hint:
Consider using the modulus operator % Look at solution

def main():
    def prime():
        is_prime = int(input("What is your int: ")) 
        for _ in range(2,is_prime):
            if is_prime % _ != 0:
                print (f"{is_prime} is a prime.")
            else:
                print(f"{is_prime} is not a prime")
                return

    prime()

if __name__ == "__main__":
    main()

In this exercise you will create a function named nextPrime that finds and 
returns the first prime number larger than some integer, n. 
The value of n will be passed to the function as its only parameter. 
Include a main program that reads an integer from the user and 
displays the first prime number larger than the entered value.

Hint:
Use your solution from the previous exercise to solve this Look at solution

def main():
    def prime(prime_candidate):
        for _ in range(2,prime_candidate):
            if prime_candidate % _ == 0:
                return False    
        return True

    def next_prime():
        prime_candidate = int(input("What is your int: ")) 
        prime_candidate += 1
        while not prime(prime_candidate):    
            prime_candidate += 1
        print (f"{prime_candidate}")
        
    next_prime()

if __name__ == "__main__":
    main()


Lists

Write a program that maps a string with several words into a list of words, 
that is each word in the original string will be one item in the new list. Look at solution
def main():
    sentence = input("What is your sentence?: ").split(" ")
    print(f'{sentence}')

if __name__ == "__main__":
    main()

Write a program that reads integers from the user and stores them in a list.
 Your program should continue reading values until the user enters 0. 
 Then it should display all of the values entered by the user 
 (except for the 0) in order from smallest to largest, with one value appearing on each line.

Hint:
Use either the sort method or the sorted function to sort the list. Look at solution

def main():
    list_ints = []
    sentence = None
    while sentence != 0:
        sentence = int(input("What are your ints?: "))
        if sentence != 0:
            list_ints.append(sentence)
    sorted_list = sorted(list_ints)
    print(f'{sorted_list}')

if __name__ == "__main__":
    main()

Write a program that reads integers from the user and stores them in a list.
 Use 0 as a sentinel value to mark the end of the input.
  Once all of the values have been read your program should display them (except for the 0)
   in reverse order, with one value appearing on each line.
Hint:
Start by solving the previous exercise Look at solution

def main():
    list_ints = []
    sentence = None
    while sentence != 0:
        sentence = int(input("What are your ints?: "))
        if sentence != 0:
            list_ints.append(sentence)
    sorted_list = sorted(list_ints, reverse = True)
    for _ in sorted_list:
        print(f'{_}', end = "\n")

if __name__ == "__main__":
    main()


Write a function that determines whether or not a list of values is in sorted order
 (either ascending or descending). The function should return True
  if the list is already sorted. Otherwise it should return False. 
  Write a main program that reads a list of numbers from the user and
   then uses your function to report whether or not the list is sorted.
Make sure you consider these questions when completing this exercise:
 Is a list that is empty in sorted order? What about a list containing one element?

def main():
    list_ints = []
    sentence = None
    while sentence != 0:
        sentence = int(input("What are your ints?: "))
        if sentence != 0:
            list_ints.append(sentence)
    sorted_list = sorted(list_ints)
    rev_sorted_list = sorted(list_ints, reverse = True)
    if sorted_list == list_ints or rev_sorted_list == list_ints:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()

In this exercise you will create a program that 
identifies all of the words in a string entered by the user. 
Begin by writing a function that takes a string of text as its only parameter.
Your function should return a list of the words in the string 
with the punctuation marks at the edges of the words removed. 
The punctuation marks that you must remove include commas, periods, 
question marks, hyphens, apostrophes, exclamation points, colons
, and semicolons. Do not remove punctuation marks that appear in the middle of a words
, such as the apostrophes used to form a contraction. 
For example, if your function is provided with the string 
"Examples of contractions include: don’t, isn’t, and wouldn’t." 
then your function should return the list 
["Examples", "of", "contractions", "include", "don’t", "isn’t", "and", "wouldn’t"].

Hint:
As this exercise uses functions you should be familiar with them before
 you try to solve this one. Look at solution

def main():
    sentence = input("What is your sentence?: ").split(" ")
    print(f"{sentence}")
    fixed = []
    for _ in sentence:
        _ = _.strip(",.?!-':;")
        fixed.append(_)
    print (f"{fixed}")

if __name__ == "__main__":
    main()

Dictionary and Set

Create a program that determines and displays the number of unique characters 
in a string entered by the user. For example, Hello, World! has 10
 unique characters while zzz has only one unique character.

Hint:
Use a dictionary or set to solve this problem. Look at solution

def main():
    chars = set(" ")
    sentence = input("What is your sentence?: ").split(" ")
    for _ in sentence:
        for char in _:
            if char not in chars:
                chars.add(char)
    print(f"{chars}")

if __name__ == "__main__":
    main()


In cryptography, a Caesar cipher is a very simple encryption techniques
 in which each letter in the plain text is replaced by a letter some
  fixed number of positions down the alphabet. For example, with a shift of 3
  , A would be replaced by D, B would become E, and so on. The method is named
   after Julius Caesar, who used it to communicate with his generals. ROT-13 
   ("rotate by 13 places") is a widely used example of a Caesar cipher where the
    shift is 13. In Python, the key for ROT-13 may be represented by means of the
     following dictionary:

		
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done,
 you will be able to read the following secret message:

Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!

Note that since English has 26 characters, your ROT-13 program will be
 able to both encode and decode texts written in English. Look at solution

def main():

   key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 

Do the same Caesar chipher as in the previous example but the time use ROT-3,
 that is rotate the letters three steps. Create two functions, one for coding
  messages and one for decoding them.

Hint:
You might want to use two dictionaries to solve this problem. In the solution section
 you will find three different solutions. For some extra chalenge you can try
  to solve this in all three ways.

The first solution is straight forward as explained in the exercise text

The second solution has two extra functions that will generate the dictionaries. 
They will both take one argument, a number indicationg how many steps used when
 rotating the dictionaries. One of the functions generates a dictionary that is used
  for encryption and the other a dictionary used for encryption.
   We can also use a single function to encrypt and decrypt if we pass in the
    dictionary to be used to the enchipher function along with the text that should
     be encrypted/decrypted.

The third version is the most advanced. Here we use list comphrensions along
 with the chain function from itertools. If used with the maketrans and
  translate functions in the string class we can perform this operation using only one
   line för generating the key tables and encrypt the string and an other
    line that does the same when decrypting. If you manage to solve this you are
     working on a professional Python level.
# newlist = [x if x != "banana" else "orange" for x in fruits] 
"""
def main():
    from itertools import chain 
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
        'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
        'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
        'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
        'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
        'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
        'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 
    sentence = input("Whatis your sentence?: ")
    raw_sent = str(chain(sentence))
    #print (f"{raw_sent}")
    #rot_sent = [key[_] if _ in key else _ for _ in raw_sent]
    rot_sent = raw_sent.maketrans(key)
    print (f"{rot_sent}")
    for _ in rot_sent:
        print(f"{_}", end ="")

if __name__ == "__main__":
    main()
"""
In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a
 function that simulates rolling a pair of six-sided dice. Your function will
  not take any parameters. It will return the total that was rolled on two dice as its only result.

Write a main program that uses your function to simulate rolling two six-sided 
dice 1,000 times. As your program runs, it should count the number of times that
 each total occurs. Then it should display a table that summarizes this data. Express
  the frequency for each total as a percentage of the total number of rolls. Your
   program should also display the percentage expected by probability theory for each
    total. Sample output is shown below.

Total	Simulated %	Expected %
2	2.90	2.78
3	6.90	5.56
4	9.40	8.33
5	11.90	11.11
6	14.20	13.89
7	14.20	16.67
8	15.00	13.89
9	10.50	11.11
10	7.90	8.33
11	4.50	5.56
12	2.60	2.78
 

Hint:
To simulate dice rolls first import random to your module. Then you can simulate
 the roll by using the code

r = random.randrange(6) +1

The reason we use +1 is that randrange will give us a random number from
 0 and up to but not including the number we pass to it. Look at solution


Morse code is an encoding scheme that uses dashes and dots to represent numbers and letters.
 In this exercise, you will write a program that uses a dictionary to store the mapping from
  letters and numbers to Morse code. Use a period to represent a dot, and a
   hyphen to represent a dash. The mapping from letters and numbers to dashes and dots is
    shown in the table below. Your program should read a message from the user.
     Then it should translate each letter and number in the message to Morse code,
      leaving a space between each sequence of dashes and dots. Your program should ignore any
       characters that are not letters or numbers. The Morse code for Hello, World! is shown below:
          .... . .-.. .-.. --- .-- --- .-. .-.. -..
Letter	Code	Letter	Code	Letter	Code	Letter	Code
A	.-	J	.---	S	...	1	.----
B	-...	K	-.-	T	-	2	..---
C	-.-.	L	.-..	U	..-	3	...--
D	-..	M	--	V	...-	4	....-
E	.	N	-.	W	.--	5	.....
F	..-.	O	---	X	-..-	6	-....
G	--.	P	.--.	Y	-.--	7	--...
H	....	Q	--.-	Z	--..	8	---..
I	..	R	.-.	0	-----	9	----.
Look at solution
List Comprehension

Write a list comprehension that creates a list of tuples. Each tuple has
 two values, a temperature in Farenheit and a temperature in Celsius.

Create one list for Farenheit values from 0 to 100 in steps of 5 and the matching Celsius values.

Create another list for Celsius values from -10 to 50 in steps of 2 and the matching Farenheit values.

Hint:
The conversion formulas between °F and °C are:

°C = (°F - 32) × 5/9
°F = °C × 9/5 + 32

Look at solution


Write a list comprehension that uses nested for-clauses to create a single list with all 36 different
 dice combinations from (1,1) to (6,6).

Hint:
The nested for-clauses mean that you have to independent for-loops, one for each dice
. Also note that each combintaion can be stored as a tuple. Look at solution

Files

To solve this exercise you will first need to download this text file. It is the
 full book of Alice in Wonderland by Lewis Carroll. Write a program that reads the entire
  file and counts the number of times each word occurs in the text. You must consider removing
   punction characters, like periods, commas and so on from the text, without touching things like
    apostrophes found inside a word. When finished the program shall present a sorted list of the 100
     most frequent words in the text. It should also present the longest word in the text.

Hint:
Consider using the Counter from the collections module and a regex expression to remove all unwanted
 punctuation marks.

When you have solved it you can, for some extra challenge, try to make your program more compact
. The solution is only 26 lines long including code that formats a nice output
. Can you beat that? Look at solution

Function Generators

Define a function generator which can iterate the numbers, which are divisible by 7
, between a given range 1 and n.

Hint:
You should use a generator by using yield in the function. Look at solution

Misc Exercises

Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog."
"Was it a rat I saw?"
"Step on no pets"
"Sit on a potato pan, Otis"
"Lisa Bonet ate no basil"
"Satan, oscillate my metallic sonatas"
"I roamed under it as a tired nude Maori"
"Rise to vote sir"
"Dammit, I'm mad!"
Note that punctuation, capitalization, and spacing are usually ignored. Look at solution


A pangram is a sentence that contains all the letters of the English alphabet at least
 once, for example:
The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a pangram or not
. Look at solution


"99 Bottles of Beer" is a traditional song in the United States and Canada. It is
 popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and
  can take a long time to sing. The song's simple lyrics are as follows:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers
 reach zero.

Your task here is write a Python program capable of generating all the verses of the song. Look
 at solution


Represent a small bilingual lexicon as a Python dictionary in the following fashion
d = {"merry":"frohe", "christmas":"weihnachten", "and":"und", "happy":"frohes", "new":"neues", "year":"jahr"}
and use it to translate your Christmas cards from English into German. That
 is, write a function translate() that takes a list of English words and returns a
  list of German words. Look at solution


Write a function char_freq() that takes a string and builds a frequency listing of the characters
 contained in it. Represent the frequency listing as a Python dictionary. Try it with
  something like char_freq("abbabcbdbabdbdbabababcbcbab"). Look at solution
"""