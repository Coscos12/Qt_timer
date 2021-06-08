import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.counter5 = 0
        self.counter6 = 0


        self.flag1 = False
        self.flag2 = False
        self.flag3 = False
        self.flag4 = False
        self.flag5 = False
        self.flag6 = False

        self.setWindowTitle('second window')
        self.setFixedWidth(500)
        self.setStyleSheet("""
            QLineEdit{
                font-size: 30px
            }
            QPushButton{
                font-size: 30px
            }
            """)
        mainLayout = QVBoxLayout()

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        mainLayout.addWidget(self.input1)
        mainLayout.addWidget(self.input2)

        self.closeButton = QPushButton('Close')
        self.closeButton.clicked.connect(self.close)
        mainLayout.addWidget(self.closeButton)

        self.setLayout(mainLayout)

    def displayInfo(self):
        self.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setFixedWidth(800)

        self.secondWindow = SecondWindow()

        mainLayout = QVBoxLayout()
        self.setStyleSheet("""
            QLineEdit{height: 40px; font-size: 30px}
            QLabel{font-size: 30px}
        """)

        self.name = QLineEdit()
        self.age = QLineEdit()
        mainLayout.addWidget(QLabel('Name:'))
        mainLayout.addWidget(self.name)
        mainLayout.addWidget(QLabel('Age:'))
        mainLayout.addWidget(self.age)

        self.Confirm = QPushButton('Confirm')
        self.Confirm.setStyleSheet('font-size: 30px')
        self.Confirm.clicked.connect(self.passingInformation)
        mainLayout.addWidget(self.Confirm)

        self.setLayout(mainLayout)

    def passingInformation(self):
        self.secondWindow.input1.setText(self.name.text())
        self.secondWindow.input2.setText(self.age.text())
        self.secondWindow.displayInfo()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = MainWindow()
#     demo.show()
#     sys.exit(app.exec_())