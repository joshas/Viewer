import os
# noinspection PyUnresolvedReferences
from fman import DirectoryPaneCommand, show_alert
# noinspection PyUnresolvedReferences
from fman.url import as_human_readable, splitscheme
# noinspection PyUnresolvedReferences
from fman.impl.util.qt import run_in_main_thread
from PyQt5.QtWidgets import *
from viewer.viewer_window import ViewerWindow


class ViewFile(DirectoryPaneCommand):
    @run_in_main_thread
    def __call__(self):
        file_name = self.pane.get_file_under_cursor()

        if not file_name:
            show_alert('No file is selected!')
            return

        scheme, path = splitscheme(file_name)
        if scheme == 'file://':
            file_name = as_human_readable(file_name)
        else:
            show_alert('Only local files are supported.')
            return

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
