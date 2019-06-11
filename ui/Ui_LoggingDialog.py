# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/LoggingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_LoggingDialog(object):
    def setupUi(self, LoggingDialog):
        LoggingDialog.setObjectName("LoggingDialog")
        LoggingDialog.resize(400, 204)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoggingDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.connect_lbl = QtWidgets.QLabel(LoggingDialog)
        self.connect_lbl.setObjectName("connect_lbl")
        self.verticalLayout.addWidget(self.connect_lbl)
        self.username_lineEdit = QtWidgets.QLineEdit(LoggingDialog)
        self.username_lineEdit.setInputMask("")
        self.username_lineEdit.setText("")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.verticalLayout.addWidget(self.username_lineEdit)
        self.token_lineEdit = QtWidgets.QLineEdit(LoggingDialog)
        self.token_lineEdit.setEnabled(True)
        self.token_lineEdit.setText("")
        self.token_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.token_lineEdit.setObjectName("token_lineEdit")
        self.verticalLayout.addWidget(self.token_lineEdit)
        self.remember_user_checkbox = QtWidgets.QCheckBox(LoggingDialog)
        self.remember_user_checkbox.setObjectName("remember_user_checkbox")
        self.verticalLayout.addWidget(self.remember_user_checkbox)
        self.remember_token_checkbox = QtWidgets.QCheckBox(LoggingDialog)
        self.remember_token_checkbox.setEnabled(True)
        self.remember_token_checkbox.setObjectName("remember_token_checkbox")
        self.verticalLayout.addWidget(self.remember_token_checkbox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.connect_pushbutton = QtWidgets.QPushButton(LoggingDialog)
        self.connect_pushbutton.setObjectName("connect_pushbutton")
        self.verticalLayout.addWidget(self.connect_pushbutton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(LoggingDialog)
        QtCore.QMetaObject.connectSlotsByName(LoggingDialog)

    def retranslateUi(self, LoggingDialog):
        _translate = QtCore.QCoreApplication.translate
        LoggingDialog.setWindowTitle(_translate("LoggingDialog", "Dialog"))
        self.connect_lbl.setText(_translate("LoggingDialog", "Connect to the intra"))
        self.username_lineEdit.setPlaceholderText(_translate("LoggingDialog", "name.lastname@epitech.eu"))
        self.token_lineEdit.setPlaceholderText(_translate("LoggingDialog", "auth-"))
        self.remember_user_checkbox.setText(_translate("LoggingDialog", "Remember username"))
        self.remember_token_checkbox.setText(_translate("LoggingDialog", "Remember token"))
        self.connect_pushbutton.setText(_translate("LoggingDialog", "Connect"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoggingDialog = QtWidgets.QDialog()
    ui = Ui_LoggingDialog()
    ui.setupUi(LoggingDialog)
    LoggingDialog.show()
    sys.exit(app.exec_())
