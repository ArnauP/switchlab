from PyQt5.QtCore import QFile, QTextStream
import os
import sys


def get_path(path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, path)


def load_style_sheet(stylesheet, obj):
    file = QFile(stylesheet)
    file.open(QFile.ReadOnly)
    obj.setStyleSheet(QTextStream(file).readAll())
    file.close()
