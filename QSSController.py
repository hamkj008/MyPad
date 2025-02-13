from icecream import ic
from enum import Enum, auto


# =============================================================================================


class Theme(Enum):

    LIGHT           = auto()
    DARK            = auto()
    ELECTRICBLUE    = auto()


# =============================================================================================


class QSSController():
   
    def __init__(self):
        ic("qssController")

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
        self.buttonHover                = "purple"
        self.borderColor                = "#0892d0"

        self.themes = {
            Theme.DARK: {
                "primaryColor"          : "#343335",
                "secondaryColor"        : "#686b6d",
                "tertiaryColor"         : "black",
                "textColor"             : "white",
                "borderColor"           : "black",
                "buttonColor"           : "#686b6d",
                "buttonTextColor"       : "white",
                "buttonHoverColor"      : "blue",
                "titleBarColor"         : "#343335",
                "titleBarButtonColor"   : "black"
            },
            
            Theme.LIGHT: {
                "primaryColor"          : "#c7c5cc",
                "secondaryColor"        : "white",
                "tertiaryColor"         : "white",
                "textColor"             : "black",
                "borderColor"           : "black",
                "buttonColor"           : "white",
                "buttonTextColor"       : "black",
                "buttonHoverColor"      : "blue",
                "titleBarColor"         : "#686770",
                "titleBarButtonColor"   : "black"
            },

            Theme.ELECTRICBLUE: {
                "primaryColor"          : "#0c5cd3",
                "secondaryColor"        : "#001120",
                "tertiaryColor"         : "#001120",
                "textColor"             : "#0892d0",
                "borderColor"           : "#0892d0",
                "buttonColor"           : "#0892d0",
                "buttonTextColor"       : "white",
                "buttonHoverColor"      : "purple",
                "titleBarColor"         : "#001120",     
                "titleBarButtonColor"   : "#0c5cd3"
            }
        }


        self.setTheme(Theme.DARK)


    # ========================================================================================
      

    def createTheme(self, themeName, parent, overrides):
        if parent not in self.themes:
            raise ValueError(f"Parent theme {parent} does not exist")

        newTheme = self.themes[parent].copy()
        newTheme.update(overrides)
        self.themes[themeName] = newTheme


    # ========================================================================================
     

    def setTheme(self, chosenTheme):

        if chosenTheme not in self.themes:
            raise ValueError(f"Theme {chosenTheme} does not exist")

        self.currentTheme = chosenTheme

   
    # ========================================================================================


    def getWindowStyle(self):

        return f""" 
                CustomWindow {{
                    border: 2px solid {self.themes[self.currentTheme]["borderColor"]}; 
                }}

                #containerWidget {{
                    background-color: {self.themes[self.currentTheme]["secondaryColor"]};
                    border-left: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                    border-right: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                }}
                /*  ------------------- */

                #titleBar {{
                    background-color: {self.themes[self.currentTheme]["titleBarColor"]}; 
                    border: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                }}

                #titleLabel {{
                    color: {self.themes[self.currentTheme]["textColor"]};
                }}

                #titleBarButton {{
                    background-color: {self.themes[self.currentTheme]["titleBarButtonColor"]};
                }}

                #titleBarButton:hover {{
                    background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                }}

                QMenuBar {{
                    color: {self.themes[self.currentTheme]["textColor"]};
                }}

                QMenuBar::item:selected {{
                    color: {self.themes[self.currentTheme]["primaryColor"]};
                    background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                }}

                QPushButton::hover {{
                    background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                }}

            """


    def getContentStyle(self):

        return f"""
                #MainWidget {{
                    background-color: {self.themes[self.currentTheme]["secondaryColor"]};
                    border-left: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                    border-right: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                }}

                #ButtonFrame, #ContentFrame {{
                    background-color: {self.themes[self.currentTheme]["primaryColor"]};
                    border: 1px solid {self.themes[self.currentTheme]["borderColor"]};
                }}

                #textEdit {{
                    background-color: {self.themes[self.currentTheme]["tertiaryColor"]};
                    color: {self.themes[self.currentTheme]["textColor"]};
                    padding: 5px;
                }}
                           
                #SaveBtn, #SaveAsBtn, #CutBtn, #CopyBtn, #PasteBtn, #ClearBtn {{
                    background-color: {self.themes[self.currentTheme]["buttonColor"]};
                    font: 12pt "Century Gothic";
                    font-weight: 400;
	                color: {self.themes[self.currentTheme]["buttonTextColor"]};
                    border: 2px solid black;	
                    padding: 10px;
                }}

                #SaveBtn:hover, #SaveAsBtn:hover, #CutBtn:hover, #CopyBtn:hover, #PasteBtn:hover, #ClearBtn:hover {{
                    background-color: {self.themes[self.currentTheme]["buttonHoverColor"]};
                }}

                #leftBtn, #rightBtn {{
                    background-color: {self.themes[self.currentTheme]["buttonColor"]};
                    border: 1px solid {self.themes[self.currentTheme]["borderColor"]};
                    padding: 3px;
                }}

                """

    def getPreferencesStyle(self):

        return f"""
                #PreferencesWidget {{
                    background-color: {self.themes[self.currentTheme]["secondaryColor"]};
                    border-left: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                    border-bottom: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                    border-right: 2px solid {self.themes[self.currentTheme]["borderColor"]};
                }}

                #themeOptionsLabel {{
                    color: {self.themes[self.currentTheme]["textColor"]};
                }}
        """


