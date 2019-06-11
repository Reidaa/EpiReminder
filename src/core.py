from loggingdialog import LoggingDialog
from mainwindow import MainWindow


class Core:
    def __init__(self):
        self.logging = LoggingDialog(None)
        self.main_window = MainWindow(None)

    def run(self):
        self.logging.exec()
        if self.logging.username == "" or self.logging.token == "":
            print("Connection failed")
            return
        else:
            print("Connection succesfull")
            self.main_window.run(self.logging.username, self.logging.token)
            self.main_window.show()


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thing = Core()
    thing.run()
    sys.exit(app.exec_())
