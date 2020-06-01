# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rose.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import numpy as np
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 774)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(390, 10, 651, 671))
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3") 
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 80, 301, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 111, 16))
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 180, 311, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.splitter) # length
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2) # k
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.splitter_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout.addWidget(self.splitter_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget) # Start
        self.pushButton.setGeometry(QtCore.QRect(50, 290, 291, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget) # Reset
        self.pushButton_2.setGeometry(QtCore.QRect(50, 470, 291, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        '''
        Ui에 대한 동작과 관련된 함수들을 여기에
        '''
        self.pushButton.clicked.connect(lambda:self.start())
        self.pushButton_2.clicked.connect(lambda:self.reset())


    def start(self):
        theta = np.linspace(0,2*np.pi,360)
        k = self.spinBox_2.value()
        length = self.spinBox.value()

        x = length*np.cos(k*theta)*np.cos(theta)
        y = length*np.cos(k*theta)*np.sin(theta)
        self.graphicsView.plot(x,y)

    def reset(self):
        self.graphicsView.clear()

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Rose (mathematics)"))
        self.label_4.setText(_translate("MainWindow", "https://en.wikipedia.org/wiki/Rose_(mathematics)"))
        self.label_5.setText(_translate("MainWindow", "Insert value"))
        self.label.setText(_translate("MainWindow", "Length"))
        self.label_2.setText(_translate("MainWindow", "k"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
