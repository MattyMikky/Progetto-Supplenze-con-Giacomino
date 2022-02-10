import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *

widgets = {
    "logo": [],
    "button": []    
}

app = QApplication(sys.argv)
Window = QWidget()
Window.setWindowTitle("Programma per le supplenze")
Window.setFixedWidth(1000)
Window.move(500, 100)
Window.setStyleSheet("Background: #FFFFFF; ")

grid = QGridLayout()


Window.setLayout(grid)




def frame1():

  #Display logo
  image = QPixmap("logotrivia.png")
  logo = QLabel()
  logo.setPixmap(image)
  logo.setAlignment(QtCore.Qt.AlignCenter)
  logo.setStyleSheet("margin-top: 400px;")
  widgets["logo"].append(logo)
  

  #button widget
  button = QPushButton("Inserisci il giorno")
  button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
  button.setStyleSheet(
      "*{border: 6px solid '#787878';" +
      "border-radius: 45px;" +
      "font-size: 40px;" +
      "color: 'Black';" +
      "padding: 20px 0;" +
      "margin: 50px 250px;}" +
      "*:hover{background: '#787878';}"
  )
  widgets["button"].append(button)

  grid.addWidget(widgets["logo"] [-1], 0, 0)
  grid.addWidget(widgets["button"] [-1], 1, 0)

def frame2():
  score = QLabel("80")
  score.setAlignment(QtCore.Qt.AlignRight)
  score.setStyleSheet(
      "font-size: 34px;" +
      "color: 'White';" +
      "padding: 20px 15px;" +
      "margin: 200px 20px;" +
      "background: '#0FEEE6';" +
      "border: 1px solid '#FEEE6'" +
      "border-radius: 40px;"
  )

frame1()

Window.show()
sys.exit(app.exec_())
