#! python3

"""
This program shows a confirmation message box when we click on the close button of the application window
"""
import sys
import PyQt5
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

   def __init__(self):
      super().__init__()
      
      self.initUI()
      
   def initUI(self):

      self.setGeometry(300, 300, 250, 150)
      self.setWindowTitle('Message Box')
      self.show()

   def closeEvent(self, event):

      reply = QMessageBox.question(self, 'Message', "Are you sure you wish to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
      
      if reply == QMessageBox.Yes:
         event.accept()
      else:
         event.ignore()
         
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
   main()