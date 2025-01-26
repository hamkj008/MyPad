from icecream import ic
from functools import partial

from PySide6.QtWidgets import QMainWindow, QFileDialog, QStatusBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import QFileInfo, Qt

from CustomWindow import CustomWindow
from UiViews.UiMainWindow import Ui_MainWindow
from QSSController import QSSController
from QSSController import ColorTheme
from LineNumberTextEdit import LineNumberTextEdit
from MyHelperLibrary.Helpers.HelperMethods import createChoiceDialog



class View(QMainWindow):

    def __init__(self, controller, filename):
        super().__init__()

        self.controller     = controller
        self.qssController  = QSSController(ColorTheme.DARK)

        self.window = CustomWindow("MyPad", "icons/MyPadIcon.png")
        self.myPadWindow = Ui_MainWindow()
        self.myPadWindow.setupUi(self)
        self.appName = "MyPad"
        self.setWindowIcon(QIcon("icons/MyPadIcon.png"))
        
        # -- Style Sheet --
        self.setStyleSheet(self.qssController.getStyle())
        

        # -- Text Edit -- 
        self.lineNumberTextEdit = LineNumberTextEdit()
        self.lineNumberTextEdit.setObjectName("textEdit")
        self.window.ContentFrame.layout().addWidget(self.lineNumberTextEdit)


        self.window.horizontalSlider.setMinimum(8)      # Minimum value
        self.window.horizontalSlider.setMaximum(60)     # Maximum value
        self.window.horizontalSlider.setValue(self.lineNumberTextEdit.fontSize)
        self.window.horizontalSlider.sliderMoved.connect(self.adjustFont)

  
        # -- Menu bar --
        self.menubar = self.menuBar()
        self.setupMenus()

        # -- Statusbar --
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Characters: ")  


        # -- Signals --
        self.lineNumberTextEdit.textChanged.connect(self.onTextChanged)
        self.window.SaveBtn.clicked.connect(self.saveAs)
        self.window.SaveAsBtn.clicked.connect(self.saveAs)
        self.window.CutBtn.clicked.connect(self.lineNumberTextEdit.cut)
        self.window.CopyBtn.clicked.connect(self.lineNumberTextEdit.copy)
        self.window.PasteBtn.clicked.connect(self.lineNumberTextEdit.paste)
        self.window.ClearBtn.clicked.connect(self.onClear)
        
        self.window.leftBtn.clicked.connect(partial(self.changeFontSize, False))
        self.window.rightBtn.clicked.connect(partial(self.changeFontSize, True))
        
        self.currentFile = None
        self.fileSaved = True
        self.setWindowTitle(self.appName)   # Default window name without file name attached

        if filename:
            self.loadFile(filename)    

        self.previous_text = self.lineNumberTextEdit.toPlainText()


    # =============================================================================================


    def main(self):
        self.show()

        
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

        # ----- File Menu -----
        fileMenu = self.menubar.addMenu("&File")

        # -- Actions --
        newAction           = fileMenu.addAction("New")
        newWindowAction     = fileMenu.addAction("New Window")
        fileMenu.addSeparator()
        openAction          = fileMenu.addAction("Open")
        fileMenu.addSeparator()
        saveAction          = fileMenu.addAction("Save")            # TO DO
        saveAsAction        = fileMenu.addAction("Save As")
        fileMenu.addSeparator()
        quitAction          = fileMenu.addAction("Exit")
        
        newAction.triggered.connect(self.newFile)
        newWindowAction.triggered.connect(self.newFileWindow)
        openAction.triggered.connect(self.openFile)
        saveAsAction.triggered.connect(self.saveAs)
        quitAction.triggered.connect(self.quitApp)


        # ----- Edit menu ------
        editMenu = self.menubar.addMenu("&Edit")

        # -- Actions --
        undoAction  = editMenu.addAction("Undo")
        redoAction  = editMenu.addAction("Redo")
        editMenu.addSeparator()
        cutAction   = editMenu.addAction("Cut")
        copyAction  = editMenu.addAction("Copy")
        pasteAction = editMenu.addAction("Paste")
        
        undoAction.triggered.connect(self.lineNumberTextEdit.undo)
        redoAction.triggered.connect(self.lineNumberTextEdit.redo)
        cutAction.triggered.connect(self.lineNumberTextEdit.cut)
        copyAction.triggered.connect(self.lineNumberTextEdit.copy)
        pasteAction.triggered.connect(self.lineNumberTextEdit.paste)


    # =============================================================================================


    def onTextChanged(self):

        # Prevent painting from triggering on text change every frame
        current_text = self.lineNumberTextEdit.toPlainText()
        if current_text != self.previous_text:
            self.previous_text = current_text
            self.fileSaved = False

            if self.currentFile:
                self.setWindowTitle(f"{self.appName} - {self.currentFile}*")

            else:
                self.setWindowTitle(f"{self.appName} - *")

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
            
        self.setWindowTitle(self.appName)
        self.previous_text = ""
        self.lineNumberTextEdit.clear()
        self.lineNumberTextEdit.lineCount = 1


    # =============================================================================================


    def save(self):
        
        if self.currentFile:
            try:
                with open(self.currentFilePath, "w") as file:
                    file.write(self.lineNumberTextEdit.toPlainText())

                self.setWindowTitle(f"{self.appName} - {self.currentFile}")
                self.fileSaved = True
                ic(f"File saved: {self.currentFile}")
                
            except IOError as e:
                ic("Error saving file")
                
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
                self.setWindowTitle(f"{self.appName} - {self.currentFile}")
                self.fileSaved = True
                ic(f"File saved as: {self.currentFilePath}")
                
            except IOError as e:
                ic("Error saving file")


    # =============================================================================================
    

    def openFile(self):

        self.currentFilePath, _ = QFileDialog.getOpenFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")

        if self.currentFilePath:
            try:
                with open(self.currentFilePath, "r") as file:
                    self.lineNumberTextEdit.clear()
                    self.lineNumberTextEdit.setText(file.read())
                    self.currentFile = QFileInfo(self.currentFilePath).fileName()
                    self.setWindowTitle(f"{self.appName} - {self.currentFile}") 

            except IOError as e:
                ic("Error opening file")
                
    # =============================================================================================


    def loadFile(self, filename):

        self.currentFilePath = filename

        try:
            with open(filename, "r") as file:
                self.lineNumberTextEdit.setText(file.read())
                self.currentFile = QFileInfo(self.currentFilePath).fileName()
                self.setWindowTitle(f"{self.appName} - {self.currentFile}") 
           
        except IOError as e:
                ic("Error loading file")


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

            self.window.horizontalSlider.setValue(self.lineNumberTextEdit.fontSize)
        

    # =============================================================================================
    

    def newFile(self):
        self.controller.main()
        

    def newFileWindow(self):
        self.close()
        self.controller.main()


    # =============================================================================================
    