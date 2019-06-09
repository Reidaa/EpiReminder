from PyQt5.QtWidgets import QWidget

from ui.Ui_EventWidget import Ui_EventWidget


class EventWidget(QWidget):
    def __init__(self, parent=None, when: str = "time", what: str = "title", where: str = "room"):
        QWidget.__init__(self, parent)
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
