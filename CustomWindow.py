from icecream import ic

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QMenuBar
from PySide6.QtCore import Qt, QPoint, QTimer, QEvent
from PySide6.QtGui import QIcon, QCursor
from MyHelperLibrary.Helpers.HelperMethods import createLayoutFrame, createWidget



class CustomWindow(QMainWindow):

    def __init__(self, windowName, windowIcon):
        super().__init__()

        self.windowName = windowName
        self.windowIcon = windowIcon

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(300, 100)

        # Custom title bar
        self.createTitleBar(windowName, windowIcon)

        self.menubar = QMenuBar(self)
        self.menubar.setFixedHeight(25)
        self.menubar.setGeometry(0, self.titleBar.height(), self.width(), 25)

        self.containerWidget = QWidget(objectName="containerWidget")
        containerLayout = QVBoxLayout(self.containerWidget)
        containerLayout.setContentsMargins(0, 0, 0, 0)  # Remove any margins
        containerLayout.setSpacing(0) 
        containerLayout.addWidget(self.titleBar)
        containerLayout.addWidget(self.menubar)

        # Set the title bar as the menu widget
        self.setMenuWidget(self.containerWidget)

        # Variables for window dragging
        self.dragging           = False
        self.dragPosition       = QPoint()

        self.resizing           = False
        self.resizeDirection    = None
        self.resizeMargin       = 10  # Threshold for detecting edges

        # Timer to continuously check the mouse position and update cursor
        self.mouseTrackingTimer = QTimer(self)
        self.mouseTrackingTimer.timeout.connect(self.trackMousePosition)
        self.mouseTrackingTimer.start(300)  # Every 30 ms


    # =============================================================================================


    def createTitleBar(self, windowName, windowIcon):

        self.titleBar   = QWidget(self, objectName="titleBar")
        titleLayout     = QHBoxLayout(self.titleBar)
        titleLayout.setContentsMargins(10,0,0,0)
        self.titleBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.iconLabel = QLabel(objectName="windowIcon")
        self.iconLabel.setPixmap(QIcon(windowIcon).pixmap(25, 25))

        self.titleLabel = createWidget("label", text=windowName, objectName="titleLabel", sizePolicy=("expanding", "fixed"))

        self.minBtn     = QPushButton(QIcon("icons/minimize"), "", objectName="titleBarButton")
        self.maxBtn     = QPushButton(QIcon("icons/maximize"), "", objectName="titleBarButton")
        self.closeBtn   = QPushButton(QIcon("icons/close_window"), "", objectName="titleBarButton")

        self.minBtn.setFixedSize(20, 20)
        self.maxBtn.setFixedSize(20, 20)
        self.closeBtn.setFixedSize(20, 20)

        buttonFrame = createLayoutFrame(objectName="buttonFrame", sizePolicy=("fixed", "fixed"), spacing=5)
        buttonFrame.setContentsMargins(0,0,0,0)
        buttonFrame.layout().addWidget(self.minBtn)
        buttonFrame.layout().addWidget(self.maxBtn)
        buttonFrame.layout().addWidget(self.closeBtn)

        titleLayout.addWidget(self.iconLabel)
        titleLayout.addWidget(self.titleLabel)
        titleLayout.addWidget(buttonFrame)

        # Connect buttons to functions
        self.minBtn.clicked.connect(self.minimizeWindow)
        self.maxBtn.clicked.connect(self.toggleMaximize)
        self.closeBtn.clicked.connect(self.close_window)


    # =============================================================================================


    def main(self):
        self.show()

        
    # =============================================================================================

 
    def minimizeWindow(self):
        self.showMinimized()


    # =============================================================================================


    def toggleMaximize(self):

        if self.isMaximized():
            self.showNormal()
            self.maxBtn.setIcon(QIcon("icons/maximize"))

        else:
            self.showMaximized()
            self.maxBtn.setIcon(QIcon("icons/restore_down"))

        # Set an event filter to capture the resize event once it has finished, otherwise it means setting the width on a window that hasn't finished resizing 
        def handleResize(obj, event):
                
            if event.type() == QEvent.Resize:
                self.titleBar.setFixedWidth(self.width())   # Can safely get the real maximized width
                self.removeEventFilter(self)        # Remove this temporary event handler

            return False
            
        self.installEventFilter(self)
        self.eventFilter = handleResize

    # =============================================================================================


    def close_window(self):
        self.close()


    # =============================================================================================


    def trackMousePosition(self):
        pos = QCursor.pos()

        for key, value in self.checkMouseOnWindowBorder(pos).items():
            if value:
                self.setCursor(self.changeCursor(key))
                break

        else:
            self.setCursor(Qt.ArrowCursor)


    # =============================================================================================


    def mousePressEvent(self, event):

        pos = QCursor.pos()

        if event.button() == Qt.LeftButton:
            # Detect if mouse is near the edges for resizing
            for key, value in self.checkMouseOnWindowBorder(pos).items():
                if value:
                    # Lock in the cursor and window values before resizing
                    self.resizing           = True
                    self.resizeDirection    = key
                    self.initialPosition    = event.globalPos()
                    self.initialWidth       = self.width()
                    self.initialHeight      = self.height()
                    break
            
            else:
                self.dragging = True
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()

    # =============================================================================================


    def mouseMoveEvent(self, event):

        if self.resizing:
            # Resize the window based on the direction
            self.resizeWindow()

        elif self.dragging:
            # Drag the window
            self.move(event.globalPos() - self.dragPosition)


    # =============================================================================================


    def mouseReleaseEvent(self, event):

        self.dragging = False
        self.resizing = False
        self.setCursor(Qt.ArrowCursor)

    
    # =============================================================================================


    """Check if the mouse is near any edge or corner of the window."""
    
    def checkMouseOnWindowBorder(self, pos):

        leftEdge    = pos.x() <= self.pos().x() + self.resizeMargin and pos.x() >= self.pos().x() - self.resizeMargin
        rightEdge   = pos.x() <= self.pos().x() + self.rect().width() + self.resizeMargin and pos.x() >= self.pos().x() + self.rect().width() - self.resizeMargin
        topEdge     = pos.y() >= self.pos().y() - self.resizeMargin and pos.y() <= self.pos().y() + self.resizeMargin
        bottomEdge  = pos.y() <= self.pos().y() + self.rect().height() + self.resizeMargin and pos.y() >= self.pos().y() + self.rect().height() - self.resizeMargin


        topLeft, bottomLeft, topRight, bottomRight = "", "", "", ""

        if leftEdge and topEdge:
            topLeft, leftEdge, topEdge = True, False, False

        elif leftEdge and bottomEdge:
            bottomLeft, leftEdge, bottomEdge = True, False, False

        elif rightEdge and topEdge:
            topRight, rightEdge, topEdge = True, False, False

        elif rightEdge and bottomEdge:
            bottomRight, rightEdge, bottomEdge = True, False, False

        direction = {"left": leftEdge, "topLeft": topLeft, "bottomLeft": bottomLeft , 
                     "right": rightEdge, "topRight": topRight, "bottomRight": bottomRight, 
                     "top": topEdge, "bottom": bottomEdge }
 
        return direction


    # =============================================================================================


    """Returns the appropriate cursor for the resize direction."""
    def changeCursor(self, direction):

        if direction == 'left' or direction == 'right':
            return Qt.SizeHorCursor

        elif direction == 'top' or direction == 'bottom':
            return Qt.SizeVerCursor

        elif direction == 'topLeft' or direction == 'bottomRight':
            return Qt.SizeFDiagCursor

        elif direction == 'topRight' or direction == 'bottomLeft':
            return Qt.SizeBDiagCursor

        return Qt.ArrowCursor


    # =============================================================================================


    """Resize the window based on mouse movement."""
    def resizeWindow(self):
        ic("resize")

        pos = QCursor.pos()

        difference = pos - self.initialPosition

        
        if self.resizeDirection == 'left':
            self.setGeometry(pos.x(), self.y(), self.initialWidth - difference.x(), self.height())

        elif self.resizeDirection == 'right':
            self.setGeometry(self.x(), self.y(), self.initialWidth + difference.x(), self.height())

        elif self.resizeDirection == 'top':
            self.setGeometry(self.x(), pos.y(), self.width(), self.initialHeight - difference.y())

        elif self.resizeDirection == 'bottom':
            self.setGeometry(self.x(), self.initialPosition.y() - self.initialHeight, self.width(), self.initialHeight + difference.y())

        elif self.resizeDirection == 'topLeft':
            ic(self.initialWidth - difference.x())
            self.setGeometry(pos.x(), pos.y(), self.initialWidth - difference.x(), self.initialHeight - difference.y())

        elif self.resizeDirection == 'topRight':
            self.setGeometry(self.x(), pos.y(), self.initialWidth + difference.x(), self.initialHeight - difference.y())

        elif self.resizeDirection == 'bottomLeft':
            self.setGeometry(pos.x(), self.initialPosition.y() - self.initialHeight, self.initialWidth - difference.x(), self.initialHeight + difference.y())

        elif self.resizeDirection == 'bottomRight':
            self.setGeometry(self.x(), self.initialPosition.y() - self.initialHeight, self.initialWidth + difference.x(), self.initialHeight + difference.y())


        self.titleBar.setFixedWidth(self.width())

    # =============================================================================================
