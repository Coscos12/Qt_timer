import sys
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QDialog
)
import threading
from second_window import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.col = QColor(0, 0, 0)
        self.counter = 0
        Dialog.setObjectName("Dialog")
        Dialog.resize(776, 482)
        self.second_window = Example()
        for i in range(1, 8):
            setattr(self, f"lineEdit{i}", QtWidgets.QLineEdit(Dialog))
            getattr(self, f"lineEdit{i}").setObjectName(f"lineEdit{i}")
            getattr(self, f"lineEdit{i}").setGeometry(QtCore.QRect(80, 90+i*40, 400, 30))
        self.lineEdit7.setGeometry(QtCore.QRect(210, 40, 400, 30))



        # self.lineEdit0 = QtWidgets.QLineEdit(Dialog)
        # self.lineEdit0.setGeometry(QtCore.QRect(210, 380, 400, 30))
        # self.LineEdit0.setObjectName("LineEdit0")

        for i in range(1, 7):
            # getattr(self, f"label{i}").setEnabled(True)
            setattr(self, f"pause_btn{i}", QtWidgets.QPushButton(Dialog))
            getattr(self, f"pause_btn{i}").setObjectName(f"pause_btn{i}")
            getattr(self, f"pause_btn{i}").setGeometry(QtCore.QRect(520, 90+i*40, 75, 30))

        self.button_font = QtWidgets.QPushButton(Dialog)
        self.button_font.setObjectName("pause_font")
        self.button_font.setGeometry(QtCore.QRect(80, 430, 75, 25))
        self.button_font.setText("шрифт")

        self.button_color = QtWidgets.QPushButton(Dialog)
        self.button_color.setObjectName("pause_color")
        self.button_color.setGeometry(QtCore.QRect(180, 430, 75, 25))
        self.button_color.setText("цвет")

        self.pause_btn1.setText("голубой")
        self.pause_btn2.setText("розовый")
        self.pause_btn3.setText("красный")
        self.pause_btn4.setText("желтый")
        self.pause_btn5.setText("синий")
        self.pause_btn6.setText("зеленый")

        self.pause_btn1.setStyleSheet("background-color: rgb(135, 206,250);")
        self.pause_btn2.setStyleSheet("background-color: rgb(238, 130, 238);")
        self.pause_btn3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pause_btn4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pause_btn5.setStyleSheet("background-color: rgb(0, 100, 255);")
        self.pause_btn6.setStyleSheet("background-color: rgb(0, 255, 0);")

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(81, 390, 589, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comL = QtWidgets.QComboBox(self.widget)
        self.comL.setObjectName("comL")
        serial = QSerialPort()
        serial.setBaudRate(9600)
        portList = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portList.append(port.portName())
        self.comL.addItems(portList)
        self.horizontalLayout.addWidget(self.comL)
        # self.fontComboBox = QtWidgets.QFontComboBox(self.widget)
        self.choose_backgroung = QtWidgets.QPushButton(self.widget)
        self.start_button = QtWidgets.QPushButton(self.widget)
        self.stop_button = QtWidgets.QPushButton(self.widget)
        self.reset_button = QtWidgets.QPushButton(self.widget)
        self.start_window = QtWidgets.QPushButton(self.widget)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.widget)

        # self.fontComboBox.setObjectName("fontComboBox")
        self.choose_backgroung.setObjectName("Choose_background")
        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.reset_button.setObjectName("reset_button")
        self.start_window.setObjectName("reset_button")

        # self.horizontalLayout.addWidget(self.fontComboBox)
        self.horizontalLayout.addWidget(self.choose_backgroung)
        self.horizontalLayout.addWidget(self.start_button)
        self.horizontalLayout.addWidget(self.stop_button)
        self.horizontalLayout.addWidget(self.reset_button)
        self.horizontalLayout.addWidget(self.start_window)



        self.retranslateUi(Dialog)
        self.add_functions()

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choose_backgroung.setText(_translate("Dialog", "Выбрать"))
        self.start_button.setText(_translate("Dialog", "Старт"))
        self.stop_button.setText(_translate("Dialog", "Стоп"))
        self.reset_button.setText(_translate("Dialog", "Сброс"))
        self.start_window.setText(_translate("Dialog", "Отобразить"))

    def add_functions(self):
        self.timer = QTimer()
        # self.timer.timeout.connect(self.printing)
        self.timer.start(10)

        self.start_button.clicked.connect(lambda: self.second_window.Start())
        self.stop_button.clicked.connect(lambda: self.second_window.Stop())
        self.reset_button.clicked.connect(self.Reset)
        self.start_window.clicked.connect(self.printing)
        self.choose_backgroung.clicked.connect(self.file_select)
        # for i in range(1, 7):
        #     getattr(self, f"pause_btn{i}").clicked.connect(lambda: self.Pause(i))
        self.pause_btn1.clicked.connect(lambda: self.Pause(1))
        self.pause_btn2.clicked.connect(lambda: self.Pause(2))
        self.pause_btn3.clicked.connect(lambda: self.Pause(3))
        self.pause_btn4.clicked.connect(lambda: self.Pause(4))
        self.pause_btn5.clicked.connect(lambda: self.Pause(5))
        self.pause_btn6.clicked.connect(lambda: self.Pause(6))
        self.button_font.clicked.connect(self.Font)
        self.button_color.clicked.connect(self.Color)

    def Font(self):
        print("begin")
        self.Font, self.ok = QFontDialog.getFont()
        print(("init"))
        if self.ok:
            self.second_window.font = self.Font
            print("font done")

    def Color(self):
        self.col = QColorDialog.getColor()
        if self.col.isValid():
            self.second_window.color = self.col
            print("color done")

    def Reset(self):
        self.counter = 0
        self.second_window.Reset()

    def Pause(self, i):
        if (getattr(self.second_window, f"flag{i}") == True):
            setattr(self.second_window, f"flag{i}", False)
            self.counter += 1
            k = self.second_window.places.pop(self.second_window.places.index(self.second_window.new_places[i]))
            self.second_window.places.insert(self.counter, k)

        self.second_window.refreshing()


    def file_select(self):
        filename = QFileDialog.getOpenFileName()
        self.second_window.path = filename[0]


    def printing(self):
        self.second_window.label_header.setText(self.lineEdit7.text())
        self.second_window.textBrowser1.setText(self.lineEdit1.text())
        self.second_window.textBrowser2.setText(self.lineEdit2.text())
        self.second_window.textBrowser3.setText(self.lineEdit3.text())
        self.second_window.textBrowser4.setText(self.lineEdit4.text())
        self.second_window.textBrowser5.setText(self.lineEdit5.text())
        self.second_window.textBrowser6.setText(self.lineEdit6.text())
        self.second_window.visiable()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())