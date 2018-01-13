import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox

from view.mainwindow import Ui_MainWindow
from PyIBapi.ibapi_client import IbClient

def msgbtn(i):
   print ("Button pressed is:",i.text())

def close_application(an_app, an_ibapi):

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Do you want to Quit?")
    msg.setWindowTitle("Quit?")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()

    print ("value of pressed message box button:", retval)
    print ("value of QMessageBox.Ok            :", QMessageBox.Ok)

    if retval == QMessageBox.Ok:
        print('quit application')
        an_ibapi.close()
        #sys.exit(app.exec_())
        #an_app.instance().quit()
    else:
        pass

def setup_window (ui_window, main_window, an_app):
    # update the Drop Down menus
    security_types = ["STK", "IND", "OPT", "FUT", "FOP", "CASH", "BAG", "NEWS"]
    ui_window.securityType.addItems(security_types)
    exchange_types = ["SMART", "CBOE", "AMEX", "IDEAL", "ISLAND", "NYSE", "PHLX"]
    ui_window.exchangeLoc.addItems(exchange_types)
    callPut_types = ["Call", "Put"]
    ui_window.callPut.addItems(callPut_types)
    currency_types = ["USD", "EUR", "JPY", "GBP", "INR", "CAD", "AUD"]
    ui_window.currency.addItems(currency_types)

    print("ui_main_window: ", ui_window)
    print("ui_main_window: ", main_window)
    print("an_app:         ", an_app)
    print("ui_main_window.actionQuit:        ", ui_window.actionQuit)

    ui_window.actionQuit.triggered.connect(close_application)

   #ui_main_window.statusbar()

    # add the IB icon
    QWidget.setWindowIcon(main_window, QIcon('icons\ib.png'))



if __name__ == "__main__":

    # create main window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # connect to IB
    ib_client = IbClient()
    ib_client.connect()

    setup_window(ui, MainWindow, app)

    MainWindow.show()

    print("app:        ", app)
    print("MainWindow: ", MainWindow)
    print("ui:         ", ui)
    # IB api Doc state
    #   User is required to trigger Client::run()
    #   he message queue is processed in an infinite loop and
    #   the EWrapper call-back functions are automatically triggered
    # ib_client.run()
    sys.exit(app.exec_())


