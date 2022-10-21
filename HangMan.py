"""
Created by Animesh Das
BSc IT 1st Sem 2022
"""

import random

#Opening the txt file and storing its contents
f = open("HangmanWords.txt","r")
data = f.readline()
words = data.split()

#selecting a random "word" from the "words"
word = random.choice(words)

lives = 7  #Total Lives 
guessed_word = "-"*len(word) #It will display as many dashes as the selected random "word"

while lives != 0: #This loop will continue unless the player has exhausted their total "lives"
    print(guessed_word)
    print()
    letter = input("Guess a letter: ").lower()

    #If the "letter" inputed by the player is in the "word" then this block will be executed
    if letter in word:
        #Main Logic Block
        for index in range(len(word)):
            if word[index] == letter: 
                guessed_word = guessed_word[:index] + letter + guessed_word[index+1:]

        #Win Block
        if guessed_word == word:
            print()
            print("Congratulations you Won !!")
            break

    #If the "letter" inputed by the player is "NOT" in the "word" then this block will be executed
    else:
        lives -= 1
        print()
        print("Incorrect Guess !")
        print(f"Remaining lives are {lives}.")
        print()

#Within the "WHILE LOOP" if the player does NOT WIN" then this "ELSE" block will be executed        
else:
    print("Game Over !!")
    print("You Loose !")

#Whether the player WIN'S or LOOSE this statement will be executed and will tell the secret "WORD"    
print(f"The Secret word was {word}")

"""
At the time of making this program, I was in a hurry. Since I was time bounded. And for this reason
I didn't got to implement some of the features in this game. If you are looking this code and if you
are a python enthusiast then you can try to code the features.
The  features that i wanted are:
(1)This program runs only Once. So I wanted to run the whole program in a "WHILE LOOP".
   After  completing one iteration and prompting about the secret word the program should ask the
   user "Do you want to continue playing ?(y/n)" . If the user wants to play then a new secret word
   will be selected and continue. And if the user does not want to play then the program would stop
   running.
   
(2)The second feature I wanted was that, It should have a score system. At the very end it should
   output how many guesses we have correctly gussed and how many we fail to guessed.
   
"""



