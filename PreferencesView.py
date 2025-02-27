from icecream import ic

from PySide6.QtWidgets import QWidget
from UiViews.UiPreferencesWidget import Ui_PreferencesWidget
from MyHelperLibrary.Helpers.CustomWindow import CustomWindow
from QSSController import Theme



class PreferencesView(CustomWindow):

    def __init__(self, mainView, qssController):
        super().__init__("Preferences", "", False)

        self.mainView = mainView
        self.qssController = qssController

        self.setWindowTitle("Preferences")
        
        # The primary widget to host the ui content 
        self.container  = QWidget()
        self.setCentralWidget(self.container)

        self.content = Ui_PreferencesWidget()
        self.content.setupUi(self.container)

        # ---- Style ----
        self.setStyle()
        # --------------

        for option in Theme:
            self.content.themeOptionsComboBox.addItem(option.name)

        self.content.themeOptionsComboBox.adjustSize()     # Ensures that the combo box�s size is updated to accommodate the contents of its items
        self.content.themeOptionsComboBox.setCurrentIndex((Theme(self.qssController.currentTheme).value) -1)
        self.content.themeOptionsComboBox.currentIndexChanged.connect(self.changeTheme)
        


    # =============================================================================================


    def setStyle(self):

        stylesheet = self.qssController.getWindowStyle()        
        stylesheet += self.qssController.getContentStyle()
        stylesheet += self.qssController.getPreferencesStyle()
        print(stylesheet)
        self.setStyleSheet(stylesheet)


    # =============================================================================================


    def main(self):
        self.show()

        
    # =============================================================================================


    def changeTheme(self, value):

        self.qssController.setTheme(Theme(value + 1))
        self.setStyle()
        self.mainView.setStyle()