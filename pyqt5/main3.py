from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle('испытай удачу, друг!')
window.resize(600, 500)

button1 = QLabel('PHP')
button2 = QLabel('JavaScript')
button3 = QLabel('Python')
button4 = QLabel('Pascal')
button5 = QLabel('SQL')
button6 = QLabel('C++')

layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(button1, alignment= Qt.AlignCenter)
layoutH1.addWidget(button2, alignment= Qt.AlignCenter)
layoutH2.addWidget(button3, alignment= Qt.AlignCenter)
layoutH2.addWidget(button4, alignment= Qt.AlignCenter)
layoutH3.addWidget(button5, alignment= Qt.AlignCenter)
layoutH3.addWidget(button6, alignment= Qt.AlignCenter)

layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)

window.show()
app.exec_()