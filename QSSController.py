from icecream import ic
from enum import Enum, auto


# =============================================================================================


class ColorTheme(Enum):

    LIGHT           = auto()
    DARK            = auto()
    ELECTRICBLUE    = auto()


# =============================================================================================


class QSSController():
   
    def __init__(self, defaultTheme):
        ic("qssController")

        self.currentTheme           = defaultTheme

        self.centralWidget          = None
        self.buttonAndContentFrame  = None
        self.textEdit               = None
        self.buttonColor            = None
        self.buttonTextColor        = None
        self.buttonHover            = None

    # =============================================================================================


    def getStyle(self):

        return """
                QMainWindow {
                    border: 5px solid #4CAF50; 
                }

                #centralwidget {
                    background-color: #686b6d;
                }

                #ButtonFrame, #ContentFrame{ 
                    background-color: #343335;
                    border: 1px solid black;
                }

                #textEdit{
                    background-color: black;
                    color: white;
                    padding: 5px;
                }
                           
                #SaveBtn, #SaveAsBtn, #CutBtn, #CopyBtn, #PasteBtn, #ClearBtn {
                    background-color: #686b6d;
                    font: 12pt "Century Gothic";
                    font-weight: 400;
	                color: black;
                    border: 2px solid black;	
                    padding: 10px;
                } 

                #SaveBtn:hover, #SaveAsBtn:hover, #CutBtn:hover, #CopyBtn:hover, #PasteBtn:hover, #ClearBtn:hover {
                    background-color: white;
                }

                #leftBtn, #rightBtn {
                    border: 1px solid black;
                    padding: 3px;
                }
                """




