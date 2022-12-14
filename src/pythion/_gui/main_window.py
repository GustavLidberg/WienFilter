from __future__ import annotations

from typing import ClassVar, Any
import sys
import matplotlib.pyplot as plt

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from pythion._layout.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    _instance: ClassVar[MainWindow | None] = None
    _app: ClassVar[QApplication]

    def __new__(cls, *args: Any, **kwargs: Any) -> MainWindow:
        # This __new__ method serves two purposes: enforcing a singleton pattern (i.e. only one MainWindowComponent may ever
        # be instantiated), and instantiating the QApplication object.
        if cls._instance is None:  # Only run once!
            # Do some initial configuration of Qt
            if 'high_resolution' in kwargs and kwargs['high_resolution']:
                # The following four lines enables using the system dpi settings - however - they aren't compatible with matplotlib
                if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
                    QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
                if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
                    QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

            # The Qapplication must be instantiated before any QWidgets, hence the class variable
            cls._app = QApplication(sys.argv)
            # Finally, instantiate and return this object through a call to super().__new__()
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, high_resolution: bool = False) -> None:
        # Boilerplate initialization
        super().__init__(None)
        self.setupUi(self)  # type: ignore

    def main_widget(self) -> QWidget:
        return self.horizontalLayoutWidget

    def add_children(self, *children: QWidget) -> None:
        for child in children:
            self.mainLayout.addWidget(child)

    def run(self) -> None:
        self.show()
        sys.exit(self._app.exec())

    def closeEvent(self, *args: Any):
        plt.close('all')
