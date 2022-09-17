from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget
main_win.setWindowTitle('Моё первое приложение')
main_win.resize(400,200)
main_win.move(900,70)


text = QLabel('Hello world')
line = QVBoxLayout()

line.addWidget(text, alignment = Qt.AlignCenter)
main_win.setLayout(line)

main_win.show()
app.exec_()