from fman import DirectoryPaneCommand, show_alert, show_status_message
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ViewerWindow(QWidget):
    def __init__(self, parent=None):
        super(ViewerWindow, self).__init__(parent)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

class ViewFile(DirectoryPaneCommand):
    def __call__(self):
        file_name = self.pane.get_file_under_cursor()

        # TODO: check if it is file or directory

        text_edit = QPlainTextEdit()
        # disable text editing
        text_edit.setReadOnly(True)

        # set background color
        palette = QPalette()
        bgcolor = QColor(39, 40, 34)
        palette.setColor(QPalette.Base, bgcolor)
        #textc = QColor(255, 255, 255)
        #pal.setColor(QPalette.Text, textc)
        text_edit.setPalette(palette)

        # set monospace font
        font = QFont('Monospace')
        font.setStyleHint(QFont.TypeWriter)
        text_edit.setFont(font)

        # load text file into viewer
        file = QFile(file_name)
        file.open(QFile.ReadOnly)
        text = file.readAll()
        text = str(text, encoding='utf8')
        text_edit.setPlainText(text)

        global window # FIXME: keep reference to window in app scope

        window = ViewerWindow()
        window.resize(640, 480)
        #window.move(300, 300)
        window.setWindowTitle('Viewer - [' + file_name + ']')

        # add text_edit to qwidget
        window.layout = QVBoxLayout(window)
        window.layout.setContentsMargins(0, 0, 0, 0)
        window.layout.addWidget(text_edit)

        # TODO: display status bar with file type, encoding, length, end line type, wrapping mode
        #status_bar = QStatusBar()
        #window.layout.addWidget(status_bar)

        window.show()
