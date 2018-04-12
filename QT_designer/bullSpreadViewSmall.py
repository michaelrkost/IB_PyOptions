# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bullSpreadViewSmall.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 201, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.underlyingText = QtWidgets.QLineEdit(self.groupBox_2)
        self.underlyingText.setGeometry(QtCore.QRect(10, 40, 61, 20))
        self.underlyingText.setObjectName("underlyingText")
        self.updatePushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.updatePushButton.setGeometry(QtCore.QRect(120, 110, 75, 23))
        self.updatePushButton.setObjectName("updatePushButton")
        self.comboBoxExchange = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxExchange.setGeometry(QtCore.QRect(90, 40, 71, 22))
        self.comboBoxExchange.setToolTip("")
        self.comboBoxExchange.setObjectName("comboBoxExchange")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.comboBoxExchange.addItem("")
        self.labelExchange = QtWidgets.QLabel(self.groupBox_2)
        self.labelExchange.setGeometry(QtCore.QRect(90, 24, 47, 13))
        self.labelExchange.setWhatsThis("")
        self.labelExchange.setObjectName("labelExchange")
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setGeometry(QtCore.QRect(10, 80, 185, 17))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.radioButton_Index = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_Index.setChecked(True)
        self.radioButton_Index.setObjectName("radioButton_Index")
        self.radioButton_Stock = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_Stock.setObjectName("radioButton_Stock")
        self.radioButton_Oprion = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_Oprion.setObjectName("radioButton_Oprion")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(440, 10, 75, 23))
        self.connectButton.setObjectName("connectButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionCon = QtWidgets.QAction(MainWindow)
        self.actionCon.setObjectName("actionCon")
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Underlying Info"))
        self.label_8.setText(_translate("MainWindow", "Underlying:"))
        self.updatePushButton.setText(_translate("MainWindow", "Qualify"))
        self.comboBoxExchange.setItemText(0, _translate("MainWindow", "CBOE"))
        self.comboBoxExchange.setItemText(1, _translate("MainWindow", "ISLAND"))
        self.comboBoxExchange.setItemText(2, _translate("MainWindow", "NYSE"))
        self.comboBoxExchange.setItemText(3, _translate("MainWindow", "AMEX"))
        self.comboBoxExchange.setItemText(4, _translate("MainWindow", "IDEAL"))
        self.comboBoxExchange.setItemText(5, _translate("MainWindow", "PHLX"))
        self.labelExchange.setText(_translate("MainWindow", "Exchange:"))
        self.radioButton_Index.setText(_translate("MainWindow", "Index"))
        self.radioButton_Stock.setText(_translate("MainWindow", "Stock "))
        self.radioButton_Oprion.setText(_translate("MainWindow", "Option"))
        self.connectButton.setText(_translate("MainWindow", "connectIB"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionCon.setText(_translate("MainWindow", "Con"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

