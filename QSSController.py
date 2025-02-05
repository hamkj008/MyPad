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

        self.currentTheme               = defaultTheme

        self.containerWidgetColor       = None
        self.titleBarColor              = None
        self.titleBarText               = None
        self.titleBarButtonColor        = None
        self.menubarTextColor           = None
        self.buttonAndContentFrame      = None
        self.textEditColor              = None
        self.textEditTextColor          = None
        self.buttonColor                = None
        self.buttonTextColor            = None
        self.buttonHover                = None
        self.borderColor                = None


        self.setTheme(self.currentTheme)


    # =============================================================================================

    def setTheme(self, chosenTheme):
        ic("set theme")

        self.currentTheme = chosenTheme

        # -----

        if self.currentTheme == ColorTheme.DARK:
            ic("dark")
            self.containerWidgetColor       = "#686b6d"
            self.titleBarColor              = "#343335"
            self.titleBarText               = "white"
            self.titleBarButtonColor        = "black"
            self.menubarTextColor           = "white"
            self.buttonAndContentFrame      = "#343335"
            self.textEditColor              = "black"
            self.textEditTextColor          = "white"
            self.buttonColor                = "#686b6d"
            self.buttonTextColor            = "black"
            self.buttonHover                = "#686b6d"
            self.borderColor                = "black"

        # -----

        elif self.currentTheme == ColorTheme.LIGHT:

            self.containerWidgetColor       = None
            self.titleBarColor              = "#686b6d"
            self.titleBarText               = "black"
            self.titleBarButtonColor        = "#686b6d"
            self.menubarTextColor           = "black"
            self.buttonAndContentFrame      = None
            self.textEditColor              = "white"
            self.textEditTextColor          = "black"
            self.buttonColor                = "white"
            self.buttonTextColor            = "black"
            self.buttonHover                = None
            self.borderColor                = "black"

        # -----

        elif self.currentTheme == ColorTheme.ELECTRICBLUE:
            ic("electric")
            self.containerWidgetColor       = "#001120"
            self.titleBarColor              = "#001120"
            self.titleBarText               = "#0892d0"
            self.titleBarButtonColor        = "#0c5cd3"
            self.menubarTextColor           = "#0892d0"
            self.buttonAndContentFrame      = "#0c5cd3"
            self.textEditColor              = "#001120"
            self.textEditTextColor          = "#0892d0"
            self.buttonColor                = "#0892d0"
            self.buttonTextColor            = "#001120"
            self.buttonHover                = "#0c5cd3"
            self.borderColor                = "#0892d0"


    # =============================================================================================


    def getWindowStyle(self):

        return f""" 
                CustomWindow {{
                    border: 2px solid {self.borderColor}; 
                }}

                #containerWidget {{
                    background-color: {self.containerWidgetColor};
                    border-left: 2px solid {self.borderColor};
                    border-right: 2px solid {self.borderColor};
                }}
                /*  ------------------- */

                #titleBar {{
                    background-color: {self.titleBarColor}; 
                    border: 2px solid {self.borderColor};
                }}

                #titleLabel {{
                    color: {self.titleBarText};
                }}

                #titleBarButton {{
                    background-color: {self.titleBarButtonColor};
                }}

                QMenuBar {{
                    color: {self.menubarTextColor};
                }}

            """


    def getContentStyle(self):

        return f"""
                #MainWidget {{
                    background-color: {self.containerWidgetColor};
                    border-left: 2px solid {self.borderColor};
                    border-right: 2px solid {self.borderColor};
                }}

                #ButtonFrame, #ContentFrame {{
                    background-color: {self.buttonAndContentFrame};
                    border: 1px solid black;
                }}

                #textEdit {{
                    background-color: {self.textEditColor};
                    color: {self.textEditTextColor};
                    padding: 5px;
                }}
                           
                #SaveBtn, #SaveAsBtn, #CutBtn, #CopyBtn, #PasteBtn, #ClearBtn {{
                    background-color: {self.buttonColor};
                    font: 12pt "Century Gothic";
                    font-weight: 400;
	                color: {self.buttonTextColor};
                    border: 2px solid black;	
                    padding: 10px;
                }}

                #SaveBtn:hover, #SaveAsBtn:hover, #CutBtn:hover, #CopyBtn:hover, #PasteBtn:hover, #ClearBtn:hover {{
                    background-color: {self.buttonHover};
                }}

                #leftBtn, #rightBtn {{
                    border: 1px solid black;
                    padding: 3px;
                }}

                """




