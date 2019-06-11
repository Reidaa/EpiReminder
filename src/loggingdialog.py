import configparser
import os
from pathlib import Path
from typing import Optional

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QLabel, QWidget

from src.intra.api import API
from ui.Ui_LoggingDialog import Ui_LoggingDialog


class ClickableLinkLabel(QLabel):
    def __init__(self, parent, txt: str):
        QLabel.__init__(self, parent)
        self.setText(txt)
        self.setTextFormat(Qt.RichText)
        self.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.setOpenExternalLinks(True)
        self.setAlignment(Qt.AlignCenter)


class ConfData:
    def __init__(self):
        self.__home = str(Path.home())
        self.config = configparser.ConfigParser()
        self._path = self.__home + "/.epireminder.ini"
        self._exist = os.path.isfile(self._path)
        if self._exist is False:
            self.__create_conf_file()
        else:
            self.config.read(self._path)

    def __create_conf_file(self):
        self.config['REMEMBER'] = {
            "username": 'False',
            "token": "False"
        }
        self.config['CREDENTIALS'] = {
            "username": "USERNAME",
            "token": "TOKEN"
        }
        with open(self._path, 'w+') as configfile:
            self.config.write(configfile)

    def reload_config(self):
        with open(self._path, 'w+') as configfile:
            self.config.write(configfile)

    def get_username(self):
        return self.config['CREDENTIALS']['username']

    def get_token(self):
        return self.config['CREDENTIALS']['token']

    def set_username(self, username: str):
        self.config['CREDENTIALS']['username'] = username
        with open(self._path, 'w+') as configfile:
            self.config.write(configfile)

    def set_token(self, token: str):
        pass


class LoggingDialog(QDialog, Ui_LoggingDialog):
    def __init__(self, parent: Optional[QWidget] = None, fun: classmethod = None):
        QDialog.__init__(self, parent)
        self.find_token_lbl = ClickableLinkLabel(self, "<a href=\"https://intra.epitech.eu/admin/autolog\">Ou trouver mon token d'autologin ?</a>")
        self.username = ""
        self.token = ""
        self.configurator = ConfData()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.state = 0
        self.fun = fun

        self.__conf_ui()
        self.__conf_signals()
        self.state = 0
        self.show()

    def __conf_ui(self):
        self.setupUi(self)
        self.verticalLayout.addWidget(self.find_token_lbl)
        self.setWindowTitle("EpiReminder - Logging")
        if self.configurator.config['REMEMBER']['username'] == "True":
            self.remember_user_checkbox.setChecked(True)
            self.username_lineEdit.setText(self.configurator.config['CREDENTIALS']['username'])
        if self.configurator.config['REMEMBER']['token'] == "True":
            self.token_lineEdit.setText(self.configurator.config['CREDENTIALS']['token'])
            self.remember_token_checkbox.setChecked(True)

    def __conf_signals(self):
        self.connect_pushbutton.clicked.connect(self._on_connect)

    def __check_options(self):
        if self.remember_user_checkbox.isChecked() is True:
            self.configurator.config['REMEMBER']['username'] = "True"
            self.configurator.config['CREDENTIALS']['username'] = self.username
        else:
            self.configurator.config['REMEMBER']['username'] = "False"

        if self.remember_token_checkbox.isChecked() is True:
            self.configurator.config['REMEMBER']['token'] = "True"
            self.configurator.config['CREDENTIALS']['token'] = self.token
        else:
            self.configurator.config['REMEMBER']['token'] = False
        self.configurator.reload_config()

    @pyqtSlot()
    def _on_connect(self):
        username = self.username_lineEdit.text()
        token = self.token_lineEdit.text()
        if API(username, token).check_log() is False:
            print("Wrong username and/or token {} {}".format(username, token))
        else:
            self.username = username
            self.token = token
            self.__check_options()
            self.state = 1
            if self.fun is not None:
                self.fun(username, token)
            self.close()
