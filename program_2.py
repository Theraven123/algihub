from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout


app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('program_1')
my_win.move(900, 70)
my_win.resize(400, 200)
my_win.show()

line = QHBoxLayout()
title = QLabel('P E B I S')
line.addWidget(title, alignment=Qt.AlignCenter)

my_win.setLayout(line)
app.exec_()