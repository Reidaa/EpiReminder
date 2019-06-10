from PyQt5.QtWidgets import QWidget

from ModuleAPI import ModuleAPI
from ui.Ui_SimpleObjectivesWidget import Ui_SimpleObjectivesWidget


class ObjectiveData:
    def __init__(self, username: str = None, token: str = None):
        self.api = ModuleAPI(username, token)
        self.talks = []
        self.workshops = []
        self.focus_groups = []
        self.hackathons = []
        self.sharings = []
        self.makers = []

    def get_activities(self):
        self.talks = self.api.get_user_activities(academicyear=self.api.get_current_academic_year(),
                                                  codemodule="B-INN-001",
                                                  codeinstance=self.api.get_user_codeinstance())
        self.workshops = self.api.get_user_activities(academicyear=self.api.get_current_academic_year(),
                                                      codemodule="B-INN-000",
                                                      codeinstance=self.api.get_user_codeinstance())

    def get_sharings(self):
        pass

    def get_hackathons(self):
        pass


class SimpleObjectivesWidget(QWidget, Ui_SimpleObjectivesWidget):
    def __init__(self, parent=None, username: str = None, token: str = None):
        if username is None or token is None:
            return
        QWidget.__init__(self, parent=parent)
        self._data = ObjectiveData(username, token)
        self.acculturation = 0
        self.experimentation = 0
        self.fruiton = 0
        self.sharing = 0
        self._conf_ui()
        self._conf_signals()

    def _conf_ui(self):
        self.setupUi(self)
        self._update_goals()
        self._update_ui()

    def _conf_signals(self):
        pass

    def _update_goals(self):
        self._data.get_activities()
        self.acculturation = len(self._data.talks)
        self.experimentation = len(self._data.workshops) + (2 * len(self._data.focus_groups)) + (2 * len(self._data.hackathons))
        self.fruition = len(self._data.makers)
        self.sharing = len(self._data.sharings)

    def _update_ui(self):
        self.talk_nb_lbl.setText(str(self.acculturation))
        self.exp_nb_lbl.setText(str(self.experimentation))
        self.fruition_nb_lbl.setText(str(self.fruition))
        self.sharing_nb_lbl.setText(str(self.sharing))

    def reload(self):
        self._update_goals()
        self._update_ui()


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys

    app = QtWidgets.QApplication(sys.argv)
    with open("../log.txt") as file:
        lines = file.readlines()
    thing = SimpleObjectivesWidget(username=lines[0], token=lines[1])
    thing.show()
    sys.exit(app.exec_())
