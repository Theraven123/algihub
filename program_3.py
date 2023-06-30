from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('P E B I S')
my_win.move(900, 70)
my_win.resize(400, 200)
my_win.show()
line = QVBoxLayout()
button = QPushButton('dont PUSH')
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)

def show_fun_title():
    fun_title = QLabel('you pushed')
    line.addWidget(fun_title, alignment = Qt.AlignCenter)
    #my_win.setLayout(line) (kosristi ak se ne pokazuje)

button.clicked.connect(show_fun_title)
app.exec_()