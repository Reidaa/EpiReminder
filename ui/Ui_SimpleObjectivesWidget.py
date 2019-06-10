# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/SimpleObjectivesWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_SimpleObjectivesWidget(object):
    def setupUi(self, SimpleObjectivesWidget):
        SimpleObjectivesWidget.setObjectName("SimpleObjectivesWidget")
        SimpleObjectivesWidget.resize(237, 214)
        self.verticalLayout = QtWidgets.QVBoxLayout(SimpleObjectivesWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(SimpleObjectivesWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame)
        self.frame1 = QtWidgets.QFrame(SimpleObjectivesWidget)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setObjectName("frame1")
        self.gridLayout = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout.setObjectName("gridLayout")
        self.exp_nb_lbl = QtWidgets.QLabel(self.frame1)
        self.exp_nb_lbl.setObjectName("exp_nb_lbl")
        self.gridLayout.addWidget(self.exp_nb_lbl, 2, 2, 1, 1)
        self.sharing_lbl = QtWidgets.QLabel(self.frame1)
        self.sharing_lbl.setObjectName("sharing_lbl")
        self.gridLayout.addWidget(self.sharing_lbl, 1, 0, 1, 1)
        self.talk_lbl = QtWidgets.QLabel(self.frame1)
        self.talk_lbl.setObjectName("talk_lbl")
        self.gridLayout.addWidget(self.talk_lbl, 3, 0, 1, 1)
        self.fruition_nb_lbl = QtWidgets.QLabel(self.frame1)
        self.fruition_nb_lbl.setObjectName("fruition_nb_lbl")
        self.gridLayout.addWidget(self.fruition_nb_lbl, 0, 2, 1, 1)
        self.exp_lbl = QtWidgets.QLabel(self.frame1)
        self.exp_lbl.setObjectName("exp_lbl")
        self.gridLayout.addWidget(self.exp_lbl, 2, 0, 1, 1)
        self.fruition_lbl = QtWidgets.QLabel(self.frame1)
        self.fruition_lbl.setObjectName("fruition_lbl")
        self.gridLayout.addWidget(self.fruition_lbl, 0, 0, 1, 1)
        self.sharing_nb_lbl = QtWidgets.QLabel(self.frame1)
        self.sharing_nb_lbl.setObjectName("sharing_nb_lbl")
        self.gridLayout.addWidget(self.sharing_nb_lbl, 1, 2, 1, 1)
        self.talk_nb_lbl = QtWidgets.QLabel(self.frame1)
        self.talk_nb_lbl.setObjectName("talk_nb_lbl")
        self.gridLayout.addWidget(self.talk_nb_lbl, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame1)
        self.credits_lbl = QtWidgets.QLabel(SimpleObjectivesWidget)
        self.credits_lbl.setObjectName("credits_lbl")
        self.verticalLayout.addWidget(self.credits_lbl)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(SimpleObjectivesWidget)
        QtCore.QMetaObject.connectSlotsByName(SimpleObjectivesWidget)

    def retranslateUi(self, SimpleObjectivesWidget):
        _translate = QtCore.QCoreApplication.translate
        SimpleObjectivesWidget.setWindowTitle(_translate("SimpleObjectivesWidget", "Form"))
        self.label.setText(_translate("SimpleObjectivesWidget", "Credits Hub"))
        self.exp_nb_lbl.setText(_translate("SimpleObjectivesWidget", "0"))
        self.sharing_lbl.setText(_translate("SimpleObjectivesWidget", "Sharing"))
        self.talk_lbl.setText(_translate("SimpleObjectivesWidget", "Acculturations"))
        self.fruition_nb_lbl.setText(_translate("SimpleObjectivesWidget", "0"))
        self.exp_lbl.setText(_translate("SimpleObjectivesWidget", "Experimentations"))
        self.fruition_lbl.setText(_translate("SimpleObjectivesWidget", "Fruitions"))
        self.sharing_nb_lbl.setText(_translate("SimpleObjectivesWidget", "0"))
        self.talk_nb_lbl.setText(_translate("SimpleObjectivesWidget", "0"))
        self.credits_lbl.setText(_translate("SimpleObjectivesWidget", "Placeholder"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SimpleObjectivesWidget = QtWidgets.QWidget()
    ui = Ui_SimpleObjectivesWidget()
    ui.setupUi(SimpleObjectivesWidget)
    SimpleObjectivesWidget.show()
    sys.exit(app.exec_())
