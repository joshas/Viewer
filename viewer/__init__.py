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
        bgcolor = QColor(39, 40, 34)
        palette.setColor(QPalette.Base, bgcolor)
        # textc = QColor(255, 255, 255)
        # pal.setColor(QPalette.Text, textc)
        self.setPalette(palette)

        # set monospace font
        font = QFont('Monospace')
        font.setStyleHint(QFont.TypeWriter)
        self.setFont(font)

        # load text file into viewer
        # TODO: use thread to prevent main process from freeze while opening big files
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
            self.close()


class ViewFile(DirectoryPaneCommand):
    def __call__(self):
        file_name = self.pane.get_file_under_cursor()

        if not os.path.isdir(file_name):
            # FIXME: how and where to keep references to open windows?
            if not hasattr(self, 'viewer_window'):
                self.viewer_window = []
            self.viewer_window.append(ViewerWindow(file_name))
