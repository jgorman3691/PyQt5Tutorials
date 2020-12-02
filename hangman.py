#! python3

from Tkinter import *
from ttk import *
from random import *
word = 0
wordLength = 0
clue = 0

linux = [
"gnu",
"kernel",
"mutex",
"penguin",
"ubuntu",
"debian",
"mint"
]
recovery = [
"steps",
"traditions",
"keytags",
"literature",
"sponsor",
"service",
"spirituality"
]
math = [
"add",
"subtract",
"multiply",
"divide",
"proof",
"matrix",
"axiom"
]
winter = [
"cold",
"snow",
"ice",
"white",
"wind",
"icicle",
"blue"
]
food = [
"eggs",
"bagel",
"taco",
"empanada",
"apple",
"chicken",
"cake"
]
choices = {
1 : linux,
2 : recovery,
3 : math,
4 : winter,
5 : food
}
Topics = {
"Choices" : choices,
"Linux": linux,
"Recovery" : recovery,
"Mathematics" : math,
"Winter" : winter,
"Food" : food
}

def gui():
   global word, wordLength, clue
   dictionary = categories()
   word = choice(dictionary)
   wordLength = len(word)
   clue = wordLength * ["_"]
   tries = 7

   def hangedman(hangman):
      graphic = [
   """

       +-------+
       |       
       |
       |
       |
       |
    ===============
    """,
    """

       +-------+
       |       |
       |       
       |
       |
       |
    ===============
    """,
    """

       +-------+
       |       |
       |       O
       |       
       |
       |
    ===============
    """,
    """

       +-------+
       |       |
       |       O
       |       |
       |
       |
    ===============
    """,
    """

       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ===============
    """,
    """

       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ===============
    """,
    """

       +-------+
       |       |
       |       O
       |      -|-
       |      /
       |
    ===============
    """,
    """

       +-------+
       |       |
       |       O
       |      -|-
       |      / \
       |
    ===============
    """
    ]
      graphicSet = graphic[hangman]
      hmGraphic.set(graphicSet)

   def categories():
      categoryNumber = 0
      while categoryNumber == 0:
         print("Please choose a category:")
         print("1: Linux")
         print("2: Recovery")
         print("3: Mathematics")
         print("4: Winter")
         print("5: Food")
         print("Enter a number:")
         categoryNumber = input()
         if categoryNumber not in choices.keys():
            print("Please choose a number from the list.")
         else:
            given = random.choice(Topics[choices][categoryNumber].value())

   def game():
      lettersWrong = incorrectGuesses.get()
      letter = guessLetter()
      firstIndex = word.find(letter)
      if firstIndex == -1:
         lettersWrong. += 1
         incorrectGuesses.set(lettersWrong)
      else:
         for i in range(wordLength):
            if letter == word[i]:
               clue[i] == letter
      hangedman(lettersWrong)
      clueSet = " ".join(clue)
      wordOutput.set(clueSet)
      if lettersWrong == tries:
         resultText = "Game Over.  The word was " + word
         resultSet.set(resultText)
         newScore = computerScore.get()
         newScore += 1
         computerScore.set(newScore)
      if "".join(clue) == word:
         resultText = "You win!  The word was " + word
         resultSet.set(resultText)
         newScore = playerScore.get()
         newScore += 1
         playerScore.set(newScore)

   def guessLetter():
      letter = letterGuess.get()
      letter.strip()
      letter.lower()
      return letter

   def resetGame():
      global word, wordLength, clue
      incorrectGuesses.set(0)
      hangedman(0)
      resultSet.set("")
      letterGuess.set("")
      word = choice(dictionary)
      wordLength = len(word)
      clue = wordLength * ["_"]
      newClue = " ".join(clue)
      wordOutput.set(newClue)

if __name__ == '__main__':
   gui()