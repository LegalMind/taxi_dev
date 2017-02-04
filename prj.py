# 외부 모듈
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# 내부 모듈
from modules import common
from ui import mainwindow


def main():
    common.prnt_result()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main()
    sys.exit(app.exec_())
