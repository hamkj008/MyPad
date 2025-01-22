import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from View import View



class Main:
    
    def __init__(self):
        self.app = QApplication([])


    def main(self):     

        filename = sys.argv[1] if len(sys.argv) > 1 else None
        self.view = View(self, filename)
        self.view.main()


    def quitApp(self):
        self.app.quit()




if __name__ == "__main__":
    main = Main()
    main.main()
    main.app.exec()
