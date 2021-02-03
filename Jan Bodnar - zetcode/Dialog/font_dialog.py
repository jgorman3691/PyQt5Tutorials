#! python3

import sys, PyQt5
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog, QApplication

class Example(QWidget):
   
   def __init__(self):
      super().__init__()
      
      self.initUI()
      
   def initUI(self):
      vbox = QVBoxLayout()
      
      btn = QPushButton('Dialog', self)
      btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
      btn.move(20, 20)
      
      vbox.addWidget(btn)
      
      btn.clicked.connect(self.showDialog)
      
      self.label = QLabel('Knowledge only matters', self)
      self.label.move(130, 20)
      
      vbox.addWidget(self.label)
      self.setLayout(vbox)
      
      self.setGeometry(300, 300, 450, 300)
      self.setWindowTitle('Font Dialog')
      self.show()
      
   def showDialog(self):
      font, ok = QFontDialog.getFont()
      if ok:
         self.label.setFont(font)
      
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()