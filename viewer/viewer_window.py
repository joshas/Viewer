from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from viewer.text_viewer import TextViewer
from viewer.image_viewer import ImageViewer


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
        result = viewer.load_image(file_name)
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
