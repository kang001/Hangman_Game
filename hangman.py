#Sources used: https://inventwithpython.com/chapter9.html
#http://stackoverflow.com/questions/32222025/hangman-game-in-python-how-to-replace-blanks-with-guessed-letters
#http://codereview.stackexchange.com/questions/95997/simple-game-of-hangman

#modified this code to read the words from a text file


#added exception handling for user input, so they cannot put in characters or numbers

#This is a game of hangman. The program picks a random word from a list of words
#The user then has to guess a letter that they might think will be in the words
#The user has a certain number of guesses before the 'man is hanged'
#If the uses goes over the amount of guesses, without completing the word
#then the user has lost the game

import random
#here make a list of random words and split it
HANGMAN = [''' #used this formatting from the source listed above to display the hangman
   +---+
   |   |
       |
       |
       |
       |
===========''','''
   +---+
   |   |
   O   |
       |
       |
       |
===========''','''
   +---+
   |   |
   O   |
   |   |
       |
       |
===========''','''
   +---+
   |   |
   O   |
  /|   |
       |
       |
===========''','''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
===========''','''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
===========''','''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
G A M E| O V E R
===========''']
#this code will open up the words from the wordList
#once the string of words is read in, it is split and held into the variable words
fileo = open("wordList.txt", "r").read()
words = fileo.split()
#print("List of words:\n",listWords)
#words = 'lotion, snow, noodles, bottle, unicorn'.split()

#adding in this variable allows me to control better how many guesses the user has 
amountOfGuesses = 6

def GetRandomWord(wordList):
    #this function will return a a selected index from the list of words read in
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def DisplayBoard(HANGMAN, missedLetters, correctLetters, secretWord):
    print(HANGMAN[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

blanks = '_'* len(secretWord)

for i in range(len(secretWord)): #replace blanks with correctly guessed letters
    if secretWord[i] in correctLetters:
        blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

for letters in blanks:
    print(letter, end=' ')
print()
#error handling
def GetGuess(alreadyGuessed):
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter!')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter')
        else:
            return guess
def PlayAgain():
    print('Do you want to play again? (Y/N)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ' '
correctLetters = ' '
secretWord = GetRandomWord(words)
endGame = False

while amountOfGuesses < 0: #this part was modified to  take continue running while the amount of guesses was still less than 6
    DisplayBoard(HANGMAN, missedLetters, correctLetters, secretWord)
    guess = GetGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('The secret word is "' + secretWord + '"! You have won!')
            else:
                missedLetters = missedLetter + guess

                if len(missedLetters) > amountOfGuesses: #this checks if the amount of missed letters is more than the amount of guesses, the user loses the game
                    DisplayBoard(HANGMAN, missedLetters, correctLetters, secretWord)
                    print('You ran out of guesses\n' + 'The word was' + secretWord)
                    endGame = True
            if endGame:
                if playAgain():
                    missedLetters = ' '
                    correctLetters = ' '
                    endGame = False
                    secretWord = getRandomWord(words)
                else:
                    break
fileo.close()
