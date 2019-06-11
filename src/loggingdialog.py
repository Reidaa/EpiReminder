from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QLabel

from api import API
from ui.Ui_LoggingDialog import Ui_LoggingDialog


class ClickableLinkLabel(QLabel):
    def __init__(self, parent, txt: str):
        QLabel.__init__(self, parent)
        self.setText(txt)
        self.setTextFormat(Qt.RichText)
        self.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.setOpenExternalLinks(True)
        self.setAlignment(Qt.AlignCenter)


class LoggingDialog(QDialog, Ui_LoggingDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.find_token_lbl = ClickableLinkLabel(self, "<a href=\"https://intra.epitech.eu/admin/autolog\">Ou trouver mon token d'autologin ?</a>")
        self.username = ""
        self.token = ""

        self.__conf_ui()
        self.__conf_signals()

    def __conf_ui(self):
        self.setupUi(self)
        self.verticalLayout.addWidget(self.find_token_lbl)
        self.setWindowTitle("EpiReminder - Logging")

    def __conf_signals(self):
        self.connect_pushbutton.clicked.connect(self._on_connect)

    @pyqtSlot()
    def _on_connect(self):
        print("connect")
        username = self.username_lineEdit.text()
        token = self.token_lineEdit.text()
        if API(username, token).check_log() is False:
            pass
        else:
            self.username = username
            self.token = token
            self.close()


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thing = LoggingDialog(None)
    thing.show()
    sys.exit(app.exec_())
