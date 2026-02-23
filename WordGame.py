#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter.upper() in word.upper() #check if letter is in the word

    

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return letter.upper() == word[spot].upper() #check if letter is in the right spot

def rateGuess(myGuess, word):
    result = ""
    myGuess = myGuess.upper()
    word = word.upper()

    for i in range(5):
        if inSpot(myGuess[i], word, i):
            result += myGuess[i].upper() # correct spot - captial letter
        elif inWord(myGuess[i], word):
            result += myGuess[i].lower() # correct letter, wrong spot - lowercase letter
        else:
            result += "*" #letter not in word
    return result
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    
    for i in range(6):
        guess = input("Enter a 5-letter guess: ")

        feedback = rateGuess(guess, todayWord)
        print("Results: ", feedback)
        if guess.lower() == todayWord:
            print("Great job, you guessed it!")
            break
    else:
        print("Out of guesses, better luck next time. Today's word was: ", todayWord)

    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
