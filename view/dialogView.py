from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox


from view.dialog import Ui_exchange


def setup_window (ui_ex, Qwidget):
    # update the Drop Down menus
    security_types = ["STK", "IND", "OPT", "FUT", "FOP", "CASH", "BAG", "NEWS"]
    ui_ex.securityType.addItems(security_types)
    exchange_types = ["SMART", "CBOE", "AMEX", "IDEAL", "ISLAND", "NYSE", "PHLX"]
    ui_ex.exchangeLoc.addItems(exchange_types)
    callPut_types = ["Call", "Put"]
    ui_ex.callPut.addItems(callPut_types)
    currency_types = ["USD", "EUR", "JPY", "GBP", "INR", "CAD", "AUD"]
    ui_ex.currency.addItems(currency_types)

    # add the IB icon
    Qwidget.setWindowIcon(QIcon('icons\ib.png'))

    # # Set up application exit
    exit_app = QAction('&Exit', Qwidget)
    exit_app.setShortcut('Ctrl+Q')
    exit_app.setStatusTip('leave the app')
    print("exit_app:  ", exit_app)
    #exit_app.triggered.connect(sys.exit())
    #
    # # create and add Menu
    mainMenu = QMainWindow.menuBar()
    fileMenu = mainMenu.addMenu('&File')
    fileMenu.addAction(exit_app)
    #
    # QMainWindow.statusBar()


if __name__ == "__main__":
    # create QT window
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exchange = QtWidgets.QDialog()
    ui = Ui_exchange()
    ui.setupUi(exchange)

    print("QtWidgets: ", QtWidgets)
    print("app:       ", app)
    print("exchange:  ", exchange)
    print("ui:        ", ui)

    # setup details of QT window
    setup_window(ui, app)

    exchange.show()
    sys.exit(app.exec_())



