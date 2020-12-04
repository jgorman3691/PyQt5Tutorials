#! python3

from tkinter import *
from tkinter.ttk import *
import random

def gui():

   rock = 1
   paper = 2
   scissors = 3
   names = {
   rock : 'Rock',
   paper : 'Paper',
   scissors: 'Scissors'
   }
   rules = {
   rock : scissors,
   paper : rock,
   scissors : paper
   }

   def start():
      while game():
         pass

   def playAgain():
      anotherRound.set("Would you like to play again?")


   def game():
      player = playerChoice.get()
      computer = random.randint(1, 3)
      computerChoice.set(names[computer])
      result(player, computer)
      return playAgain()


   def result(player, computer):
      newScore = 0
      if player == computer:
         resultSet.set("Tie Game...")
      else:
         if rules[player] == computer:
            resultSet.set("Your victory is assured...")
            newScore = playerScore.get()
            newScore += 1
            playerScore.set(newScore)
         else:
            resultSet.set("The computer laugh as you realize you've been defeated by a chunk of sparking rock...")
            newScore = computerScore.get()
            newScore += 1
            computerScore.set(newScore)

   rpsWindow = Toplevel()
   rpsWindow.title("Rock, Paper, Scissors")

   playerChoice = IntVar()
   computerChoice = StringVar()
   resultSet = StringVar()
   anotherRound = StringVar()
   playerChoice.set(1)
   playerScore = IntVar()
   computerScore = IntVar()

   rpsFrame = Frame(rpsWindow, padding = '3 3 12 12', width = 300)
   rpsFrame.grid(column=0, row=0, sticky=(N,W,E,S))
   rpsFrame.columnconfigure(0, weight=1)
   rpsFrame.rowconfigure(0, weight=1)

   Label(rpsFrame, text="Player").grid(column=1, row=1, sticky=W)
   Radiobutton(rpsFrame, text="Rock", variable=playerChoice, value=1).grid(column=1, row=2, sticky=W)
   Radiobutton(rpsFrame, text="Paper", variable=playerChoice, value=2).grid(column=1, row=3, sticky=W)
   Radiobutton(rpsFrame, text="Scissors", variable=playerChoice, value=3).grid(column=1, row=4, sticky=W)

   Label(rpsFrame, text="Computer").grid(column=3, row=1, sticky=W)
   Label(rpsFrame, textvariable = computerChoice).grid(column=3, row=3, sticky=W)

   Button(rpsFrame, text="Play", command=start).grid(column=2, row=2)

   Label(rpsFrame, text="Score").grid(column=1, row=5, sticky=W)
   Label(rpsFrame, textvariable=playerScore).grid(column=1, row=6, sticky=W)

   Label(rpsFrame, text="Score").grid(column=3, row=5, sticky=W)
   Label(rpsFrame, textvariable=computerScore).grid(column=3, row=6, sticky=W)

   Label(rpsFrame, textvariable=resultSet).grid(column=2, row=7)

   Label(rpsFrame, text="Play Again?").grid(column = 2, row = 8, sticky=S)
   Label(rpsFrame, textvariable = anotherRound).grid(column = 2, row = 9, sticky=S)
   Button(rpsFrame, text="Play", command = start).grid(column = 1, row = 10, sticky=SW)
   Button(rpsFrame, text="Quit", command = rpsWindow.destroy).grid(column=3, row=10, sticky=SE)

if __name__ == '__main__':
   gui()

if __name__ == '__main__':
   start()