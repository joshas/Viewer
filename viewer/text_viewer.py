from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TextViewer(QPlainTextEdit):
    def __init__(self, file_name, parent=None):
        super(TextViewer, self).__init__(parent)

        # disable text editing
        self.setReadOnly(True)

        # set background color
        palette = QPalette()
        bg_color = QColor(39, 40, 34)
        palette.setColor(QPalette.Base, bg_color)
        text_color = QColor(200, 200, 200)
        palette.setColor(QPalette.Text, text_color)
        self.setPalette(palette)

        # set monospace font
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.setFont(font)
        self.isFontMonospace = True

        # set tab size to 4 spaces
        metrics = QFontMetrics(font)
        self.setTabStopWidth(4 * metrics.width(' '))

        # load text file into viewer
        file = QFile(file_name)
        file.open(QFile.ReadOnly)
        text = file.readAll()
        # if text is not unicode, display it as latin1
        try:
            text = str(text, encoding='utf8')
        except:
            text = str(text, 'latin1')
        self.setPlainText(text)
        self.setFocus()

    def keyPressEvent(self, e):
        # toggle line wrapping mode
        if e.key() == Qt.Key_W:
            if self.lineWrapMode() == QPlainTextEdit.NoWrap:
                self.setLineWrapMode(self.WidgetWidth)
            else:
                self.setLineWrapMode(self.NoWrap)
        # toggle variable/fixed font
        if e.key() == Qt.Key_V:
            if self.isFontMonospace:
                font = QFontDatabase.systemFont(QFontDatabase.GeneralFont)
                self.isFontMonospace = False
            else:
                font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
                self.isFontMonospace = True
            self.setFont(font)

        super(TextViewer, self).keyPressEvent(e)
