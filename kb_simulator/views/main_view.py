
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QWidget, QComboBox, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from ..controllers.constants import *
from ..utils.utils import *


class MainView(QWidget):

    def __init__(self, ctrl):
        super(MainView, self).__init__()
        self.__ctrl = ctrl
        self.build_ui()
        self.__ctrl.current_key_pressed = self.switch_selector.itemText(0)

    def build_ui(self):
        self.setWindowTitle('KB Switch Simulator')
        self.setFixedSize(300, 300)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        self.switch_selector = QComboBox(self)
        for switch_name in SWITCHES.keys():
            self.switch_selector.addItem(switch_name)
        
        img_path = get_path('{}{}.png'.format(
            SWITCH_SFX_PATH,
            SWITCHES[self.switch_selector.itemText(0)]
            ))
        print(img_path, os.path.isfile(img_path))
        self.img_container = QLabel(self)
        img = QPixmap(img_path)
        self.img_container.setPixmap(img.scaled(QSize(SWITCH_HEIGHT, SWITCH_WIDTH)))

        self.__ctrl.switch_selected = SWITCHES[self.switch_selector.itemText(0)]
        self.switch_selector.currentIndexChanged.connect(self.selection_change)

        main_layout.addWidget(self.img_container)
        main_layout.addWidget(self.switch_selector)
        self.setLayout(main_layout)
        self.show()

    def selection_change(self, index):
        new_switch_name = self.switch_selector.itemText(index)
        img_path = get_path('{}{}.png'.format(
            SWITCH_SFX_PATH,
            SWITCHES[new_switch_name]
            ))
        img = QPixmap(img_path)
        self.img_container.setPixmap(img.scaled(QSize(SWITCH_HEIGHT, SWITCH_WIDTH)))
        self.__ctrl.change_switch_selected(SWITCHES[new_switch_name])
        
