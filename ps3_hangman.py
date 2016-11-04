# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\Users\Dhananjay.Pandit-PC\Documents\edX Courses\Introduction to Computer Science and Programming\Week 3\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secret=[]
   
    for letters in secretWord:
        while(letters not in secret):
            secret.append(letters)

    for char in lettersGuessed:
        if char in secret:
            secret.remove(char)

    if secret==[]:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secret=[]
    index=0
    temp=[]
    ans=''
    
    for s in secretWord:
        temp.append('_ ')
   
    for letters in secretWord:
        secret.append(letters)
    
    for char in lettersGuessed:
        while char in secret:
            index=secret.index(char)
            temp[index]=char
            secret.pop(index)
            secret.insert(index,'')

    for t in temp:
        ans+=t
    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha=''
    change=[]
    ans=''
    alpha=string.ascii_lowercase

    for char in alpha:
        change.append(char)

    for letters in lettersGuessed:
        if letters in change:
            change.remove(letters)

    for c in change:
        ans+=c

    return ans
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    mistakesMade=0
    totalGuess=8
    lettersGuessed=[]
    rem=[]
    inc=''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("-------------")
    while(mistakesMade!=8):
        print("You have "+str(totalGuess)+" guesses left.")
        print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
        inc=raw_input("Please guess a letter: ")
        inc=inc.lower()
        lettersGuessed.append(inc)
        if(inc in rem):
            print("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord,lettersGuessed)))
        elif(inc in secretWord):
            print("Good guess: "+str(getGuessedWord(secretWord,lettersGuessed)))
        elif(inc not in secretWord):
            print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord,lettersGuessed)))
            mistakesMade+=1
            totalGuess-=1
        if(isWordGuessed(secretWord,lettersGuessed)==True):
            print("-------------")
            print("Congratulations, you won!")
            break
        print("-------------")
        rem.append(inc)
    if(totalGuess==0):
        print("Sorry, you ran out of guesses. The word was "+str(secretWord))






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
