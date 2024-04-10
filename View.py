from icecream import ic

from PySide6.QtWidgets import QMainWindow, QFileDialog, QStatusBar, QVBoxLayout, QPushButton, QLabel, QTextEdit
from UiViews.UiMainWindow import Ui_MainWindow
from PySide6.QtCore import Qt
from functools import partial



class View(QMainWindow):

    
    def __init__(self, controller, filename):
        super().__init__()
        self.controller = controller

        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.setWindowTitle("My Pad")
        
        self.setFixedSize(1000, 1000)
        
        # -- Style Sheet --
        self.setStyleSheet("""#centralwidget {
                               background-color: #686b6d;
                               }
                               #ButtonFrame, #ContentFrame{ 
                                    background-color: #343335;
                                    border: 3px solid black;
                               }

                                #numLine, #firstLabel {
                                    color: #b620fc;
                                }

                                #textEdit{
                                    background-color: black;
                                    color: #26ea10;                                    
                                }
                           
                                #SaveBtn, #SaveAsBtn, #CutBtn, #CopyBtn, #PasteBtn, #ClearBtn {
                                    background-color: #4470f4;
                                    font: 14pt "Ariel";
                                    font-weight: 600;
	                                color: black;
                                    border: 3px solid black;	
                                    padding: 15px;
                                }""")
        

        # -- Text Edit -- 
        self.textEdit = self.window.textEdit
        self.fontSize = 20
        self.window.horizontalSlider.setValue(self.fontSize)
        self.window.horizontalSlider.sliderMoved.connect(self.adjustFont)
        self.adjustFont(self.fontSize)
        
        font = self.textEdit.font()
        font.setPointSize(self.fontSize)
        self.textEdit.setFont(font)

        
        self.cursor = self.textEdit.textCursor()
        self.lineNumber = self.cursor.blockNumber() + 1
        numLine = QLabel(str(self.lineNumber))
        numLine.setObjectName("numLine")
        self.window.numVBox.addWidget(numLine)
        self.adjustFont(self.fontSize)
        
  
        # -- Menu bar --
        self.menubar = self.menuBar()
        self.setupMenus()

        # -- Statusbar --
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Characters: ")  


        # -- Initialize UI / Buttons --
        self.window.numVBox.setAlignment(Qt.AlignTop)
        self.window.numVBox.setSpacing(0)
        self.window.numVBox.setContentsMargins(0,5,0,0)
        

        # -- Signals --
        self.textEdit.textChanged.connect(self.onTextChanged)
        self.window.SaveBtn.clicked.connect(self.saveAs)
        self.window.SaveAsBtn.clicked.connect(self.saveAs)
        self.window.CutBtn.clicked.connect(self.textEdit.cut)
        self.window.CopyBtn.clicked.connect(self.textEdit.copy)
        self.window.PasteBtn.clicked.connect(self.textEdit.paste)
        self.window.ClearBtn.clicked.connect(self.textEdit.clear)
        
        self.window.leftBtn.clicked.connect(partial(self.changeFontSize, False))
        self.window.rightBtn.clicked.connect(partial(self.changeFontSize, True))
        
        if filename:
            self.loadFile(filename)    


    # -------------------------------------------------------------------------


    def main(self):
        self.show()

        
    # -------------------------------------------------------------------------


    def quitApp(self):
        self.controller.quitApp()


    # -------------------------------------------------------------------------
        

    def setupMenus(self):

        # ----- File Menu -----
        fileMenu = self.menubar.addMenu("&File")

        # -- Actions --
        newAction = fileMenu.addAction("New")
        newAction.triggered.connect(self.newFile)
        newWindowAction = fileMenu.addAction("New Window")
        newWindowAction.triggered.connect(self.newFileWindow)
        openAction = fileMenu.addAction("Open")
        openAction.triggered.connect(self.openFile)
        saveAction = fileMenu.addAction("Save")
        saveAsAction = fileMenu.addAction("Save As")
        saveAsAction.triggered.connect(self.saveAs)
        quitAction = fileMenu.addAction("Exit")
        quitAction.triggered.connect(self.quitApp)


        # ----- Edit menu ------
        editMenu = self.menubar.addMenu("&Edit")

        # -- Actions --
        undoAction = editMenu.addAction("Undo")
        undoAction.triggered.connect(self.textEdit.undo)
        redoAction = editMenu.addAction("Redo")
        redoAction.triggered.connect(self.textEdit.redo)
        cutAction = editMenu.addAction("Cut")
        cutAction.triggered.connect(self.textEdit.cut)
        copyAction = editMenu.addAction("Copy")
        copyAction.triggered.connect(self.textEdit.copy)
        pasteAction = editMenu.addAction("Paste")
        pasteAction.triggered.connect(self.textEdit.paste)


    # -------------------------------------------------------------------------
        

    def onTextChanged(self):

        # Status bar display
        self.statusBar().showMessage("Characters: " + str(len(self.textEdit.toPlainText())))


        # -----  ADD LINE NUMBERS -----

        # A new numLine label replaces the default "firstLabel" that is a placeholder in the numVBox.
        # Without the placeholder the column has no content and the first line number should be displayed initially 
        # instead of appearing once content is entered
        lines = self.textEdit.toPlainText().split('\n')
        
        if len(lines) > self.lineNumber:
            while len(lines) > self.lineNumber:
                self.lineNumber += 1
                numLine = QLabel(str(self.lineNumber))
                numLine.setObjectName("numLine")
                self.window.numVBox.addWidget(numLine)
                self.adjustFont(self.fontSize)
            

        # If the lines decrease, delete the line number
        elif len(lines) < self.lineNumber:
            self.lineNumber -= 1
            widget = self.window.numVBox.itemAt(self.lineNumber).widget()

            if widget:
                widget.deleteLater()           


    # -------------------------------------------------------------------------
            

    def saveAs(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textEdit.toPlainText())
                

    # -------------------------------------------------------------------------
    
    
    def openFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "r") as file:
                self.textEdit.setText(file.read())
       
                
    # -------------------------------------------------------------------------


    def loadFile(self, filename):
        with open(filename, "r") as file:
            self.textEdit.setText(file.read())
            

    # -------------------------------------------------------------------------
    
    def changeFontSize(self, bigger):
        
        if bigger:
            self.fontSize += 5
 
        else:
            self.fontSize -= 5  
                
        self.adjustFont(self.fontSize) 
        

    # -------------------------------------------------------------------------
    
    
    def adjustFont(self, fontSize):
        
        font = self.textEdit.font()
        font.setPointSize(fontSize)
        self.textEdit.setFont(font)
        
        
        numLines = self.window.ContentFrame.findChildren(QLabel)
        
        for line in numLines:
            line.setFont(font)
        
        self.window.horizontalSlider.setValue(fontSize)
        self.fontSize = fontSize
        

    # -------------------------------------------------------------------------
    

    def newFile(self):
        self.controller.main()
        

    def newFileWindow(self):
        self.close()
        self.controller.main()

        