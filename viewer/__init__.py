from fman import DirectoryPaneCommand
import os
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


class ImageViewer(QScrollArea):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)

    def loadImage(self, file_name):
        image_label = QLabel()
        image = QPixmap(file_name)

        if image.isNull():
            return False

        image_label.setPixmap(image)
        self.setWidget(image_label)

        return True


class ViewerWindow(QWidget):
    def __init__(self, file_name, parent=None):
        super(ViewerWindow, self).__init__(parent)

        # delete this widget when the widget has accepted the close event
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.resize(640, 480)
        # window.move(300, 300)
        self.setWindowTitle('Viewer - [' + file_name + ']')

        # try to display image
        viewer = ImageViewer(self)
        result = viewer.loadImage(file_name)
        if not result:
            viewer = TextViewer(file_name, self)

        # add viewer to qwidget
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(viewer)

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            if self.isFullScreen():
                self.showNormal()
            self.close()


class ViewFile(DirectoryPaneCommand):
    def __call__(self):
        file_name = self.pane.get_file_under_cursor()

        # check if selected item is not a directory
        if not os.path.isdir(file_name):
            # display a warning before opening big file (larger than 100MB)
            file_size = os.path.getsize(file_name)
            if file_size > (1024 * 1024 * 100):
                warn_msg = "The file you are about to open is large. Do you really want to open it?"
                reply = QMessageBox.information(None, 'Warning', warn_msg, QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.No:
                    return

            # store windows in a list
            if not hasattr(self, 'viewer_window'):
                self.viewer_window = []
            self.viewer_window.append(ViewerWindow(file_name))
