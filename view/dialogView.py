from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox


from view.mainwindow import Ui_MainWindow
def msgbtn(i):
   print ("Button pressed is:",i.text())

def close_application():

    print("hello")
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("This is a message box")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()
    print ("value of pressed message box button:", retval)

def setup_window (ui_main_window, an_app):
    # update the Drop Down menus
    security_types = ["STK", "IND", "OPT", "FUT", "FOP", "CASH", "BAG", "NEWS"]
    ui_main_window.securityType.addItems(security_types)
    exchange_types = ["SMART", "CBOE", "AMEX", "IDEAL", "ISLAND", "NYSE", "PHLX"]
    ui_main_window.exchangeLoc.addItems(exchange_types)
    callPut_types = ["Call", "Put"]
    ui_main_window.callPut.addItems(callPut_types)
    currency_types = ["USD", "EUR", "JPY", "GBP", "INR", "CAD", "AUD"]
    ui_main_window.currency.addItems(currency_types)

    print("an_app:         ", an_app)
    print("ui_main_window: ", ui_main_window)
    print("ui_main_window.actionQuit:        ", ui_main_window.actionQuit)

    ui_main_window.actionQuit.triggered.connect(close_application)

    # add the IB icon
    QWidget.setWindowIcon(an_app, QIcon('icons\ib.png'))


if __name__ == "__main__":
    # create main window
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    setup_window(ui, MainWindow)

    MainWindow.show()

    print("app:        ", app)
    print("MainWindow: ", MainWindow)
    print("ui:         ", ui)

    sys.exit(app.exec_())


