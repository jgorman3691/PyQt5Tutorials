#! python3

import sys, PyQt5
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):

   def __init__(self):
      super().__init__()
      
      self.initUI()
      
   def initUI(self):

      self.statusbar = self.statusBar()
      self.statusbar.showMessage('Ready')
      
      menubar = self.menuBar()
      viewMenu = menubar.addMenu('View')

      viewStatAct = QAction('View Status Bar', self, checkable=True)
      viewStatAct.setStatusTip('View the status bar')
      viewStatAct.setChecked(True)
      viewStatAct.triggered.connect(self.toggleMenu)
      
      viewMenu.addAction(viewStatAct)

      self.setGeometry(300, 300, 300, 200)
      self.setWindowTitle('Check Menu')
      self.show()
      
   def toggleMenu(self, state):
      if state:
         self.statusbar.show()
      else:
         self.statusbar.hide()
         
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()