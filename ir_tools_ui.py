# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ir_tools_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        if sys.platform == "win32":
            font.setPointSize(14)
        else:
            font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        if sys.platform == "win32":
            font.setPointSize(12)
        else:
            font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        if sys.platform == "win32":
            font.setPointSize(12)
        else:
            font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 500, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        if sys.platform == "win32":
            font.setPointSize(12)
        else:
            font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 500, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        if sys.platform == "win32":
            font.setPointSize(12)
        else:
            font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 500, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        if sys.platform == "win32":
            font.setPointSize(12)
        else:
            font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 90, 721, 181))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(40, 320, 721, 161))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(120, 500, 111, 31))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(390, 500, 111, 31))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(660, 500, 111, 31))
        self.listWidget_5.setObjectName("listWidget_5")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "学习工具数据显示"))
        self.label.setText(_translate("mainWindow", "当前按键学习数据显示"))
        self.label_2.setText(_translate("mainWindow", "按键时间码"))
        self.label_3.setText(_translate("mainWindow", "按键16进制数据"))
        self.label_4.setText(_translate("mainWindow", "按键频率"))
        self.label_5.setText(_translate("mainWindow", "按键数量"))
        self.label_6.setText(_translate("mainWindow", "设备状态"))
