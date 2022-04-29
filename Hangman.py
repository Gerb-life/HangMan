from operator import truediv
import random
from xml.etree.ElementTree import tostring
import functools
score = []

def readFile():  
# Open the file in read mode
    with open("RandomWords.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))  # using map funciton
        return words


def mainMenu():
    print("Welcome to the main menu")
    request = int(input("1: Play \n2: Exit\n"))

    if(request == 1):
        playMenu() # recursion
    elif(request ==2):
        quit()
    else:
        mainMenu()
    
def playMenu():
    print("Welcome to the play Menu")
    play = int(input("1:Play Normal\n2:Play Easy \n3:exit\n"))

    if(play == 1):
        words = readFile()
        secretWord = random.choice(words)
        game(secretWord)
    elif(play ==2):
        words = readFile()
        words = list(filter(lambda x: len(x) == 5 , words)) # lambda function and filter function
        secretWord = pickRandom(chooseRandomWord , words)  #calling a funciton with a funciton as a parameter
        game(secretWord)
        
    elif(play==3):
        mainMenu()
    else:
        playMenu()

def game(secretWord):
    print(secretWord) # keep for testing purposes
    turn = turnCounter()
    lettersGuessed = ""
    
    
    print("A secret word has been chosen you may begin guessing letters \n")
    numGuesses = len(secretWord) + 5
    while(numGuesses > 0 ):
             print("Turn number: " + str(turn()))
            
             
             guess = input("\nEnter a letter: ")
             
             if(guess in secretWord):
                print(f"There are 1 or more {guess} in the word\n")
            
             else:
                sub1 = lambda x: x-1  #Labmda funciton for subtracting 1 from num guesses
                numGuesses = sub1(numGuesses)


                print(f"Try again you have {numGuesses} guesses left\n")
            
             lettersGuessed += guess
           
             
             print("Letters you have guessed: " +lettersGuessed)
             totalGuess = ""
             
             for letter in secretWord:
                if letter in lettersGuessed:
                    print(f"{letter}",end="")
                    totalGuess += letter
                
                else:
                    print(f"_",end="")
                    totalGuess += "_"
              
             print("\n")
          

             if(checkGuess(secretWord , totalGuess)):
                 print(f"Congradulations you were right the secret word was {secretWord}")
                 score.append(numGuesses)
                 scoreTotal = functools.reduce(lambda a,b: a+b , score)
                 print(f"Your score is {scoreTotal}")
                 playAgain = int(input("Would you like to play again? \n1: Yes\n2: No\n"))
                 if(playAgain ==1):
                     words = readFile()
                     secretWord = random.choice(words)
                     game(secretWord)
                 else:
                     mainMenu()
                 

    else:
            print(f"\nThe secret word was {secretWord}")

    mainMenu()


def checkGuess(secretWord , guess): #pure function
    result = False
    if(secretWord == guess):
        result = True
    return result

def pickRandom(action , list):
    return action(list)

def chooseRandomWord(words):
    return random.choice(words)

def turnCounter():   #closure that involves state change
    turn = 0

    def addTurn():
        nonlocal turn
        turn = turn + 1
        return turn
    return addTurn
    
def main():
     mainMenu()



main()



