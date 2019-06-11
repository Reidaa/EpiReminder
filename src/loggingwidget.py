from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QLineEdit

from ui.Ui_LoggingWidget import Ui_LoggingWidget


class LoggingWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_LoggingWidget()
        self._conf_ui()

    def _conf_ui(self):
        self.ui.setupUi(self)
        self.ui.show_password_checkbox.stateChanged.connect(self._on_show_password)
        self.ui.connect_pushbutton.clicked.connect(self._on_connect)
        self.ui.password_lineEdit.setHidden(True)
        self.ui.show_password_checkbox.setHidden(True)
        self.ui.remember_password_checkbox.setHidden(True)

    @pyqtSlot()
    def _on_connect(self):
        print("connect")
        username = self.ui.username_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        print(username, password)

    @pyqtSlot()
    def _on_show_password(self):
        state = self.ui.show_password_checkbox.isChecked()
        if state is False:
            self.ui.password_lineEdit.setEchoMode(QLineEdit.Password)
        else:
            self.ui.password_lineEdit.setEchoMode(QLineEdit.Normal)


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thing = LoggingWidget()
    # LoggingWidget = QtWidgets.QWidget()
    # ui = Ui_LoggingWidget()
    # ui.setupUi(LoggingWidget)
    # LoggingWidget.show()
    thing.show()
    sys.exit(app.exec_())
