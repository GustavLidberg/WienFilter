import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from voltage_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.configure()

    def configure(self):
        # Connect dial to input voltage display
        self.voltageDial.valueChanged.connect(self.newValueLCD.display)
        self.setBtn.clicked.connect(self.set_value)
    
    def set_value(self):
        self.lastValueLCD.display(self.voltageDial.value())

if __name__ == "__main__":
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())