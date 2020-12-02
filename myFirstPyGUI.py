#! python3
from Tkinter import *

import rockPaperScissors
import hangman
import pokerDice

root = Tk()
root.title("Jed's Micro and Mini Games Collection")

mainFrame = Frame(root, height = 200, width = 500)
mainFrame.pack_propagate(0)
mainFrame.pack(padx = 5, pady = 5)

intro = Label(mainFrame, text="""
Welcome to my Games Collection!
Please select one of the following games to play:
""")
intro.pack(side = TOP)

rpsButton = Button(mainFrame, text = "Rock, Paper, Scissors", command = rockPaperScissors.gui)
rpsButton.pack()

hmButton = Button(mainFrame, text = "Hangman", command = hangman.start)
hmButton.pack()

pdButton = Button(mainFrame, text = "Poker Dice", command = pokerDice.start)

exitButton = Button(mainFrame,text="Quit",command=root.destroy)
exitButton..pack(side = BOTTOM)

root.mainloop()

