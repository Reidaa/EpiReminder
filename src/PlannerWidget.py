import datetime

from PyQt5.QtWidgets import QWidget

from EventWidget import EventWidget
from Intra.API import API
from Utils import clear_layout
from ui.Ui_PlannerWidget import Ui_PlannerWidget


class PlannerWidget(QWidget):
    def __init__(self, parent=None, intra: API = None):
        QWidget.__init__(self, parent)
        self.ui = Ui_PlannerWidget()
        self.intra = intra
        self.date = datetime.date.today()

        self._conf_ui()
        self._conf_signal()

        pass

    def _conf_ui(self):
        self.ui.setupUi(self)
        self._update_date()
        self._add_events()

    def _conf_signal(self):
        self.ui.right_arrow_button.clicked.connect(self._tomorrow)
        self.ui.left_arrow_button.clicked.connect(self._yesterday)

    def _reload_ui(self):
        clear_layout(self.ui.events_layout)
        self._update_date()
        self._add_events()

    def _add_events(self):
        events = self.intra.get_planning(start=str(self.date), end=str(self.date))
        events = [i for i in events if i.is_registered == True]
        for i, val in enumerate(events):
            self.ui.events_layout.addWidget(EventWidget(parent=self,
                                                        when=val.when,
                                                        what=val.what,
                                                        where=val.where))

    def _tomorrow(self):
        self.date += datetime.timedelta(days=1)
        self._reload_ui()

    def _yesterday(self):
        self.date -= datetime.timedelta(days=1)
        self._reload_ui()

    def _update_date(self):
        self.ui.date_lbl.setText("{day} {number} {month} {year}".format(day=self.date.strftime('%A').capitalize(),
                                                                        number=str(self.date.day),
                                                                        month=self.date.strftime("%B"),
                                                                        year=str(self.date.year)))


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open("../../log.txt") as file:
        lines = file.readlines()
    intra = API(lines[0], lines[1])
    thing = PlannerWidget(intra=intra)
    # LoggingWidget = QtWidgets.QWidget()
    # ui = Ui_LoggingWidget()
    # ui.setupUi(LoggingWidget)
    # LoggingWidget.show()
    thing.show()
    sys.exit(app.exec_())
