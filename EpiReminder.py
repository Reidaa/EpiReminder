#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QApplication

from src.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(None)
    window.login()
    sys.exit(app.exec_())

