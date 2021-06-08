import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QTextCursor




class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.places = [0, 120, 210, 300, 390, 480, 570]
        self.new_places = [0, 120, 210, 300, 390, 480, 570]
        self.path =''
        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(24)

        for i in range(1, 7):
            # getattr(self, f"label{i}").setEnabled(True)
            setattr(self, f"counter{i}", 0)
            setattr(self, f"flag{i}", False)
            setattr(self, f"label{i}", QLabel(self))
            getattr(self, f"label{i}").setEnabled(True)
            getattr(self, f"label{i}").setFont(self.font)
            getattr(self, f"label{i}").setFrameShape(QtWidgets.QFrame.Box)
            getattr(self, f"label{i}").setLineWidth(2)
            getattr(self, f"label{i}").setGeometry(QtCore.QRect(1700, self.places[i], 150, 50))
            getattr(self, f"label{i}").setObjectName(f"label{i}")
            setattr(self, f"textBrowser{i}", QLabel(self))
            getattr(self, f"textBrowser{i}").setEnabled(True)
            getattr(self, f"textBrowser{i}").setGeometry(QtCore.QRect(50, self.places[i], 1000, 80))
            getattr(self, f"textBrowser{i}").setFont(self.font)
            getattr(self, f"textBrowser{i}").setFrameShape(QtWidgets.QFrame.Box)
            getattr(self, f"textBrowser{i}").setLineWidth(2)
            getattr(self, f"textBrowser{i}").setObjectName(f"textBrowser{i}")

        self.label1.setStyleSheet("background-color: rgb(135, 206,250);")
        self.label2.setStyleSheet("background-color: rgb(238, 130, 238);")
        self.label3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label5.setStyleSheet("background-color: rgb(0, 100, 255);")
        self.label6.setStyleSheet("background-color: rgb(0, 255, 0);")

        self.textBrowser1.setStyleSheet("background-color: rgb(135, 206,250);")
        self.textBrowser2.setStyleSheet("background-color: rgb(238, 130, 238);")
        self.textBrowser3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.textBrowser4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.textBrowser5.setStyleSheet("background-color: rgb(0, 100, 255);")
        self.textBrowser6.setStyleSheet("background-color: rgb(0, 255, 0);")

        self.setWindowTitle('Icon')
        self.text1 = str(self.counter1 / 100)
        self.text2 = str(self.counter2 / 100)
        self.text3 = str(self.counter3 / 100)
        self.text4 = str(self.counter4 / 100)
        self.text5 = str(self.counter5 / 100)
        self.text6 = str(self.counter6 / 100)


        self.label1.setText(self.text1)
        self.label2.setText(self.text2)
        self.label3.setText(self.text3)
        self.label4.setText(self.text4)
        self.label5.setText(self.text5)
        self.label6.setText(self.text6)


    def Start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(10)
        for i in range(1, 7):
            setattr(self, f"flag{i}", True)
        print(self.flag1)

    def Stop(self):
         self.timer.stop()

    def Reset(self):
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.counter5 = 0
        self.counter6 = 0
        self.places = [0, 120, 210, 300, 390, 480, 570]
        self.new_places = [0, 120, 210, 300, 390, 480, 570]
        self.refreshing()
        self.settingText()

    def visiable(self):
        oImage = QImage(f'{self.path}')
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)
        self.showMaximized()

    def refreshing(self):
        for i in range(1, 7):
            getattr(self, f"label{i}").setGeometry(QtCore.QRect(1700, self.new_places[self.places.index(self.new_places[i])], 150, 50))
            getattr(self, f"textBrowser{i}").setGeometry(QtCore.QRect(50, self.new_places[self.places.index(self.new_places[i])], 1000, 80))
        print("refreshing done")

    def showTime(self):
        if self.flag1:
            self.counter1 += 1
        if self.flag2:
            self.counter2 += 1
        if self.flag3:
            self.counter3 += 1
        if self.flag4:
            self.counter4 += 1
        if self.flag5:
            self.counter5 += 1
        if self.flag6:
            self.counter6 += 1
        self.settingText()
        # counter +=1
        # print(self.counter1)

    def settingText(self):
        self.text1 = str(self.counter1 / 100)
        self.text2 = str(self.counter2 / 100)
        self.text3 = str(self.counter3 / 100)
        self.text4 = str(self.counter4 / 100)
        self.text5 = str(self.counter5 / 100)
        self.text6 = str(self.counter6 / 100)
        # # showing text
        self.label1.setText(self.text1)
        self.label2.setText(self.text2)
        self.label3.setText(self.text3)
        self.label4.setText(self.text4)
        self.label5.setText(self.text5)
        self.label6.setText(self.text6)



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.showMaximized()
#     sys.exit(app.exec_())