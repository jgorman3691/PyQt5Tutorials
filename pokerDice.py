#! python3

import random
from itertools import groupby

from Tkinter import *
from ttk import *

dice = 0

def roll(rollNumber):
   numbers = range(1,7)
   dice = range(rollNumber)
   iterations = 0
   while iterations < rollNumber:
      iterations += 1
      dice[iterations - 1] = random.choice(numbers)
   return dice

def hand(dice):
   diceHand = [len(list(group)) for key, group in groupby(dice)]
   diceHand.sort(reverse=True)
   straight1 = [1, 2, 3, 4, 5]
   straight2 = [2, 3, 4, 5, 6]
   if dice == straight1 or dice == straight2:
      return "A straight!"
   elif diceHand[0] == 5:
      return "Five of a kind!"
   elif diceHand[0] == 4:
      return "Four of a kind!"
   elif diceHand[0] == 3:
      if diceHand[1] == 2:
         return "A full house!"
      else:
         return "Three of a kind"
   elif diceHand[0] == 2:
      if diceHand[1] == 2:
         return "Two pair."
      else:
         return "One pair."
   else:
      return "A high card"

def gui():
   global dice
   dice = roll(5)
   dice.sort()
   nine = 1
   ten = 2
   jack = 3
   queen = 4
   king = 5
   ace = 6
   names =
   {
   nine : "9",
   ten : "10",
   jack : "J",
   queen : "Q",
   king : "K",
   ace : "A"
   }
   result = "You have " + hand(dice)

   def game():
      throws()

def start():
   print("The computer will help you with throwing your 5 dice.")
   throws()
   return playAgain()

   def throws():
      global dice
      dice1_Check = dice1.get()
      dice2_Check = dice2.get()
      dice3_Check = dice3.get()
      dice4_Check = dice4.get()
      dice5_Check = dice5.get()
      diceRerolls = [dice1_Check, dice2_Check, dice3_Check, dice4_Check, dice5_Check]
      for i in range(len(diceRerolls)):
         if 0 in diceRerolls:
            diceRerolls.remove(0)
         if len(diceRerolls) == 0:
            result = "You finish with " + hand(dice)
            handOutput.set(result)
         else:
            rollNumber = len(diceRerolls)
            numberRerolls = roll(rollNumber)
            diceChanges = range(len(diceRerolls))
            iterations = 0
            while iterations < rollNumber:
               iterations++
               replacement = numberRerolls[iterations - 1]
               dice[diceChanges[iterations - 1]] = replacement
            dice.sort()
            newDiceList = [0, 0, 0, 0, 0]
            for i in range(len(dice)):
               newDiceList[i] = names[dice[i]]
            finalDice = " ".join(newDiceList)
            diceOutput.set(finalDice)
            finalResult = "You finish with " + hand(dice)
            handOutput.set(finalResult)

   def reset_game():
      global dice
      dice = roll(5)
      dice.sort()
      for i in range(len(dice)):
         emptyDice[i] = names[dice[i]]
      firstDice = " ".join(emptyDice)
      diceOutput.set(firstDice)
      result = "You have " = hand(dice)
      handOutput.set(result)

   pdWindow = Toplevel()
   pdWindow.title("Poker Dice")
   diceOutput = StringVar()
   emptyDice = [0, 0, 0, 0, 0]
   for i in range(len(dice)):
      emptyDice[i] = names[dice[i]]
   firstDice = " ".join(emptyDice)
   diceOutput.set(firstDice)
   handOutput = StringVar()
   handOutput.set(result)
   dice1 = IntVar()
   dice2 = IntVar()
   dice3 = IntVar()
   dice4 = IntVar()
   dice5 = IntVar()
   resultSet = StringVar()
   playerScore = IntVar()
   computerScore = IntVar()

   pdFrame = Frame(pdWindow, padding = '3 3 12 12', width = 300)
   pdFrame.grid(column = 0, row = 0, sticky=(N,W,E,S))
   pdFrame.rowconfigure(0, weight = 1)
   Label(pdFrame, text='Dice').grid(column = 3, row = 1)
   Label(pdFrame, textvariable = diceOutput).grid(column = 3, row = 2)
   Label(pdFrame, textvariable = handOutput).grid(column = 3, roow = 3)
   Label(pdFrame, text="Dice to Reroll?").grid(column = 3, row = 4)
   reroll1 = Checkbutton(pdFrame, text = "1", variable = dice1, onValue = 1, offValue = 0).grid(column = 1, row = 5)
   reroll2 = Checkbutton(pdFrame, text = "2", variable = dice2, onValue = 2, offValue = 0).grid(column = 2, row = 5)
   reroll3 = Checkbutton(pdFrame, text = "3", variable = dice3, onValue = 3, offValue = 0).grid(column = 3, row = 5)
   reroll4 = Checkbutton(pdFrame, text = "4", variable = dice4, onValue = 4, offValue = 0).grid(column = 4, row = 5)
   reroll5 = Checkbutton(pdFrame, text = "5", variable = dice5, onValue = 5, offValue = 0).grid(column = 5, row = 5)
   pdRerollButton = Button(pdFrame, text = "Reroll", command = game).grid(column = 3, row = 6)
   replayButton = Button(pdFrame, text = "Reset", command = resetGame).grid(column = 3, row = 7)

if __name__ == '__main__':
   gui()
