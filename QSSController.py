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
        self.borderColor            = None


    # =============================================================================================

    def setTheme(self, chosenTheme):

        self.currentTheme = chosenTheme

        # -----

        if self.currentTheme == ColorTheme.DARK:

            self.centralWidget          = None
            self.buttonAndContentFrame  = None
            self.textEdit               = None
            self.buttonColor            = None
            self.buttonTextColor        = None
            self.buttonHover            = None
            self.borderColor            = None

        # -----

        elif self.currentTheme == ColorTheme.LIGHT:

            self.centralWidget          = None
            self.buttonAndContentFrame  = None
            self.textEdit               = None
            self.buttonColor            = None
            self.buttonTextColor        = None
            self.buttonHover            = None
            self.borderColor            = None

        # -----

        elif self.currentTheme == ColorTheme.ELECTRICBLUE:

            self.centralWidget          = None
            self.buttonAndContentFrame  = None
            self.textEdit               = None
            self.buttonColor            = None
            self.buttonTextColor        = None
            self.buttonHover            = None
            self.borderColor            = None


    # =============================================================================================


    def getWindowStyle(self):

        return """ 
                CustomWindow {
                    border: 2px solid rgb(0, 0, 255); 
                }

                #containerWidget {
                    background-color: #A0A0A0;
                    border-left: 2px solid rgb(0, 0, 255);
                    border-right: 2px solid rgb(0, 0, 255);
                }
                /*  ------------------- */

                #titleBar {
                    background-color: #333333; 
                    border: 2px solid rgb(0, 0, 255);
                }

                #titleLabel {
                    color: white;
                }

                #titleBarButton {
                    background-color: blue;
                }

            """


    def getContentStyle(self):

        return """
                #Content {
                    background-color: #A0A0A0;
                    border-left: 2px solid rgb(0, 0, 255);
                    border-right: 2px solid rgb(0, 0, 255);
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




