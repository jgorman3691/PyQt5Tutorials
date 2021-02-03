#! python3

import sys, PyQt5
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap

class Example(QWidget):

   def __init__(self):
      super().__init__()
      
      self.initUI()
      
   def initUI(self):
      hbox = QHBoxLayout(self)
      pixmap = QPixmap('sid.jpg')

      label = QLabel(self)
      label.setPixmap(pixmap)
      
      hbox.addWidget(label)
      self.setLayout(hbox)
      
      self.move(300, 200)
      self.setWindowTitle('Sid')
      self.show()
      
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()