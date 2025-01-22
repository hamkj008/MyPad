from icecream import ic

from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QPainter, QColor, QTextBlockFormat, QTextCursor, QPen, QFontMetrics
from PySide6.QtCore import Qt



class LineNumberTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()

        # self.setViewportMargins(40, 0, 0, 0)  # 40px space for line numbers
        self.setLineWrapMode(QTextEdit.NoWrap)

        self.fontSize = 15
        self.leftMargin = 70
        self.numbersColor = QColor(0, 255, 0)
        self.lineColor = QColor(0, 0, 255)
        self.lineCount = 1


    # =============================================================================================

    """Get and display the number of lines in QTextEdit."""
    def getLineCount(self):

        cursor = QTextCursor(self.document())
        self.lineCount = 0
        cursor.movePosition(QTextCursor.Start)
        totalBlocks = self.document().blockCount()
        
        for _ in range(totalBlocks):
            cursor.movePosition(QTextCursor.Down)  # Move to the next line
            self.lineCount += 1


    # =============================================================================================


    """Set left margin for the QTextEdit document."""
    def setSettings(self, lineHeight):

        block_format = QTextBlockFormat()
        block_format.setLeftMargin(self.leftMargin)      # The margin space that separates the text from the numbers
        block_format.setBottomMargin(5)
        block_format.setLineHeight(lineHeight, QTextBlockFormat.FixedHeight.value) 

        cursor = QTextCursor(self.document())
        cursor.select(QTextCursor.Document)  # Select the entire document
        cursor.setBlockFormat(block_format)  # Apply the block format


    # =============================================================================================


    """Override paintEvent to draw line numbers and lines for each line of text."""
    def paintEvent(self, event):

        super().paintEvent(event)

        # Use QPainter to draw line numbers in the left margin
        painter = QPainter(self.viewport())

        font = self.font()      # Retrieve the font of the QTextEdit
        painter.setFont(font)   # Set the painter's font to match the QTextEdit's font
        font.setPointSize(self.fontSize)

        self.setFont(font)    

        fontMetrics = QFontMetrics(font)
        self.setSettings(fontMetrics.height())
      
        block = self.document().begin()
        blockNumber = 1
        scroll_y = self.verticalScrollBar().value()
       
        
        # Draw numbers and lines for each block
        while block.isValid():

            block_rect = self.document().documentLayout().blockBoundingRect(block)
            y_position = block_rect.topLeft().y() - scroll_y  # Adjust for scrolling

            if y_position > self.viewport().height():  # Stop drawing if out of viewport
                break

            painter.setPen(QPen(self.lineColor, 0.5))
            painter.drawLine(self.leftMargin, y_position + block_rect.height(), self.width(), y_position + block_rect.height())


            # Draw the line number to the left of the text
            painter.setPen(QPen(self.numbersColor, 2))


            # Calculate the y position such that the number is centered in the middle of the block
            numberPosition = y_position + block_rect.height() * 0.8
            painter.drawText(10, numberPosition, str(blockNumber))  # 10px from left

            # painter.drawRect(block_rect.topLeft().x(), block_rect.topLeft().y(), block_rect.width(), block_rect.height())  # 10px from left

            # Move to the next block
            block = block.next()
            blockNumber += 1

        painter.end()


    # =============================================================================================



    def keyPressEvent(self, event):

        # If Enter key is pressed, add additional lines
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            cursor = self.textCursor()
            cursor.movePosition(QTextCursor.End)  # Move cursor to the end
            cursor.insertBlock() 

        super().keyPressEvent(event)