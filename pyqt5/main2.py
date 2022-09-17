from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('испытай удачу, друг!')
window.resize(800, 400)

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')

layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()

layoutH1.addWidget(button1, alignment= Qt.AlignLeft)
layoutH1.addWidget(button2, alignment= Qt.AlignRight)
layoutH2.addWidget(button3, alignment= Qt.AlignCenter)
layoutH3.addWidget(button4, alignment= Qt.AlignLeft)
layoutH3.addWidget(button5, alignment= Qt.AlignRight)

layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
layoutV.addLayout(layoutH4)
layoutV.addLayout(layoutH5)
window.setLayout(layoutV)

window.show()
app.exec_()