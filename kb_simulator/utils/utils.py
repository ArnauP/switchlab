from PyQt5.QtCore import QFile, QTextStream
from pygame import mixer
from time import sleep
import os, sys


def get_path(path):
    base_path = os.getcwd()
    return os.path.join(base_path, path)

def load_style_sheet(stylesheet, obj):
    """
    Loads the given style file to the targeted qt app
    """

    file = QFile(stylesheet)
    file.open(QFile.ReadOnly)
    obj.setStyleSheet(QTextStream(file).readAll())
    file.close()
