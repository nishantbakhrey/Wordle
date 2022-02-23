from ctypes import sizeof
from curses.ascii import islower
import random
from collections import Counter
from turtle import position

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
# Class to take the user details as input 
class User:
    def __init__(self, first_name):
        self.first_name = first_name
    
    def greet(self):
        print(color.BOLD + color.UNDERLINE + "Hi %s," % (self.first_name) + color.END)

# function to calculate the number of vowels in the word
def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "AEIOU":
           num_vowels = num_vowels+1
    return num_vowels

# This function will print all the rules of the Game
def rules(User):
    print("\n")
    player.greet()
    print("Welcome to Nishant's implementation of Wordle")
    print("You have to guess a 5 letter word in 6 tries")
    print("If a letter is in the word and in the correct spot it will be shown in Green")
    print("Example - " + color.GREEN + color.BOLD + "G" +  color.END + "UESS")
    print("If a letter is in the word and not in the correct spot it will be shown in Yellow")
    print("Example - GU" + color.YELLOW + color.BOLD + "E" +  color.END + "SS")
    
# This function will take the guess as an input and check if it is a valid 
# All caps 5 letter string and return the string to the main functuon
def getGuess(validwords):
    guess = input("Guess: ")
    if len(guess) != 5:
        print("Enter a 5 letter word only")
    elif (not guess.islower() and not guess.isupper()) or guess.islower():
        print("Enter all letters capital")
    elif guess.upper() not in validwords:
        print ("Guess must be a valid word")
    else:
        return 1,guess
    return 0, None

# Function will find out positon of the character in the word
def findall(WORD, GUESS_char):
    positions = []
    for i in range(5):
        if GUESS_char == WORD[i]:
            positions.append(i)
    return positions

def getres(WORD, GUESS):
    res = ['#','#','#','#','#']
    pos = set()
    # Make the list index for letter match as *
    for i in range(5):
        if(WORD[i] == GUESS[i]):
            res[i] = '*'
            pos.add(i)
    # Make the list in index for letter found in word as -
    for i in range(5):
        if GUESS[i] in WORD and res[i] != '*' :
            positions = findall(WORD, GUESS[i])
            for fpos in positions:
                if fpos not in pos:
                    res[i] = '-'
                    pos.add(i)
                    break
    return res

def printguess(res, GUESS):
    for i in range(5):
        if(res[i]=='#'):
            print(GUESS[i], end = "")
        elif(res[i]=='*'):
            print(color.GREEN + GUESS[i] + color.END, end = "")
        else:
            print(color.YELLOW + GUESS[i] + color.END, end = "")
    print("\n")

#Main Method
if __name__ == '__main__':
    
    #Input the name of the user
    name = input("\nEnter your UserName :\n")
    # instantiate an object of the User class and call the greet function
    player = User(name)
    
    rules(player);
    
    newlist = []
    with open('WordList.txt','r') as file:   
        for line in file:
            # reading each word     
            for word in line.split():
                newlist.append(word.upper())
    validwords = []           
    with open('AllowedGuesses.txt','r') as file:   
        for line in file:
            # reading each word     
            for word in line.split():
                validwords.append(word.upper())
                
    # list compression to filter out all 5 letter words from list and make them upper case
    wordList = [x.upper() for x in newlist if len(x) == 5]
    # dictionary compression to create a dictionary of word is to vowel count of the word
    word_dict = {x: countvowels(x) for x in wordList}
    
    # The below snippet will return a random word according to the difficulty selected, 
    # 1 will return a word with many vowels 
    # and 2 will return a word with least vowels
    difficulty = input("\nEnter \n1 for Easy \n2 for Hard\nAnything Else for Random :\n")
    flist = []
    c = Counter(word_dict)
    my_keys = []
    if(difficulty == "1"):
        my_keys = sorted(word_dict, key=word_dict.get, reverse=True)[:100]
        WORD = random.choice(my_keys)
    elif(difficulty == "2"):
        my_keys = sorted(word_dict, key=word_dict.get)[:100]
        WORD = random.choice(my_keys)
    else:
        WORD = random.choice(wordList)
    
    #print(WORD)
    num = 0
    try:
        while num<6:
            i,GUESS = getGuess(validwords);
            if(i == 1):
                res = getres(WORD,GUESS)
                num += 1
                printguess(res,GUESS)
            if WORD == GUESS:
                print("You won! It took you %s guesses."%num)
                quit()
        print("\n" + color.BOLD + "Well Tried!" + color.END)
        print("Correct answer was - " + color.BOLD + WORD + color.END + "\n")
    except KeyboardInterrupt:
        quit()