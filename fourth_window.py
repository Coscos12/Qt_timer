
from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPalette, QBrush
# import serial
import threading

global ser
seq = []
# global places
places = [0, 30, 120, 210, 300, 390, 480]
new_places = [0, 30, 120, 210, 300, 390, 480]


# ser = serial.Serial(
#     port='COM9',\
#     baudrate=9600, \
#     parity=serial.PARITY_NONE, \
#     stopbits=serial.STOPBITS_ONE, \
#     bytesize=serial.EIGHTBITS, \
#     timeout=0)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # self.texts =[0, textBrowser, textBrowser_2, textBrowser_3, textBrowser_4, textBrowser_5, textBrowser_6]
        # self.labels = [0, labels, labels_2, labels_3, labels_4, labels_5, labels_6]
        self.counter = 0
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.counter5 = 0
        self.counter6 = 0

        # self.flag11 = False
        # self.flag12 = False
        # self.flag13 = False
        # self.flag14 = False
        # self.flag15 = False
        # self.flag16 = False

        self.flag1 = False
        self.flag2 = False
        self.flag3 = False
        self.flag4 = False
        self.flag5 = False
        self.flag6 = False
        # self.t = ser.readline().decode('utf-8')

        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1000, 620)
        oImage = QImage("134.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        MainWindow.setPalette(palette)
        MainWindow.showMaximized()
        # MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Port = QtWidgets.QComboBox(MainWindow)
        self.Port.setGeometry(QtCore.QRect(10, 580, 381, 31))
        self.Port.setObjectName("Port")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(1550, 950, 75, 23))
        self.start_btn.setStyleSheet("background-color: rgb(85, 170, 127)")
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(1660, 950, 75, 23))
        self.stop_btn.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.stop_btn.setObjectName("stop_btn")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(1770, 950, 75, 23))
        self.reset_btn.setStyleSheet("background-color: rgb(255, 202, 0);")
        self.reset_btn.setObjectName("reset_btn")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)

        self.label.setEnabled(True)
        self.label_2.setEnabled(True)
        self.label_3.setEnabled(True)
        self.label_4.setEnabled(True)
        self.label_5.setEnabled(True)
        self.label_6.setEnabled(True)
        #
        self.label.setGeometry(QtCore.QRect(1700, places[1], 150, 50))
        self.label_2.setGeometry(QtCore.QRect(1700, places[2], 150, 50))
        self.label_3.setGeometry(QtCore.QRect(1700, places[3], 150, 50))
        self.label_4.setGeometry(QtCore.QRect(1700, places[4], 150, 50))
        self.label_5.setGeometry(QtCore.QRect(1700, places[5], 150, 50))
        self.label_6.setGeometry(QtCore.QRect(1700, places[6], 150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)

        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)

        self.label.setLineWidth(2)
        self.label_2.setLineWidth(2)
        self.label_3.setLineWidth(2)
        self.label_4.setLineWidth(2)
        self.label_5.setLineWidth(2)
        self.label_6.setLineWidth(2)
        self.label.setObjectName("label")
        self.label_2.setObjectName("label_2")
        self.label_3.setObjectName("label_3")
        self.label_4.setObjectName("label_4")
        self.label_5.setObjectName("label_5")
        self.label_6.setObjectName("label_6")
        self.label.setStyleSheet("background-color: rgb(135, 206,250);")
        self.label_2.setStyleSheet("background-color: rgb(238, 130, 238);")
        self.label_3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_5.setStyleSheet("background-color: rgb(0, 100, 255);")
        self.label_6.setStyleSheet("background-color: rgb(0, 255, 0);")


        self.pause_btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn_1.setGeometry(QtCore.QRect(1500, 40, 75, 23))
        self.pause_btn_1.setObjectName("pause_btn_1")
        self.pause_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn_2.setGeometry(QtCore.QRect(1500, 130, 75, 23))
        self.pause_btn_2.setObjectName("pause_btn_2")
        self.pause_btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn_3.setGeometry(QtCore.QRect(1500, 220, 75, 23))
        self.pause_btn_3.setObjectName("pause_btn_3")
        self.pause_btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn_4.setGeometry(QtCore.QRect(1500, 310, 75, 23))
        self.pause_btn_4.setObjectName("pause_btn_4")
        self.pause_btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn_5.setGeometry(QtCore.QRect(1500, 400, 75, 23))
        self.pause_btn_5.setObjectName("pause_btn_5")
        self.pause_btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn_6.setGeometry(QtCore.QRect(1500, 490, 75, 23))
        self.pause_btn_6.setObjectName("pause_btn_6")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, places[1], 1000, 80))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(font)
        self.textBrowser_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, places[2], 1000, 80))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setFont(font)
        self.textBrowser_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, places[3], 1000, 80))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_3.setFont(font)
        self.textBrowser_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(50, places[4], 1000, 80))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_4.setFont(font)
        self.textBrowser_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(50, places[5], 1000, 80))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_5.setFont(font)
        self.textBrowser_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(50, places[6], 1000, 80))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_6.setFont(font)

        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.serial = QtSerialPort.QSerialPort(
        #     self,
        #     readyRead=self.receive
        # )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stop_btn.setText(_translate("MainWindow", "Стоп"))
        self.start_btn.setText(_translate("MainWindow", "Старт"))
        self.reset_btn.setText(_translate("MainWindow", "Сброс"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.pause_btn_1.setText(_translate("MainWindow", "голубой"))
        self.pause_btn_2.setText(_translate("MainWindow", "розовый"))
        self.pause_btn_3.setText(_translate("MainWindow", "красный"))
        self.pause_btn_4.setText(_translate("MainWindow", "желтый"))
        self.pause_btn_5.setText(_translate("MainWindow", "синий"))
        self.pause_btn_6.setText(_translate("MainWindow", "зеленый"))

        self.add_functions()
        self.check_serial_event()
        # self.refreshing()

    def refreshing(self):
        self.label.setGeometry(QtCore.QRect(1700, new_places[places.index(new_places[1])], 150, 50))
        self.label_2.setGeometry(QtCore.QRect(1700, new_places[places.index(new_places[2])], 150, 50))
        self.label_3.setGeometry(QtCore.QRect(1700, new_places[places.index(new_places[3])], 150, 50))
        self.label_4.setGeometry(QtCore.QRect(1700, new_places[places.index(new_places[4])], 150, 50))
        self.label_5.setGeometry(QtCore.QRect(1700, new_places[places.index(new_places[5])], 150, 50))
        self.label_6.setGeometry(QtCore.QRect(1700, new_places[places.index(new_places[6])], 150, 50))
        self.textBrowser.setGeometry(QtCore.QRect(50, new_places[places.index(new_places[1])], 1000, 80))
        self.textBrowser_2.setGeometry(QtCore.QRect(50, new_places[places.index(new_places[2])], 1000, 80))
        self.textBrowser_3.setGeometry(QtCore.QRect(50, new_places[places.index(new_places[3])], 1000, 80))
        self.textBrowser_4.setGeometry(QtCore.QRect(50, new_places[places.index(new_places[4])], 1000, 80))
        self.textBrowser_5.setGeometry(QtCore.QRect(50, new_places[places.index(new_places[5])], 1000, 80))
        self.textBrowser_6.setGeometry(QtCore.QRect(50, new_places[places.index(new_places[6])], 1000, 80))

    def add_functions(self):
        self.timer = QTimer(self.centralwidget)
        # # adding action to timer
        self.timer.timeout.connect(self.showTime)
        # # update the timer every tenth second
        self.timer.start(10)
        self.start_btn.clicked.connect(lambda: self.Start())
        self.stop_btn.clicked.connect(lambda: self.Stop())
        self.reset_btn.clicked.connect(lambda: self.Reset())
        self.pause_btn_1.clicked.connect(lambda: self.Pause(1))
        self.pause_btn_2.clicked.connect(lambda: self.Pause(2))
        self.pause_btn_3.clicked.connect(lambda: self.Pause(3))
        self.pause_btn_4.clicked.connect(lambda: self.Pause(4))
        self.pause_btn_5.clicked.connect(lambda: self.Pause(5))
        self.pause_btn_6.clicked.connect(lambda: self.Pause(6))
        # self.Port.addItems(lambda :self.serial_ports())

    def visible(self):
        # Dialog1 = QtWidgets.QMainWindow()
        ui1 = Ui_MainWindow()
        ui1.setupUi(Dialog1)
        Dialog1.show()

    def Pause(self, i):
        setattr(self, f"flag{i}", False)
        self.counter += 1
        k = places.pop(places.index(new_places[i]))
        places.insert(self.counter, k)
        self.refreshing()

    def Start(self):
         for i in range(1, 7):
            setattr(self, f"flag{i}", True)

    def Stop(self):
        for i in range(1, 7):
            setattr(self, f"flag{i}", False)

    def Reset(self):
        for i in range(1, 7):
            setattr(self, f"flag{i}", False)
            setattr(self, f"counter{i}", 0)
        self.counter = 0

    def showTime(self):
        # checking if flag is true
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

        # getting text from count
        text1 = str(self.counter1 / 100)
        text2 = str(self.counter2 / 100)
        text3 = str(self.counter3 / 100)
        text4 = str(self.counter4 / 100)
        text5 = str(self.counter5 / 100)
        text6 = str(self.counter6 / 100)
        # showing text
        self.label.setText(text1)
        self.label_2.setText(text2)
        self.label_3.setText(text3)
        self.label_4.setText(text4)
        self.label_5.setText(text5)
        self.label_6.setText(text6)

    def check_serial_event(self):
        return
        # serial_thread = threading.Timer(0.1, self.check_serial_event)
        # if ser.is_open == True:
        # serial_thread.start()
        # if ser.in_waiting:
        #     t = ser.read().decode('utf-8')
        #     # t = t[:t.find('/n')]
        #     print(t)
        #     if t == '1' and self.flag1:
        #
        #         self.counter += 1
        #         self.Pause1()
        #
        #     if t == '2' and self.flag2:
        #         self.counter += 1
        #         self.Pause2()
        #
        #     if t == "3" and self.flag3:
        #         self.counter += 1
        #         self.Pause3()
        #
        #     if t == "4" and self.flag4:
        #         self.counter += 1
        #         self.Pause4()
        #
        #     if t == "5" and self.flag5:
        #         self.counter += 1
        #         self.Pause5()
        #
        #     if t == "6" and self.flag6:
        #         self.counter += 1
        #         self.Pause6()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
