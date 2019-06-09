import datetime

from PyQt5.QtWidgets import QWidget

from Intra.API import API
from ui.Ui_SimpleObjectivesWidget import Ui_SimpleObjectivesWidget


class SimpleObjectivesWidget(QWidget):
    def __init__(self, parent=None, intra: API = None):
        if intra is None:
            return
        QWidget.__init__(self, parent=parent)
        self.ui = Ui_SimpleObjectivesWidget()
        self.intra = intra
        self.date = datetime.date.today()

        self._get_activities()
        # self._conf_ui()
        # self._conf_signals()

    def _conf_ui(self):
        self.ui.setupUi(self)

    def _conf_signals(self):
        pass

    def _get_activities(self):
        pass


if __name__ == "__main__":
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open("../../log.txt") as file:
        lines = file.readlines()
    intra = API(lines[0], lines[1])
    thing = SimpleObjectivesWidget(intra=intra)
    # LoggingWidget = QtWidgets.QWidget()
    # ui = Ui_LoggingWidget()
    # ui.setupUi(LoggingWidget)
    # LoggingWidget.show()
    # thing.show()
    # sys.exit(app.exec_())
