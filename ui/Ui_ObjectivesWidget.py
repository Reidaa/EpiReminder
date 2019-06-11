# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/ObjectivesWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_ObjectivesWidget(object):
    def setupUi(self, ObjectivesWidget):
        ObjectivesWidget.setObjectName("ObjectivesWidget")
        ObjectivesWidget.resize(426, 260)
        self.verticalLayout = QtWidgets.QVBoxLayout(ObjectivesWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(ObjectivesWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ObjectivesWidget)
        QtCore.QMetaObject.connectSlotsByName(ObjectivesWidget)

    def retranslateUi(self, ObjectivesWidget):
        _translate = QtCore.QCoreApplication.translate
        ObjectivesWidget.setWindowTitle(_translate("ObjectivesWidget", "Form"))
        self.label.setText(_translate("ObjectivesWidget", "Progression Hub"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ObjectivesWidget = QtWidgets.QWidget()
    ui = Ui_ObjectivesWidget()
    ui.setupUi(ObjectivesWidget)
    ObjectivesWidget.show()
    sys.exit(app.exec_())
