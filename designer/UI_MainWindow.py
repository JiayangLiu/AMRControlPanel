# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(620, 0, 171, 551))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_AddZone = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_AddZone.setGeometry(QtCore.QRect(10, 510, 70, 30))
        self.pushButton_AddZone.setObjectName("pushButton_AddZone")
        self.pushButton_DeleteZone = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_DeleteZone.setGeometry(QtCore.QRect(90, 510, 70, 30))
        self.pushButton_DeleteZone.setObjectName("pushButton_DeleteZone")
        self.listWidget_NoGoZone = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_NoGoZone.setGeometry(QtCore.QRect(10, 30, 151, 471))
        self.listWidget_NoGoZone.setObjectName("listWidget_NoGoZone")
        self.groupBox_ControlPanel = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ControlPanel.setGeometry(QtCore.QRect(10, 0, 601, 551))
        self.groupBox_ControlPanel.setObjectName("groupBox_ControlPanel")
        self.pushButton_BuildMap = QtWidgets.QPushButton(self.groupBox_ControlPanel)
        self.pushButton_BuildMap.setGeometry(QtCore.QRect(30, 510, 160, 30))
        self.pushButton_BuildMap.setObjectName("pushButton_BuildMap")
        self.pushButton_LoadMap = QtWidgets.QPushButton(self.groupBox_ControlPanel)
        self.pushButton_LoadMap.setGeometry(QtCore.QRect(220, 510, 160, 30))
        self.pushButton_LoadMap.setObjectName("pushButton_LoadMap")
        self.pushButton_StartCleaning = QtWidgets.QPushButton(self.groupBox_ControlPanel)
        self.pushButton_StartCleaning.setGeometry(QtCore.QRect(410, 510, 160, 30))
        self.pushButton_StartCleaning.setObjectName("pushButton_StartCleaning")
        self.label_mapdisplay = QtWidgets.QLabel(self.groupBox_ControlPanel)
        self.label_mapdisplay.setGeometry(QtCore.QRect(10, 30, 581, 471))
        self.label_mapdisplay.setScaledContents(False)
        self.label_mapdisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mapdisplay.setWordWrap(True)
        self.label_mapdisplay.setIndent(0)
        self.label_mapdisplay.setObjectName("label_mapdisplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AMR Control Panel"))
        self.groupBox.setTitle(_translate("MainWindow", "No-go Zone"))
        self.pushButton_AddZone.setText(_translate("MainWindow", "Add"))
        self.pushButton_DeleteZone.setText(_translate("MainWindow", "Delete"))
        self.groupBox_ControlPanel.setTitle(_translate("MainWindow", "Control Panel"))
        self.pushButton_BuildMap.setText(_translate("MainWindow", "Build Map"))
        self.pushButton_LoadMap.setText(_translate("MainWindow", "Load Map"))
        self.pushButton_StartCleaning.setText(_translate("MainWindow", "Start Cleaning"))
        self.label_mapdisplay.setText(_translate("MainWindow", "To start, please click \"Build Map\" to let robot start scanning the environment, or \"Load Map\" to use a existed map."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
