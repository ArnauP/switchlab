from pynput.keyboard import Key, Listener
from PyQt5.QtCore import QObject
from playsound import playsound
from threading import Thread

from ..utils.utils import *
from ..views.main_view import MainView
from ..constants import *


class MainController(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.__switch_selected = None
        self.__key_pressed = False
        self.__view = MainView(self)
        self.start_listener()

    def play_sfx(self, switch_id, key_type, key_action):
        sound_path = get_path('{}{}/{}_{}.wav'.format(PATH_SWITCH_SFX, switch_id, key_type, key_action))
        playsound(sound_path)

    def change_switch_selected(self, switch_id):
        self.__switch_selected = switch_id
    
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
            key = FILE_NAME_SPACE
        elif key == Key.enter:
            key = FILE_NAME_ENTER
        elif key == Key.backspace or key == Key.tab:
            key = FILE_NAME_BACKSPACE
        else:
            key = FILE_NAME_ALPHANUMERIC
        return key

    def on_press(self, key):
        if self.__key_pressed == key:
            return
        self.__key_pressed = key
        key_type = self.get_key_type(key)
        play_audio_thread = Thread(target=lambda: self.play_sfx(self.__switch_selected, key_type, 'press'))
        play_audio_thread.start()

    def on_release(self, key):
        self.__key_pressed = None
        key_type = self.get_key_type(key)
        play_audio_thread = Thread(target=lambda: self.play_sfx(self.__switch_selected, key_type, 'release'))
        play_audio_thread.start()

    @property
    def switch_selected(self):
        return self.__switch_selected

    @switch_selected.setter
    def switch_selected(self, value):
        self.__switch_selected = value