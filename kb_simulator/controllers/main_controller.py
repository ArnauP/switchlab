from PyQt5.QtCore import QObject
from pynput.keyboard import Key, Listener
from ..views.main_view import MainView
from ..utils.utils import *
from ..constants import *
from threading import Thread
from pygame import mixer


class MainController(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.switch_selected = None
        self.__key_pressed = False
        self.__view = MainView(self)
        self.init_mixer()
        self.start_listener()
    
    def init_mixer(self):
        self.__mixer = mixer
        self.__mixer.init()

    def play_sfx(self, switch_id, key_type, key_action):
        sound_path = get_path('{}{}/{}/{}{}'.format(PATH_SWITCH_SFX, switch_id,
                                                    key_action, key_type, FILE_EXTENSION_SFX))
        self.__mixer.music.load(sound_path)
        self.__mixer.music.play()

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

    def on_press(self, key):
        if self.__key_pressed == key:
            return
        self.__key_pressed = key
        key_type = self.get_key_type(key)
        play_audio_thread = Thread(target=lambda: self.play_sfx(self.switch_selected, key_type, KEY_ACTION_PRESS))
        play_audio_thread.start()

    def on_release(self, key):
        self.__key_pressed = None
        key_type = self.get_key_type(key)
        play_audio_thread = Thread(target=lambda: self.play_sfx(self.switch_selected, key_type, KEY_ACTION_RELEASE))
        play_audio_thread.start()

    @staticmethod
    def get_key_type(key):
        if key == Key.space:
            key = FILE_NAME_SPACE
        elif key == Key.enter:
            key = FILE_NAME_ENTER
        elif key in [Key.backspace, Key.tab]:
            key = FILE_NAME_BACKSPACE
        else:
            key = FILE_NAME_ALPHANUMERIC
        return key
