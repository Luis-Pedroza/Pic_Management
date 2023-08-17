# ***************************************************
# FILE: Main.py
#
# DESCRIPTION: 
# This code imports the main UI and initialize it
#
# AUTHOR:  Luis Pedroza
# CREATED: 05/07/2023 (dd/mm/yy)
# ******************* ********************************

# Command to create an exe.
# pyinstaller --onefile --noconsole -n "Pic Management" Main.py
# pylupdate5 prueba2.py -ts translations2_en.ts  

import sys
from PyQt5 import QtWidgets
from assets.UI_Window import Ui_MainWindow

#Initialize the Ui_MainWindow as a QMainWindow type
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#Initialize de mainWindow until program is closed
if __name__ == '__main__':

    InitMainWindow = QtWidgets.QApplication([])    
    MainApp = MainWindow()
    MainApp.show()
    sys.exit(InitMainWindow.exec())