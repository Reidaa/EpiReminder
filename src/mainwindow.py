from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QDesktopWidget

from loggingdialog import LoggingDialog
from mainwidget import MainWidget


class MainWindow(QMainWindow):
    def __init__(self, parent):
        QMainWindow.__init__(self, parent)
        self._central_layout = QGridLayout()
        self._central_widget = QWidget(self)
        self._main_widget = MainWidget(self)

        self.__conf_ui()

    def __conf_ui(self):
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self._central_layout)
        self._central_layout.addWidget(self._main_widget)
        self.setWindowTitle("EpiReminder")
        self.setMinimumSize(930, 520)
        self.__center()

    def __center(self):
        desktop = QDesktopWidget()
        screen_width = desktop.width()
        screen_height = desktop.height()
        window_size = self.size()
        width = window_size.width()
        height = window_size.height()
        x = (screen_width - width) / 2
        y = (screen_height - height) / 2
        self.move(x, y)

    def login(self):
        LoggingDialog(self, self._run)

    def _run(self, username: str = None, token: str = None):
        # logging = LoggingDialog(self)
        # if logging.username == "" or logging.token == "":
        #     sys.exit(0)
        self._main_widget.run(username, token)
        self.show()


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(None)
    with open("../log.txt") as file:
        lines = file.readlines()
    window.login()
    # window.run(lines[2][:-1], lines[3][:-1])

    print(window.size())
    sys.exit(app.exec_())
