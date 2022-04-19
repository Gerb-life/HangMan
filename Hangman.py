import random
  
def readFile():  
# Open the file in read mode
    with open("RandomWords.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        print(random.choice(words))

readFile()

