# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyPad.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1378, 819)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 0)
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ButtonFrame = QFrame(self.MainFrame)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonFrame.sizePolicy().hasHeightForWidth())
        self.ButtonFrame.setSizePolicy(sizePolicy)
        self.ButtonFrame.setMaximumSize(QSize(16777215, 90))
        self.ButtonFrame.setBaseSize(QSize(0, 0))
        self.ButtonFrame.setStyleSheet(u"")
        self.ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ButtonFrame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SaveBtn = QPushButton(self.ButtonFrame)
        self.SaveBtn.setObjectName(u"SaveBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SaveBtn.sizePolicy().hasHeightForWidth())
        self.SaveBtn.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/save-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveBtn.setIcon(icon)
        self.SaveBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.SaveBtn)

        self.SaveAsBtn = QPushButton(self.ButtonFrame)
        self.SaveAsBtn.setObjectName(u"SaveAsBtn")
        sizePolicy1.setHeightForWidth(self.SaveAsBtn.sizePolicy().hasHeightForWidth())
        self.SaveAsBtn.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/save-as-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveAsBtn.setIcon(icon1)
        self.SaveAsBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.SaveAsBtn)

        self.line = QFrame(self.ButtonFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.CutBtn = QPushButton(self.ButtonFrame)
        self.CutBtn.setObjectName(u"CutBtn")
        sizePolicy1.setHeightForWidth(self.CutBtn.sizePolicy().hasHeightForWidth())
        self.CutBtn.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/cut-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CutBtn.setIcon(icon2)
        self.CutBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.CutBtn)

        self.CopyBtn = QPushButton(self.ButtonFrame)
        self.CopyBtn.setObjectName(u"CopyBtn")
        sizePolicy1.setHeightForWidth(self.CopyBtn.sizePolicy().hasHeightForWidth())
        self.CopyBtn.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/copy-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CopyBtn.setIcon(icon3)
        self.CopyBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.CopyBtn)

        self.PasteBtn = QPushButton(self.ButtonFrame)
        self.PasteBtn.setObjectName(u"PasteBtn")
        sizePolicy1.setHeightForWidth(self.PasteBtn.sizePolicy().hasHeightForWidth())
        self.PasteBtn.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/paste-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PasteBtn.setIcon(icon4)
        self.PasteBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.PasteBtn)

        self.line_2 = QFrame(self.ButtonFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.ClearBtn = QPushButton(self.ButtonFrame)
        self.ClearBtn.setObjectName(u"ClearBtn")
        sizePolicy1.setHeightForWidth(self.ClearBtn.sizePolicy().hasHeightForWidth())
        self.ClearBtn.setSizePolicy(sizePolicy1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/clear-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ClearBtn.setIcon(icon5)
        self.ClearBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.ClearBtn)


        self.verticalLayout_2.addWidget(self.ButtonFrame)

        self.ContentFrame = QFrame(self.MainFrame)
        self.ContentFrame.setObjectName(u"ContentFrame")
        sizePolicy.setHeightForWidth(self.ContentFrame.sizePolicy().hasHeightForWidth())
        self.ContentFrame.setSizePolicy(sizePolicy)
        self.ContentFrame.setStyleSheet(u"")
        self.ContentFrame.setFrameShape(QFrame.StyledPanel)
        self.ContentFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.ContentFrame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.numVBox = QVBoxLayout()
        self.numVBox.setObjectName(u"numVBox")

        self.horizontalLayout.addLayout(self.numVBox)

        self.textEdit = QTextEdit(self.ContentFrame)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addWidget(self.ContentFrame)

        self.HBoxFrame = QFrame(self.MainFrame)
        self.HBoxFrame.setObjectName(u"HBoxFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.HBoxFrame.sizePolicy().hasHeightForWidth())
        self.HBoxFrame.setSizePolicy(sizePolicy3)
        self.HBoxFrame.setFrameShape(QFrame.StyledPanel)
        self.HBoxFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.HBoxFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.leftBtn = QPushButton(self.HBoxFrame)
        self.leftBtn.setObjectName(u"leftBtn")
        sizePolicy1.setHeightForWidth(self.leftBtn.sizePolicy().hasHeightForWidth())
        self.leftBtn.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/back-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftBtn.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.leftBtn)

        self.horizontalSlider = QSlider(self.HBoxFrame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy1.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.rightBtn = QPushButton(self.HBoxFrame)
        self.rightBtn.setObjectName(u"rightBtn")
        sizePolicy1.setHeightForWidth(self.rightBtn.sizePolicy().hasHeightForWidth())
        self.rightBtn.setSizePolicy(sizePolicy1)
        icon7 = QIcon()
        icon7.addFile(u":/icons/forward-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rightBtn.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.rightBtn)


        self.verticalLayout_2.addWidget(self.HBoxFrame)


        self.verticalLayout.addWidget(self.MainFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1378, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SaveBtn.setText(QCoreApplication.translate("MainWindow", u"  Save", None))
        self.SaveAsBtn.setText(QCoreApplication.translate("MainWindow", u"  Save As", None))
        self.CutBtn.setText("")
        self.CopyBtn.setText("")
        self.PasteBtn.setText("")
        self.ClearBtn.setText(QCoreApplication.translate("MainWindow", u"  Clear", None))
        self.leftBtn.setText("")
        self.rightBtn.setText("")
    # retranslateUi

