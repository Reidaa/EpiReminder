# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/LoggingWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_LoggingWidget(object):
    def setupUi(self, LoggingWidget):
        LoggingWidget.setObjectName("LoggingWidget")
        LoggingWidget.resize(400, 233)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoggingWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.connect_lbl = QtWidgets.QLabel(LoggingWidget)
        self.connect_lbl.setObjectName("connect_lbl")
        self.verticalLayout.addWidget(self.connect_lbl)
        self.username_lineEdit = QtWidgets.QLineEdit(LoggingWidget)
        self.username_lineEdit.setInputMask("")
        self.username_lineEdit.setText("")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.verticalLayout.addWidget(self.username_lineEdit)
        self.password_lineEdit = QtWidgets.QLineEdit(LoggingWidget)
        self.password_lineEdit.setEnabled(True)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.verticalLayout.addWidget(self.password_lineEdit)
        self.show_password_checkbox = QtWidgets.QCheckBox(LoggingWidget)
        self.show_password_checkbox.setObjectName("show_password_checkbox")
        self.verticalLayout.addWidget(self.show_password_checkbox)
        self.remember_user_checkbox = QtWidgets.QCheckBox(LoggingWidget)
        self.remember_user_checkbox.setObjectName("remember_user_checkbox")
        self.verticalLayout.addWidget(self.remember_user_checkbox)
        self.remember_password_checkbox = QtWidgets.QCheckBox(LoggingWidget)
        self.remember_password_checkbox.setEnabled(True)
        self.remember_password_checkbox.setObjectName("remember_password_checkbox")
        self.verticalLayout.addWidget(self.remember_password_checkbox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.connect_pushbutton = QtWidgets.QPushButton(LoggingWidget)
        self.connect_pushbutton.setObjectName("connect_pushbutton")
        self.verticalLayout.addWidget(self.connect_pushbutton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(LoggingWidget)
        QtCore.QMetaObject.connectSlotsByName(LoggingWidget)

    def retranslateUi(self, LoggingWidget):
        _translate = QtCore.QCoreApplication.translate
        LoggingWidget.setWindowTitle(_translate("LoggingWidget", "Form"))
        self.connect_lbl.setText(_translate("LoggingWidget", "Connect to the intra"))
        self.username_lineEdit.setPlaceholderText(_translate("LoggingWidget", "name.lastname@epitech.eu"))
        self.password_lineEdit.setPlaceholderText(_translate("LoggingWidget", "password"))
        self.show_password_checkbox.setText(_translate("LoggingWidget", "Show password"))
        self.remember_user_checkbox.setText(_translate("LoggingWidget", "Remember this username"))
        self.remember_password_checkbox.setText(_translate("LoggingWidget", "Remember password"))
        self.connect_pushbutton.setText(_translate("LoggingWidget", "Connect"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoggingWidget = QtWidgets.QWidget()
    ui = Ui_LoggingWidget()
    ui.setupUi(LoggingWidget)
    LoggingWidget.show()
    sys.exit(app.exec_())
