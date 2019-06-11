from PyQt5.QtWidgets import QMainWindow

from mainwindow import MainWindow


class Core:
    main_window: QMainWindow

    def __init__(self):
        self.main_window = MainWindow()

        self.main_window.run()
