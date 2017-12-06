from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ImageViewer(QScrollArea):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)

    def load_image(self, file_name):
        image_label = QLabel()
        image = QPixmap(file_name)

        if image.isNull():
            return False

        image_label.setPixmap(image)
        self.setWidget(image_label)

        return True
