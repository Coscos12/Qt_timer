from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QColor


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.places = [0, 180, 270, 360, 450, 540, 630]
        self.new_places = [0, 180, 270, 360, 450, 540, 630]
        self.path =''
        self.font = QtGui.QFont()
        self.color = QColor(0, 0, 0)
        self.font.setFamily("Arial")
        self.font.setPointSize(24)
        self.colors = [1, '#87cefa', '#ee82ee', '#ff0000', '#ffff00', '#0064ff','#00ff00']

        for i in range(1, 7):
            setattr(self, f"counter{i}", 0)
            setattr(self, f"flag{i}", False)
            setattr(self, f"label{i}", QLabel(self))
            getattr(self, f"label{i}").setEnabled(True)
            getattr(self, f"label{i}").setFont(self.font)
            # getattr(self, f"label{i}").setFrameShape(QtWidgets.QFrame.Box)
            # getattr(self, f"label{i}").setLineWidth(2)
            getattr(self, f"label{i}").setGeometry(QtCore.QRect(1700, self.places[i], 150, 50))
            getattr(self, f"label{i}").setObjectName(f"label{i}")
            # getattr(self, f"label{i}").setStyleSheet("background-color: rgb(255,255,255, 75%);")
            setattr(self, f"textBrowser{i}", QLabel(self))
            getattr(self, f"textBrowser{i}").setEnabled(True)
            getattr(self, f"textBrowser{i}").setGeometry(QtCore.QRect(50, self.places[i], 1000, 80))
            getattr(self, f"textBrowser{i}").setFont(self.font)
            # getattr(self, f"textBrowser{i}").setFrameShape(QtWidgets.QFrame.Box)
            # getattr(self, f"textBrowser{i}").setLineWidth(2)
            getattr(self, f"textBrowser{i}").setObjectName(f"textBrowser{i}")
            # getattr(self, f"textBrowser{i}").setStyleSheet("background-color: rgb(255,255,255, 75%);")
            # getattr(self, f"textBrowser{i}").setStyleSheet("QWidget { color: rgb(255,255,255);  }")

        self.label_header = QLabel(self)
        self.label_header.setEnabled(True)
        # self.label_header.setFrameShape(QtWidgets.QFrame.Box)
        # self.label_header.setLineWidth(0)
        self.label_header.setGeometry(QtCore.QRect(560, 30, 800, 80))
        self.label_header.setObjectName(f"label_header")
        # self.label_header.setStyleSheet("background-color: rgb(255,255,255, 75%);")

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

        self.timer.start(10)
        for i in range(1, 7):
            setattr(self, f"flag{i}", True)

    def Stop(self):
         self.timer.stop()

    def Reset(self):
        for i in range(1, 7):
            setattr(self, f"counter{i}", 0)
            setattr(self, f"flag{i}", False)
        self.places = [0, 180, 270, 360, 450, 540, 630]
        self.new_places = [0, 180, 270, 360, 450, 540, 630]
        self.settingText()
        self.refreshing()

    def visiable(self):
        oImage = QImage(f'{self.path}')
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)
        self.showMaximized()
        self.label_header.setFont(self.font)
        for i in range(1, 7):
            # getattr(self, f"label{i}").setFont(self.font)
            getattr(self, f"textBrowser{i}").setFont(self.font)
            getattr(self, f"textBrowser{i}").setStyleSheet("QWidget {color: %s; }" % self.color.name())
            getattr(self, f"label{i}").setStyleSheet("QWidget { color: %s; }" % self.colors[i])
        self.label_header.setStyleSheet("QWidget {color: %s; }" % self.color.name())

    def refreshing(self):
        for i in range(1, 7):
            getattr(self, f"label{i}").setGeometry(QtCore.QRect(1700, self.new_places[self.places.index(self.new_places[i])], 150, 50))
            getattr(self, f"textBrowser{i}").setGeometry(QtCore.QRect(50, self.new_places[self.places.index(self.new_places[i])], 1000, 80))


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
