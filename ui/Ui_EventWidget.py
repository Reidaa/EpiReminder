# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/EventWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_EventWidget(object):
    def setupUi(self, EventWidget):
        EventWidget.setObjectName("EventWidget")
        EventWidget.resize(528, 150)
        EventWidget.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(EventWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hours_lbl = QtWidgets.QLabel(EventWidget)
        self.hours_lbl.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.hours_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hours_lbl.setLineWidth(2)
        self.hours_lbl.setText("")
        self.hours_lbl.setObjectName("hours_lbl")
        self.verticalLayout.addWidget(self.hours_lbl)
        self.title_lbl = QtWidgets.QLabel(EventWidget)
        self.title_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_lbl.setText("")
        self.title_lbl.setWordWrap(True)
        self.title_lbl.setObjectName("title_lbl")
        self.verticalLayout.addWidget(self.title_lbl)
        self.room_lbl = QtWidgets.QLabel(EventWidget)
        self.room_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.room_lbl.setText("")
        self.room_lbl.setObjectName("room_lbl")
        self.verticalLayout.addWidget(self.room_lbl)

        self.retranslateUi(EventWidget)
        QtCore.QMetaObject.connectSlotsByName(EventWidget)

    def retranslateUi(self, EventWidget):
        _translate = QtCore.QCoreApplication.translate
        EventWidget.setWindowTitle(_translate("EventWidget", "Form"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EventWidget = QtWidgets.QWidget()
    ui = Ui_EventWidget()
    ui.setupUi(EventWidget)
    EventWidget.show()
    sys.exit(app.exec_())
