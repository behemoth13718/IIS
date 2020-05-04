import sys
from test import *
from PyQt5 import QtWidgets
from IISCommand import IISCommand

class MyWin(QtWidgets.QMainWindow):

    global label
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.IIS = IISCommand()


        self.ui.pushButton.clicked.connect(self.MyFunction)


    def MyFunction(self):
        self.IIS.test()
        #здесь дергаем функцию из класса IISCommand
        #self.ui.label.setStyleSheet("background-color: rgb(255, 0, 0);")

    def MyFunctionOut(self):
        self.ui.label.setStyleSheet("background-color: rgb(255, 0, 0);")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
