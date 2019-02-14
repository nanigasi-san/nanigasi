import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("I Love Megane.")
w.setGeometry(50,50,500,300)
w.show()
app.exec()
