from PyQt5.QtCore import pyqtSignal, QObject
from pynput.keyboard import Key, Listener
from ..views.main_view import MainView
from ..utils.utils import *
from .constants import *


class MainController(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.switch_selected = None
        self.__key_pressed = False
        self.__view = MainView(self)
        self.start_listener()
    
    def change_switch_selected(self, switch_id):
        self.switch_selected = switch_id
    
    def stop_listener(self):
        try:
            self.listener.join()
        except Exception as e:
            print('Could not stop thread. Exception: {}'.format(e))

    def start_listener(self):
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
    
    def get_key_type(self, key):
        if key == Key.space:
            key = 'space'
        elif key == Key.enter:
            key = 'enter'
        elif key == Key.backspace or key == Key.tab:
            key = 'backspace'
        else:
            key = 'normal'
        return key

    def on_press(self, key):
        if self.__key_pressed == key:
            return
        self.__key_pressed = key
        key_type = self.get_key_type(key)
        audio_path = 'kb_simulator/resources/sfx/{}/{}_press.mp3'.format(self.switch_selected, key_type)
        play_audio_thread = PlaySoundThread(audio_path)
        play_audio_thread.start()

    def on_release(self, key):
        self.__key_pressed = None
        key_type = self.get_key_type(key)
        audio_path = 'kb_simulator/resources/sfx/{}/{}_release.mp3'.format(self.switch_selected, key_type)
        play_audio_thread = PlaySoundThread(audio_path)
        play_audio_thread.start()
