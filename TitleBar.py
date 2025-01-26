from PySide6.QtWidgets import QWidget, QLabel, QPushButton
from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtGui import QIcon, QCursor, QPixmap

class TitleBar(QWidget):
    def __init__(self, windowName, windowIcon):
        super().__init__()
        self.setFixedHeight(32)


        titleBar = QWidget(self, objectName="titleBar")
        titleBar.setFixedHeight(50)
        titleBar.setMinimumWidth(500)

        iconLabel = QLabel(objectName="windowIcon", parent=self)
        iconLabel.setPixmap(QIcon(windowIcon).pixmap(25, 25))
        iconLabel.move(8, 0)

        titleLabel = QLabel(windowName, titleBar, objectName="titleLabel")
        titleLabel.move(40, 0)
        titleLabel.setFixedWidth(self.width() - 150)

        self.minBtn     = QPushButton(QIcon("icons/minimize"), "", objectName="titleBarButton", parent=self)
        self.maxBtn     = QPushButton(QIcon("icons/maximize"), "", objectName="titleBarButton", parent=self)
        self.closeBtn   = QPushButton(QIcon("icons/close_window"), "", objectName="titleBarButton", parent=self)

        self.minBtn.setFixedWidth(

        self.closeBtn.move(self.width() - , 0)
        self.maxBtn.move(self.width() - 92, 0)
        self.minBtn.move(self.width() - 138, 0)

