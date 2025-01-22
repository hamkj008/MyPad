from icecream import ic


class QSSController():
   
    def __init__(self):
        ic("qssController")


    def getStyle(self):

        return """
                #centralwidget {
                    background-color: #686b6d;
                }
                #ButtonFrame, #ContentFrame{ 
                    background-color: #343335;
                    border: 1px solid black;
                }

                #numLine, #firstLabel {
                    color: #b620fc;
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

                #leftBtn, #rightBtn {
                    border: 1px solid black;
                    padding: 3px;
                }
                """




