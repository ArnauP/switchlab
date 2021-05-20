from PyQt5.QtWidgets import QVBoxLayout, QWidget, QComboBox, QLabel, QMainWindow, QSystemTrayIcon, QMenu, QAction, qApp
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt

from ..constants import *
from ..utils.utils import *


class MainView(QMainWindow):

    def __init__(self, ctrl):
        super(MainView, self).__init__()
        self.__ctrl = ctrl
        self.build_ui()
        self.__ctrl.current_key_pressed = self.switch_selector.itemText(0)

    def build_ui(self):
        self.setWindowTitle('KB Switch Simulator')
        self.setFixedSize(300, 300)

        # Init widgets
        self.main_widget = QWidget()

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        self.switch_selector = QComboBox(self.main_widget)
        for switch_name in SWITCHES.keys():
            self.switch_selector.addItem(switch_name)
        
        img_path = get_path('{}{}.png'.format(
            PATH_SWITCH_IMG,
            SWITCHES[self.switch_selector.itemText(0)]
            ))
        self.img_container = QLabel(self.main_widget)
        img = QPixmap(img_path)
        self.img_container.setPixmap(img.scaled(QSize(SWITCH_HEIGHT, SWITCH_WIDTH)))

        self.__ctrl.switch_selected = SWITCHES[self.switch_selector.itemText(0)]
        self.switch_selector.currentIndexChanged.connect(self.selection_change)

        # Setup layouts
        main_layout.addWidget(self.img_container)
        main_layout.addWidget(self.switch_selector)
        self.main_widget.setLayout(main_layout)

        self.setCentralWidget(self.main_widget)

        # Init tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(get_path(PATH_ICON)))
        
        # Tray actions
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)

        # Tray menu
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.show()
    
    def selection_change(self, index):
        new_switch_name = self.switch_selector.itemText(index)
        img_path = get_path('{}{}.png'.format(
            PATH_SWITCH_IMG,
            SWITCHES[new_switch_name]
            ))
        img = QPixmap(img_path)
        self.img_container.setPixmap(img.scaled(QSize(SWITCH_HEIGHT, SWITCH_WIDTH)))
        self.__ctrl.change_switch_selected(SWITCHES[new_switch_name])

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "KB Switch Simulator",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )        
