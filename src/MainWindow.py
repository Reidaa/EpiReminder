from PyQt5.QtWidgets import QMainWindow, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self._layout = QVBoxLayout()

        self.setWindowTitle("EpiReminder")
        self.setGeometry(50, 50, 1280, 720)
        self.setLayout(self._layout)

    def run(self):
        self.show()
