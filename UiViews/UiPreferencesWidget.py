# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PreferencesWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PreferencesWidget(object):
    def setupUi(self, PreferencesWidget):
        if not PreferencesWidget.objectName():
            PreferencesWidget.setObjectName(u"PreferencesWidget")
        PreferencesWidget.resize(534, 392)
        self.verticalLayout = QVBoxLayout(PreferencesWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PreferencesFrame = QFrame(PreferencesWidget)
        self.PreferencesFrame.setObjectName(u"PreferencesFrame")
        self.PreferencesFrame.setFrameShape(QFrame.StyledPanel)
        self.PreferencesFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.PreferencesFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.themeOptionsLabel = QLabel(self.PreferencesFrame)
        self.themeOptionsLabel.setObjectName(u"themeOptionsLabel")
        self.themeOptionsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.themeOptionsLabel)

        self.themeOptionsComboBox = QComboBox(self.PreferencesFrame)
        self.themeOptionsComboBox.setObjectName(u"themeOptionsComboBox")

        self.verticalLayout_2.addWidget(self.themeOptionsComboBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.PreferencesFrame)


        self.retranslateUi(PreferencesWidget)

        QMetaObject.connectSlotsByName(PreferencesWidget)
    # setupUi

    def retranslateUi(self, PreferencesWidget):
        PreferencesWidget.setWindowTitle(QCoreApplication.translate("PreferencesWidget", u"Form", None))
        self.themeOptionsLabel.setText(QCoreApplication.translate("PreferencesWidget", u"Theme:", None))
    # retranslateUi

