#! python3

import sys, PyQt5, random
from PyQt5.QtCore import Qt, QtBasicTimer, pyqtSignal
from PyQt5.Gui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QHBoxLayout, QVBoxLayout

class Tetris(QMainWindow):
      def __init__(self):
      super().__init__()

      self.initUI()
      
   def initUI(self):
      # Initiates application UI

      self.tboard = Board(self)
      self.setCentralWidget(self.tboard)
      
      self.statusbar = self.statusBar()
      self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
      
      self.tboard.start()
      
      self.resize(180, 380)
      self.center()
      self.setWindowTitle('Tetris')
      self.show()
   
   def center(self):
      # This function centers the window onto the screen

      screen = QDesktopWidget().screenGeometry()
      size = self.geometry()
      self.move(int((screen.width() - size.width()) /2 ), int((screen.height() - size.height()) / 2))
      
class Board(QFrame):
   msg2Statusbar = pyqtSignal(str)

   BoardWidth = self.w
   BoardHeight = self.h
   Speed = self.s
   
   def __init__(self, parent):
      super().__init__(parent)
      
      w = self.w
      h = self.h
      s = self.s
      
      self.initBoard()
      
   def initBoard(self):
      # Initiates the board

      self.timer = QBasicTimer()k
      self.isWaitingAfterLine = False
      
      self.curX = 0
      self.curY = 0
      self.numLinesRemoved = 0
      self.board = []
      
      self.setFocusPolicy(Qt.StrongFocus)
      self.isStarted = False
      self.isPaused = Fal
      self.clearBoard()
      
   def shapeAt(self, x, y):
      # Determines the shape at the specific position
      
      return self.board[(y * Board.BoardWidth) + x]
   
   def setShapeAt(self, x, y, shape):
      # Puts a shape onto the board
      
      self.board[(y * Board.BoardWidth) + x] = shape

   def squareWidth(self):
      # Returns the width of a single square

      return self.contentsRect().width() // Board.BoardWidth
   
   def squareHeight(self):
      # Returns the height of a single square

      return self.contentsRect().height() // Board.BoardHeight

   def start(self): # Now we start the game
      if self.isPaused:
         return

      self.isStarted = True
      self.isWaitingAfterLine = False
      self.numLinesRemoved = 0
      self.clearBoard()
      
      self.msg2Statusbar.emit(str(self.numLinesRemoved))
      
      self.newPiece()
      self.timer.start(Board.Speed, self)
      
   def pause(self):
      # Pause!
      if not self.isStarted:
         return
      
      self.isPaused = not self.isPaused
      
      if self.isPaused:
         self.timer.stop()
         self.msg2Statusbar.emit("Paused")
      else:
         self.timer.start(Board.Speed, self)
         self.msg2Statusbar.emit(str(self.numLinesRemoved))
      
      self.update()
      
   def paintEvent(self, event):
      # This function paints all the shapes in the game
      painter = QPainter(self)
      rect = self.contentsRect()
      
      boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
      
      for i in range(Board.BoardHeight):
         for j in range(Board.BoardWidth):
            shape = self.shapeAt(j, Board.BoardHeight - i - 1)
            
            if shape != Tetrominoe.NoShape:
               self.drawSquare(painter, rect.left() + j * self.squareWidth(), boardTop + i * self.squareHeight(), shape)
               
      if self.curPiece.shape() != Tetrominoe.NoShape:
         for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.drawSquare(painter, rect.left() + x * self.squareWidth(), boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(), self.curPiece.shape())
            
   def keyPressEvent(self, event):
      # Processes Key Press Events

      if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
         super(Board, self).keyPressEvent(event)
         return

      key = event.key()
      
      if key == Qt.Key_P:
         self.pause()
         return
      
      if self.isPaused:
         return
      elif key -- Qt.Key_Left:
         self.tryMove(self.curPiece, self.curX - 1, self.curY)
      elif key == Qt.Key_right:
         self.tryMove(self.curPiece, self.curX + 1, self.curY)
      elif key == Qt.Key_Down:
         self.trymove(self.curPiece.rotateLeft(), self.curX, self.curY)
      elif key == Qt.Key_Space:
         self.dropDown()
      elif key == Qt.Key_D:
         self.oneLineDown()
      else:
         super(Board, self).keyPressEvent(event)
         
   def timerEvent(self, event):
      # Handles timer events
      if event.timerId() == self.timer.timerId():
         if self.isWaitingAfterLine:
            self.isWaitingAfterLine = False
            self.newPiece()
         else:
            self.oneLineDown()
      else:
         super(Board, self).timerEvent(event)
         
   def ClearBoard(self):
      # Clears out the shapes from the board

      for i in range(Board.BoardHeight * Board.BoardWidth):
         self.board.append(Tetrominoe.NoShape)
         
   def dropDown(self): 
      # Drops the shape down more quickly
      newY = self.curY
      while newY > 0:
         if not self.tryMove(self.curPiece, self.curX, newY - 1):
            break
         newY -= 1
         
      self.pieceDropped()
      
   def oneLineDown(self):
      # Takes a shape one line down
      if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
         self.pieceDropped()
         
   def pieceDropped(self):
      # After dropping the shape, remove full lines nd create a new shape

      for i i n range(4):
         x = self.curX + self.curPiece.x(i)
         y = self.curY - self.curPiece.y(i)
         self.setShapeAt(x, y, self.curPiece.shape())
         
      self.removeFullLines()
      
      if not self.isWaitingAfterLine:
         self.newPiece:
            
   def removeFullLines(self):
      # Removes the full lines from the board
      numFullLines = 0
      rowsToRemove - []
      
      for i in range(Board.BoardHeight):
         n = 0
         for j in range(Board.BoardWidth):
            if not self.shapeAt(j, i) == Tetrominoe.NoShape:
               n = n+1
               
      if n == 10:
         rowsToRemove.append(i)
      
      rowstoRemove.reverse()
      
      for m in rowsToRemove:
         for k in range(m, Board.BoardHeight):
            for l in range(Board.BoardWidth):
               self.setShapeAt(1, k, self.shapeAt(1, k+1))
      
      numFullLines = numFullLines + len(rowsToRemove)
      
      if numFullLines > 0:
         self.numLinesRemoved = self.numLinesRemoved + numFullLines
         self.msg2Statusbar.emit(str(self.numLinesRemoved))
         
         self.isWaitingAfterLine = True
         self.curPiece.setShape(Tetrominoe.NoShape)