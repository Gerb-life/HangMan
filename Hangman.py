from operator import truediv
import random
from xml.etree.ElementTree import tostring
import functools
score = []
# Authors Gabriel Rodriguez , Jett Midkiff
# Date 4/29/2022
# version 1.0

#Hangman.py - This class contains all of the logic for the hangman game 
#and for user interaction with the game.
#

#This function is used to get the list of words from RandomWords.txt
#params- none
#returns - list of words from the txt file.
#
def readFile():  
# Open the file in read mode
    with open("RandomWords.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))  # using map funciton
        return words

#This function is responsible for displaying the main menu 
# in the command line to the user.
#params - none
#returns - none
#
def mainMenu():
    print("Welcome to the main menu")
    request = int(input("1: Play \n2: Exit\n")) #request input from the user
    #if 1 then play , if 2 then exit , else call mainMenu()
    if(request == 1):
        playMenu() # recursion
    elif(request ==2):
        quit()
    else:
        mainMenu()

#This function is used to display the play menu to the user.
# The user has the option to play normal , play easy or exit.
# params- none
# returns- none
#     
def playMenu():
    print("Welcome to the play Menu")
    play = int(input("1:Play Normal\n2:Play Easy \n3:exit\n"))
    #if 1 then get random word from txtfile 
    if(play == 1):
        words = readFile()
        secretWord = random.choice(words)
        game(secretWord)
    # if 2 then filter list of words then pick random
    elif(play ==2):
        words = readFile()
        words = list(filter(lambda x: len(x) == 5 , words)) # lambda function and filter function
        secretWord = pickRandom(chooseRandomWord , words)  #calling a funciton with a funciton as a parameter
        game(secretWord)
    #if 3 then go back to playMenu    
    elif(play==3):
        mainMenu()
    #else then call playMenu again    
    else:
        playMenu()

#This function displays the game screen and contains the logic for the game.
#params- secretWord - word from either list or filtered list of words.
#returns - none
#
#
def game(secretWord):
    print(secretWord) # keep to display word so you dont have to guess everytime.
    turn = turnCounter() #using closure to keep track of turns
    lettersGuessed = ""
    
    print("A secret word has been chosen you may begin guessing letters \n")
    numGuesses = len(secretWord) + 5 #number of guesses
    while(numGuesses > 0 ):
             print("Turn number: " + str(turn()))
            
             #allowing user to either guess a letter or guess the whole word.
             guess = input("\nGuess a letter or try to guess the whole word!: \n") 
             
             #if guess is in secret word let user know they are correct 
             if(guess in secretWord):
                print(f"There are 1 or more {guess} in the word\n")
            #if guess is not in secret word subtract from number of guesses they have left
             else:
                sub1 = lambda x: x-1  #Labmda funciton for subtracting 1 from num guesses
                numGuesses = sub1(numGuesses)


                print(f"Try again you have {numGuesses} guesses left\n")
            
             lettersGuessed += guess
           
             #display the letters guessed so the user can keep track of their guesses
             print("Letters you have guessed: " +lettersGuessed)
             totalGuess = ""
             
             
             for letter in secretWord:
                 #if the letter is in the secret word print the letter
                if letter in lettersGuessed:
                    print(f"{letter}",end="")
                    totalGuess += letter
                #else print underscore to show user letters they have not guessed
                else:
                    print(f"_",end="")
                    totalGuess += "_"
              
             print("\n")
          
             #if the user's guess is the secret word display message and score and ask if they want to play again   
             if(checkGuess(secretWord , totalGuess)):
                 print(f"Congradulations you were right the secret word was {secretWord}")
                 score.append(numGuesses)
                 scoreTotal = functools.reduce(lambda a,b: a+b , score)
                 print(f"Your score is {scoreTotal}")
                 playAgain = int(input("Would you like to play again? \n1: Yes\n2: No\n"))
                 #if 1 then generate new word and call game
                 if(playAgain ==1):
                     words = readFile()
                     secretWord = random.choice(words)
                     game(secretWord)
                 #if 2 go back to the main menu
                 elif(playAgain ==2):
                     mainMenu()
                 #else go back to main menu
                 else:
                     mainMenu()
                 
    #if user cannot guess secret word display secret word
    else:
            print(f"\nThe secret word was {secretWord}")

    playAgain = int(input("Would you like to play again? \n1: Yes\n2: No\n"))
    #if 1 then generate new word and call game
    if(playAgain ==1):
        words = readFile()
        secretWord = random.choice(words)
        game(secretWord)
     #if 2 go back to the main menu
    elif(playAgain ==2):
        mainMenu()
    #else go back to main menu
    else:
        mainMenu()

#This function was used to check if the users guess is equal to the secret word.
#param- secretWord - secret word generated from reading the textfile
#param- guess- the users guesses
#return result- if guess is == to secret word then return true else return false.
#
def checkGuess(secretWord , guess): #pure function
    result = False
    if(secretWord == guess):
        result = True
    return result
#This funciton is being used to call another function and pass it the list
#param- action - function to be called
#param- list - list to be passed to another function
#return- result of action being passed the list
#
def pickRandom(action , list):
    return action(list)

#This function is being used to pick a random word from a list of words.
#param- words - list of words 
#return random.choice(words) - a random word chosen
#
def chooseRandomWord(words):
    return random.choice(words)

#This function is being used to increment the counter that displays what turn it is.
#params- none
#returns addTurn- function definition that adds one to the turn and returns it.
#
def turnCounter():   #closure that involves state change
    turn = 0
    def addTurn():
        nonlocal turn
        turn = turn + 1
        return turn
    return addTurn
#This is the main function all it does is call the main menu
# params none
# returns none
def main():
     mainMenu()

main() #calling main function.



