import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.le)
        h_box.addWidget(self.b2)

        v_box = QtWidgets.QVBoxLayout()
        #v_box.addWidget(h_box)
        v_box.addWidget(self.b1)

        self.setLayout(v_box)
        self.setLayout(h_box)
        self.setWindowTitle('PyQt5 Lesson 7')

        self.b1.clicked.connect(self.btn_clk)
        self.b2.clicked.connect(self.btn_clk)

        self.le.setText("cat")

        self.show()

    def btn_clk(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())