from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 590)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(620, 0, 171, 551))
        self.groupBox.setObjectName("groupBox")

        self.listWidget_NoGoZone = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_NoGoZone.setGeometry(QtCore.QRect(10, 30, 151, 471))
        self.listWidget_NoGoZone.setObjectName("listWidget_NoGoZone")

        self.pushButton_AddZone = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_AddZone.setGeometry(QtCore.QRect(10, 510, 70, 30))
        self.pushButton_AddZone.setObjectName("pushButton_AddZone")

        self.pushButton_DeleteZone = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_DeleteZone.setGeometry(QtCore.QRect(90, 510, 70, 30))
        self.pushButton_DeleteZone.setObjectName("pushButton_DeleteZone")

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

        self.label_MapDisplay = QtWidgets.QLabel(self.groupBox_ControlPanel)
        self.label_MapDisplay.setGeometry(QtCore.QRect(50, 30, 581, 471))
        self.label_MapDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_MapDisplay.setWordWrap(True)
        self.label_MapDisplay.setIndent(0)
        self.label_MapDisplay.setObjectName("label_MapDisplay")
        self.label_MapDisplay.setScaledContents(False)
        self.label_MapDisplay.mousePressEvent = self.mousePressEvent        # override the mousePressEvent
        self.label_MapDisplay.mouseMoveEvent = self.mouseMoveEvent
        self.label_MapDisplay.mouseReleaseEvent = self.mouseReleaseEvent

        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_ControlPanel)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 581, 471))
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.label_MapDisplay)
        self.scrollArea.setWidgetResizable(True)        # keep the map image in its original size
        self.scrollArea.setVisible(True)

        self.rectangleStartPoint = QtCore.QPoint()
        self.rectangleEndPoint = QtCore.QPoint()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setUpButtonClickEvent()

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
        self.label_MapDisplay.setText(_translate("MainWindow", "To start, please click \"Build Map\" to let robot start scanning the environment, or \"Load Map\" to use a existed map."))

    # set up click event for each button
    def setUpButtonClickEvent(self):
        self.pushButton_BuildMap.clicked.connect(self.clickButton_BuildMap)
        self.pushButton_LoadMap.clicked.connect(self.clickButton_LoadMap)
        self.pushButton_StartCleaning.clicked.connect(self.clickButton_StartCleaning)
        self.pushButton_AddZone.clicked.connect(self.clickButton_AddZone)
        self.pushButton_DeleteZone.clicked.connect(self.clickButton_DeleteZone)
        self.isAddingZone = False

    # action when click button "Build map"
    def clickButton_BuildMap(self):
        # TODO: after map building finished
        print('pushButton_BuildMap clicked')

    # action when click button "Load map"
    def clickButton_LoadMap(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd()+'/map', "Image files (*.jpg *.gif *.png)")
        self.imagePath = fname[0]
        pixmap = QPixmap(self.imagePath)
        self.label_MapDisplay.setPixmap(QPixmap(pixmap))
        # clear action when load a new map
        self.rectangleDict = {}
        self.listWidget_NoGoZone.clear()

    # action when click button "Start cleaning"
    def clickButton_StartCleaning(self):
        # TODO: after path planning finished
        print('pushButton_StartCleaning clicked')

    # action when click button "Add zone"
    def clickButton_AddZone(self):
        self.isAddingZone = True

    # action when click button "Delete zone"
    def clickButton_DeleteZone(self):
        deleteItemList = self.listWidget_NoGoZone.selectedItems()
        if not deleteItemList:      # if the list is empty
            return
        for deleteItem in deleteItemList:
            # print('Item deleted: ' + deleteItem.text())
            self.listWidget_NoGoZone.takeItem(self.listWidget_NoGoZone.row(deleteItem))
            del self.rectangleDict[deleteItem.text()]
            self.updatePixMap()

    # override the mousePressEvent of self.label_MapDisplay
    def mousePressEvent(self, event):
        if self.isAddingZone and event.button() == Qt.LeftButton:
            self.rectangleStartPoint = event.pos()
            self.rectangleEndPoint = event.pos()
        super().mousePressEvent(event)

    # override the mouseMoveEvent of self.label_MapDisplay
    def mouseMoveEvent(self, event):
        if self.isAddingZone and event.button() == Qt.LeftButton:
            self.rectangleEndPoint = event.pos()
            self.update()
        super().mouseMoveEvent(event)

    # override the mouseReleaseEvent of self.label_MapDisplay
    def mouseReleaseEvent(self, event):
        if self.isAddingZone and event.button() == Qt.LeftButton:
            self.rectangleEndPoint = event.pos()
            self.isAddingZone = False
            key = '(' + str(self.rectangleStartPoint.x()) + ',' + str(self.rectangleStartPoint.y()) \
                  + ') -> (' + str(self.rectangleEndPoint.x()) + ',' + str(self.rectangleEndPoint.y()) + ')'
            self.rectangleDict[key] = QtCore.QRect(self.rectangleStartPoint, self.rectangleEndPoint)
            self.listWidget_NoGoZone.addItem(QListWidgetItem(key))
            self.updatePixMap()
        super().mouseReleaseEvent(event)

    # helper function to re-print the pixmap of self.label_MapDisplay
    def updatePixMap(self):
        pixmap = QPixmap(self.imagePath)
        painterInstnace = QtGui.QPainter(pixmap)
        painterInstnace.setBrush(QtGui.QBrush(QtGui.QColor(100, 10, 10, 40)))
        for dictKey in self.rectangleDict:
            painterInstnace.drawRect(self.rectangleDict.get(dictKey))
        self.label_MapDisplay.setPixmap(pixmap)
        self.label_MapDisplay.show()
        painterInstnace.end()       # to avoid error msg "QPaintDevice: Cannot destroy paint device that is being painted"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
