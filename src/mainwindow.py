from PyQt5.QtWidgets import QMainWindow, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.__layout = QGridLayout()

        self.__conf_ui()

    def __conf_ui(self):
        self.setLayout(self._layout)
        self.setWindowTitle("EpiReminder")
        # self.setGeometry(50, 50, 1280, 720)

    def run(self):
        self.show()
