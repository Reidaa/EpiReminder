from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy
from qroundprogressbar import QRoundProgressBar

from moduleapi import ModuleAPI
from ui.Ui_HelpObjectivesWidget import Ui_HelpObjectivesWidget
from ui.Ui_ObjectivesWidget import Ui_ObjectivesWidget


class ObjectiveData:
    def __init__(self, username: str = None, token: str = None):
        self.api = ModuleAPI(username, token)
        self.username = username
        self.talks = []
        self.workshops = []
        self.focus_groups = []
        self.hackathons = []
        self.sharings = []
        self.makers = []
        self.credits = 0

    def is_sharing(self, title: str) -> bool:
        index = title.find(self.username)
        return False if index == -1 else True

    def get_goals(self):
        self.get_workshops()
        self.get_talks()
        self.get_hackathons()
        self.get_makers()
        self.get_sharings()

    def get_credits(self):
        pass

    def get_talks(self):
        print("talks")
        self.talks = self.api.get_user_activities(academicyear=self.api.get_current_academic_year(),
                                                  codemodule="B-INN-001",
                                                  codeinstance=self.api.get_user_codeinstance())

    def get_workshops(self):
        print("workshops")
        self.workshops = self.api.get_user_activities(academicyear=self.api.get_current_academic_year(),
                                                      codemodule="B-INN-000",
                                                      codeinstance=self.api.get_user_codeinstance())

    def get_sharings(self):
        self.sharings = self.api.get_all_activities(academicyear=self.api.get_current_academic_year(),
                                                    codemodule="B-INN-001",
                                                    codeinstance=self.api.get_user_codeinstance())
        self.sharings = [i for i in self.sharings if len(i.events) != 0 and self.is_sharing(i.title)]

    def get_hackathons(self):
        pass

    def get_makers(self):
        pass


class ProgressionWidget(QWidget):
    def __init__(self, parent: QWidget, title: str, maxi: int, value: int):
        QWidget.__init__(self, parent)
        self.vertical_layout = QVBoxLayout(self)
        self.setLayout(self.vertical_layout)
        self.label = QLabel(self)
        self.progress = QRoundProgressBar(self)
        self.title = title
        self.max = maxi
        self.value = value

        self.__conf_ui()

    def __conf_ui(self):
        self.progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)
        self.progress.setMaximum(self.max)
        self.progress.setMinimum(0)

        self.label.setText(self.title)
        self.label.setAlignment(Qt.AlignCenter)
        self.set_value(self.value)
        self.vertical_layout.addWidget(self.progress, Qt.AlignCenter)
        self.vertical_layout.addWidget(self.label)
        self.setMinimumHeight(160)
        self.setMinimumWidth(140)

    def set_value(self, value: int):
        self.value = value
        self.progress.setValue(self.value)
        self.progress.setFormat('{v}/{max}'.format(v=str(self.value), max=str(self.progress.maximum())))


# class MakersProgressionWidget(QWidget):
#     def __init__(self, parent: QWidget, title: str, maxi: int, value: int):
#         QWidget.__init__(self, parent)
#         self.vertical_layout = QVBoxLayout(self)
#         self.setLayout(self.vertical_layout)
#         self.spinbox = QSpinBox(self)
#         self.progress = QRoundProgressBar(self)
#         self.title = title
#         self.max = maxi
#         self.value = value
#
#         self.__conf_ui()
#
#     def __conf_ui(self):
#         self.progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)
#         self.progress.setMaximum(self.max)
#         self.progress.setMinimum(0)
#
#         self.spinbox.setAlignment(Qt.AlignCenter)
#         self.set_value(self.value)
#         self.vertical_layout.addWidget(self.progress, Qt.AlignCenter)
#         self.vertical_layout.addWidget(self.spinbox)
#         self.setMinimumHeight(160)
#         self.setMinimumWidth(140)
#
#     def set_value(self, value: int):
#         self.value = value
#         self.progress.setValue(self.value)
#         self.progress.setFormat('{v}/{max}'.format(v=str(self.value), max=str(self.progress.maximum())))


class ObjectivesWidget(QWidget, Ui_ObjectivesWidget):
    def __init__(self, parent=None, username: str = None, token: str = None):
        if username is None or token is None:
            return
        QWidget.__init__(self, parent=parent)
        self._data = ObjectiveData(username, token)
        self.acculturation = 0
        self.experimentation = 0
        self.fruition = 0
        self.sharing = 0

        self._conf_ui()
        self._conf_signals()

    def _conf_ui(self):
        self.setupUi(self)
        self.acculturation_progress = ProgressionWidget(self, "HubTalk", 4, 0)
        self.experimentation_progress = ProgressionWidget(self, "Experimentation", 3, 0)
        # self.fruition_progress = MakersProgressionWidget(self, "Maker", 2, 0)
        self.sharing_progress = ProgressionWidget(self, "Sharing", 2, 0)
        self.horizontalLayout.setSpacing(3)

        self.horizontalLayout.addWidget(self.acculturation_progress)
        # self.horizontalLayout.addWidget(self.fruition_progress)
        self.horizontalLayout.addWidget(self.experimentation_progress)
        self.horizontalLayout.addWidget(self.sharing_progress)
        self.horizontalLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding))
        self.reload()

    def _conf_signals(self):
        pass

    def _reload_goals(self):
        self._data.get_goals()
        self.acculturation = len(self._data.talks)
        self.experimentation = len(self._data.workshops) + (2 * len(self._data.focus_groups)) + (
                2 * len(self._data.hackathons))
        self.fruition = len(self._data.makers)
        self.sharing = len(self._data.sharings)

    def _update_ui(self):
        self.acculturation_progress.set_value(self.acculturation)
        self.experimentation_progress.set_value(self.experimentation)
        self.sharing_progress.set_value(self.sharing)
        # self.fruition_progress.set_value(self.fruition)

    def reload(self):
        self._reload_goals()
        self._update_ui()


class HelpObjectiveWidget(QWidget, Ui_HelpObjectivesWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._conf_ui()

    def _conf_ui(self):
        self.setupUi(self)


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys

    with open("../log.txt") as file:
        lines = file.readlines()
    app = QtWidgets.QApplication(sys.argv)
    thing = ObjectivesWidget(username=lines[0][:-1], token=lines[1][:-1])
    thing.show()
    sys.exit(app.exec_())

    # thing = ObjectiveData(username=lines[0][:-1], token=lines[1][:-1])
    # thing.get_goals()
