import datetime

from PyQt5.QtWidgets import QFrame

from planningapi import PlanningAPI
from ui.Ui_EventWidget import Ui_EventWidget
from ui.Ui_PlanningWidget import Ui_PlanningWidget
from utils import clear_layout


class PlanningData:
    def __init__(self, username: str, token: str):
        self.api = PlanningAPI(username, token)
        self.events = []
        self.date = datetime.date.today()

    def get_events(self):
        events = self.api.get_planning(start=str(self.date), end=str(self.date))
        self.events = [i for i in events if i.is_registered() is True]
        pass


class EventWidget(QFrame):
    def __init__(self, parent=None, when: str = "time", what: str = "title", where: str = "room"):
        QFrame.__init__(self, parent)
        self.ui = Ui_EventWidget()
        self.param = {
            "time": when,
            "title": what,
            "location": where
        }

        self.conf_ui()

    def conf_ui(self):
        self.ui.setupUi(self)
        self.ui.hours_lbl.setText(self.param["time"])
        self.ui.title_lbl.setText(self.param["title"])
        self.ui.room_lbl.setText(self.param["location"])
        self.setFrameStyle(QFrame.Raised)
        self.setFrameShape(QFrame.StyledPanel)


class PlanningWidget(QFrame, Ui_PlanningWidget):
    def __init__(self, parent, username: str, token: str):
        QFrame.__init__(self, parent)
        self.__data = PlanningData(username, token)

        self._conf_ui()
        self._conf_signal()

        pass

    def _conf_ui(self):
        self.setupUi(self)
        self._update_date()
        self._add_events()
        self.setFrameStyle(QFrame.Raised)
        self.setFrameShape(QFrame.StyledPanel)

    def _conf_signal(self):
        self.right_arrow_button.clicked.connect(self._tomorrow)
        self.left_arrow_button.clicked.connect(self._yesterday)

    def _update_date(self):
        self.date_lbl.setText("{day} {number} {month} {year}".format(day=self.__data.date.strftime('%A').capitalize(),
                                                                     number=str(self.__data.date.day),
                                                                     month=self.__data.date.strftime("%B"),
                                                                     year=str(self.__data.date.year)))

    def _add_events(self):
        self.__data.get_events()
        for i, val in enumerate(self.__data.events):
            self.events_layout.addWidget(EventWidget(parent=self,
                                                     when=val.when,
                                                     what=val.what,
                                                     where=val.where))

    def _tomorrow(self):
        self.__data.date += datetime.timedelta(days=1)
        self._reload_ui()

    def _yesterday(self):
        self.__data.date -= datetime.timedelta(days=1)
        self._reload_ui()

    def _reload_ui(self):
        clear_layout(self.events_layout)
        self._update_date()
        self._add_events()


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys

    with open("../log.txt") as file:
        lines = file.readlines()
    app = QtWidgets.QApplication(sys.argv)
    thing = PlanningWidget(None, lines[0][:-1], lines[1][:-1])
    thing.show()
    sys.exit(app.exec_())

    # thing = PlanningData(lines[0][:-1], lines[1][:-1])
    # thing.date += datetime.timedelta(days=1)
    # thing.date += datetime.timedelta(days=1)
    # thing.date += datetime.timedelta(days=1)
    # thing.get_events()
    pass
