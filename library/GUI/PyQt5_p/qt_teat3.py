import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication

app = QApplication(sys.argv)
w = QWidget()
quit_btn = QPushButton("Quit",w)
quit_btn.move(10,10)

quit_btn.clicked.connect(QCoreApplication.instance().quit)
w.show()
app.exec()
