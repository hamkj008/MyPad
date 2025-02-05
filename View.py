from icecream import ic
from functools import partial
from PySide6.QtWidgets import QWidget, QFileDialog, QStatusBar
from PySide6.QtCore import QFileInfo

from UiViews.UiMainWindow2 import Ui_MainWidget
from QSSController import QSSController, ColorTheme
from LineNumberTextEdit import LineNumberTextEdit
from MyHelperLibrary.Helpers.HelperMethods import createChoiceDialog, createActionDictionary, createMenu
from MyHelperLibrary.Helpers.CustomWindow import CustomWindow
from PreferencesView import PreferencesView


class View(CustomWindow):

    def __init__(self, controller, filename):

        iconPath = "E:/MyITstuff/ProgrammingIDEs/VisualStudio/Python/Projects/MyPad/MyPad/icons/MyPadIcon.png"        # have to pass an absolute path
        super().__init__("MyPad", iconPath, True)
        # ----------------------

        self.controller = controller
        
        self.appName    = "MyPad"
        self.setMinimumSize(700, 500)

        # The primary widget to host the ui content 
        self.container  = QWidget()

        # -- Style --
        self.qssController  = QSSController(ColorTheme.DARK)
        self.setStyle()
        # ------------

        self.content = Ui_MainWidget()
        self.content.setupUi(self.container)

        self.setCentralWidget(self.container)
        

        # -- Custom Text Edit -- 
        self.lineNumberTextEdit = LineNumberTextEdit()
        self.lineNumberTextEdit.setObjectName("textEdit")
        self.content.ContentFrame.layout().addWidget(self.lineNumberTextEdit)


        # -- Font change sliders --
        self.content.horizontalSlider.setMinimum(8)      # Minimum value
        self.content.horizontalSlider.setMaximum(60)     # Maximum value
        self.content.horizontalSlider.setValue(self.lineNumberTextEdit.fontSize)
        self.content.horizontalSlider.sliderMoved.connect(self.adjustFont)
        
        self.previous_text  = self.lineNumberTextEdit.toPlainText()
  
        # -- Menu bar --
        self.setupMenus()

        # -- Statusbar --
        self.setStatusBar(QStatusBar(self))
        self.statusBar().setSizeGripEnabled(False)
        self.statusBar().showMessage("Characters: ")  

        # -- Signals --
        self.lineNumberTextEdit.textChanged.connect(self.onTextChanged)
        self.content.SaveBtn.clicked.connect(self.save)
        self.content.SaveAsBtn.clicked.connect(self.saveAs)
        self.content.CutBtn.clicked.connect(self.lineNumberTextEdit.cut)
        self.content.CopyBtn.clicked.connect(self.lineNumberTextEdit.copy)
        self.content.PasteBtn.clicked.connect(self.lineNumberTextEdit.paste)
        self.content.ClearBtn.clicked.connect(self.onClear)
        
        self.content.leftBtn.clicked.connect(partial(self.changeFontSize, False))
        self.content.rightBtn.clicked.connect(partial(self.changeFontSize, True))
        
        self.currentFile    = None
        self.fileSaved      = True

        if filename:
            self.loadFile(filename)    


    # =============================================================================================


    def main(self):
        self.show()

        
    # =============================================================================================


    def setStyle(self):

        stylesheet = self.qssController.getWindowStyle()
        stylesheet += self.qssController.getContentStyle()
        self.setStyleSheet(stylesheet)


    # =============================================================================================


    def quitApp(self):

        if not self.fileSaved:
            if createChoiceDialog("File not saved", """The curent file has not been saved. 
                                    \nWould you like to save it?"""):
                if self.currentFile:
                    self.saveAs()
                else:
                    self.save()

        self.controller.quitApp()


    # =============================================================================================
        

    def setupMenus(self):

        self.menuList = {}
        # ----- File Menu -----
        newAction           = createActionDictionary("New", trigger=self.newFile)
        newWindowAction     = createActionDictionary("New Window", trigger=self.newFileWindow)
        openAction          = createActionDictionary("Open", trigger=self.openFile)
        saveAction          = createActionDictionary("Save", trigger=self.save)         
        saveAsAction        = createActionDictionary("Save As", trigger=self.saveAs)
        quitAction          = createActionDictionary("Exit", trigger=self.quitApp)

        fileActionList = [newAction, newWindowAction, "separator", openAction, "separator", saveAction, saveAsAction, quitAction]
        self.menuList["fileMenu"] = createMenu(self.menubar, "File", fileActionList)
        

        # ----- Edit Menu -----
        undoAction  = createActionDictionary("Undo", trigger=self.lineNumberTextEdit.undo)
        redoAction  = createActionDictionary("Redo", trigger=self.lineNumberTextEdit.redo)
        cutAction   = createActionDictionary("Cut", trigger=self.lineNumberTextEdit.cut)
        copyAction  = createActionDictionary("Copy", trigger=self.lineNumberTextEdit.copy)
        pasteAction = createActionDictionary("Paste", trigger=self.lineNumberTextEdit.paste)

        editActionList = [undoAction, redoAction, "separator", cutAction, copyAction, pasteAction]
        self.menuList["editMenu"]    = createMenu(self.menubar, "Edit", editActionList)


        # ----- Settings menu ------
        openPreferencesAction   =   createActionDictionary("Preferences", shortcut="Ctrl+P", trigger=self.displayPreferencesView)
        actionList              =   [openPreferencesAction]
        
        self.menuList["settingsMenu"] = createMenu(self.menubar, "Settings", actionList)


    # =============================================================================================


    def onTextChanged(self):

        # Prevent painting from triggering on text change every frame
        current_text = self.lineNumberTextEdit.toPlainText()
        if current_text != self.previous_text:
            self.previous_text = current_text
            self.fileSaved = False

            if self.currentFile:
                self.titleLabel.setText(f"{self.appName} - {self.currentFile}*")

            else:
                self.titleLabel.setText(f"{self.appName} - *")

        # Status bar display
        self.statusBar().showMessage("Characters: " + str(len(self.lineNumberTextEdit.toPlainText())) + "    Lines: " + str(self.lineNumberTextEdit.document().blockCount()))      


    # =============================================================================================


    def onClear(self):
        ic("clear")

        if self.currentFile:
            if not createChoiceDialog("Clear current file", "There is a file loaded. Are you sure you want to clear it?"):
                return
            else:
                self.currentFile = None
            
        self.titleLabel.setText(self.appName)
        self.previous_text = ""
        self.lineNumberTextEdit.clear()
        self.lineNumberTextEdit.lineCount = 1


    # =============================================================================================


    def save(self):
        
        if self.currentFile:
            try:
                with open(self.currentFilePath, "w") as file:
                    file.write(self.lineNumberTextEdit.toPlainText())

                self.titleLabel.setText(f"{self.appName} - {self.currentFile}")
                self.fileSaved = True
                ic(f"File saved: {self.currentFile}")
                
            except IOError as e:
                ic("Error saving file {e}")
                
        else:
            # If no file is open yet, trigger Save As
            self.saveAs()


    # =============================================================================================

    def saveAs(self):

        self.currentFilePath, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")

        if self.currentFilePath:
            try:
                with open(self.currentFilePath, "w") as file:
                    file.write(self.lineNumberTextEdit.toPlainText())

                self.currentFile = QFileInfo(self.currentFilePath).fileName()
                self.titleLabel.setText(f"{self.appName} - {self.currentFile}")
                self.fileSaved = True
                ic(f"File saved as: {self.currentFilePath}")
                
            except IOError as e:
                ic("Error saving file {e}")


    # =============================================================================================
    

    def openFile(self):

        self.currentFilePath, _ = QFileDialog.getOpenFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")

        if self.currentFilePath:
            try:
                with open(self.currentFilePath, "r") as file:
                    self.lineNumberTextEdit.clear()
                    self.lineNumberTextEdit.setText(file.read())
                    self.currentFile = QFileInfo(self.currentFilePath).fileName()
                    self.titleLabel.setText(f"{self.appName} - {self.currentFile}")

            except IOError as e:
                ic("Error opening file {e}")
                
    # =============================================================================================


    def loadFile(self, filename):

        self.currentFilePath = filename

        try:
            with open(filename, "r") as file:
                self.lineNumberTextEdit.setText(file.read())
                self.currentFile = QFileInfo(self.currentFilePath).fileName()
                self.titleLabel.setText(f"{self.appName} - {self.currentFile}")
           
        except IOError as e:
                ic("Error loading file {e}")


    # =============================================================================================
    

    def changeFontSize(self, bigger):
        
        size = self.lineNumberTextEdit.fontSize

        if bigger:
            size += 5
            self.adjustFont(size)
 
        else:
            size -= 5
            self.adjustFont(size) 
        

    # =============================================================================================
    
    
    def adjustFont(self, fontSize):
        ic(fontSize)

        if fontSize > 8 and fontSize < 60:
            self.lineNumberTextEdit.fontSize = fontSize

            self.content.horizontalSlider.setValue(self.lineNumberTextEdit.fontSize)
        

    # =============================================================================================
    

    def newFile(self):
        self.controller.main()
        

    def newFileWindow(self):
        self.close()
        self.controller.main()


    # =============================================================================================
    

    # =================================   VIEWS    ===========================================


    def displayPreferencesView(self):
        ic("displayPreferencesView")
        
        self.preferencesView = PreferencesView(self, self.qssController)
        self.preferencesView.main()
    

    def closePreferencesView(self):
        self.preferencesView.close()
        

    # ========================================================================================