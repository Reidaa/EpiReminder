from PyQt5 import QtWidgets


def clear_layout(layout: QtWidgets.QLayout) -> None:
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)
