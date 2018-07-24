import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import robot


if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = robot.Ui_Form()

    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_())