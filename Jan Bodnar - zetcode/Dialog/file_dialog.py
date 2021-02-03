#! python3

import sys, PyQt5
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
   
   def __init__(self):
      super().__init__()
      
      self.initUI()
      
   def initUI(self):
      self.textEdit = QTextEdit()
      self.setCentralWidget(self.textEdit)
      self.statusBar()
      
      openFile = QAction(QIcon('open.png'), 'Open', self)
      openFile.setShortcut('Ctrl+O')
      openFile.setStatusTip('Open a new File')
      openFile.triggered.connect(self.showDialog)
      
      menubar = self.menuBar()
      fileMenu = menubar.addMenu('&File')
      fileMenu.addAction(openFile)
      
      self.setGeometry(300, 300, 550, 450)
      self.setWindowTitle('File Dialog')
      self.show()
      
   def showDialog(self):
      
      home_dir = str(Path.home())
      fname = QFileDialog.getOpenFileName(self, 'Open File', home_dir)

      if fname[0]:
         with open(fname[0], 'r') as f:
            data = f.read()
            self.textEdit.setText(data)

def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()