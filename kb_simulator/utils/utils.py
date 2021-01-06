from PyQt5.QtCore import QFile, QTextStream
from playsound import playsound
from threading import Thread
import os, sys


class PlaySoundThread(Thread):
    def __init__(self, path):
        super().__init__()
        self.__path = get_path(path)
    
    def run(self):
        playsound(self.__path)

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
