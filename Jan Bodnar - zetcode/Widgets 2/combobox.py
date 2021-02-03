#! python3

import sys, PyQt5
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication

class Example(QWidget):
   def __init__(self):
      super().__init__()

      self.initUI()
      
   def initUI(self):
      
      self.label = QLabel('Ubuntu', self)
      
      combo = QComboBox(self)
      combo.addItem('Ubuntu')
      combo.addItem('Debian')
      combo.addItem('Kali')
      combo.addItem('Mandriva')
      combo.addItem('Fedora')
      combo.addItem('Arch')
      combo.addItem('Gentoo')
      
      combo.move(50, 50)
      self.label.move(50, 200)
      
      combo.activated[str].connect(self.onActivated)
      
      self.setGeometry(300, 300, 450, 400)
      self.setWindowTitle('QComboBox')
      self.show()
      
   def onActivated(self, text):
      self.label.setText(text)
      self.label.adjustSize()
      
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()