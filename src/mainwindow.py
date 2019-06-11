from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget

from loggingdialog import LoggingDialog
from mainwidget import MainWidget


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self._central_layout = QGridLayout()
        self._central_widget = QWidget(self)
        self.loggin = LoggingDialog(self)
        self.loggin.exec()
        self._widget = MainWidget(self, self.loggin.username, self.loggin.token)

        self.__conf_ui()

    def __conf_ui(self):
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self._central_layout)
        self._central_layout.addWidget(self._widget)
        self.setWindowTitle("EpiReminder")

    def run(self):
        self.show()


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.run()
    sys.exit(app.exec_())
