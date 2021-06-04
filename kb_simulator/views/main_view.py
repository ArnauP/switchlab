from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QPushButton,\
    QLabel, QMainWindow, QSystemTrayIcon, QMenu, QAction, qApp, QFrame, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt

from .. import __version__
from ..constants import *


class MainView(QMainWindow):

    def __init__(self, ctrl):
        super(MainView, self).__init__()
        self.__ctrl = ctrl
        self.build_ui()
        self.init_tray_icon()
        self.__ctrl.current_key_pressed = self.switch_selector.itemText(0)

    def action_clicked_home(self):
        print('home')
        self.frame_page.setStyleSheet(
            """
            background-color: white;
            """
        )
        self.page_home.show()
        self.page_switches.hide()
        self.page_settings.hide()
        self.page_about.hide()

    def action_clicked_switches(self):
        print('Switches')
        self.frame_page.setStyleSheet(
            """
            background-color: green;
            """
        )
        self.page_home.hide()
        self.page_switches.show()
        self.page_settings.hide()
        self.page_about.hide()

    def action_clicked_settings(self):
        print('Settings')
        self.page_home.hide()
        self.page_switches.hide()
        self.page_settings.show()
        self.page_about.hide()

    def action_clicked_about(self):
        print('About')
        self.page_home.hide()
        self.page_switches.hide()
        self.page_settings.hide()
        self.page_about.show()

    def init_page_home(self):
        frame = QFrame()
        lyt_frame = QVBoxLayout()

        label = QLabel('Welcome!')
        lyt_frame.addWidget(label)
        frame.setLayout(lyt_frame)

        return frame

    def init_page_switches(self):
        frame = QFrame()
        lyt_frame = QVBoxLayout()

        self.switch_selector = QComboBox(self.main_widget)
        for switch_name in SWITCHES.keys():
            self.switch_selector.addItem(switch_name)

        img_path = '{}{}.png'.format(
            PATH_SWITCH_IMG,
            SWITCHES[self.switch_selector.itemText(0)]
        )
        self.img_container = QLabel(self.main_widget)
        img = QPixmap(img_path)
        self.img_container.setPixmap(img.scaled(QSize(SWITCH_HEIGHT, SWITCH_WIDTH)))

        self.__ctrl.switch_selected = SWITCHES[self.switch_selector.itemText(0)]
        self.switch_selector.currentIndexChanged.connect(self.selection_change)

        lyt_frame.addWidget(self.img_container)
        lyt_frame.addWidget(self.switch_selector)

        frame.setLayout(lyt_frame)

        return frame

    def init_page_settings(self):
        frame = QFrame()
        lyt_frame = QVBoxLayout()

        label = QLabel('Settings')
        lyt_frame.addWidget(label)
        frame.setLayout(lyt_frame)

        return frame

    def init_page_about(self):
        frame = QFrame()
        lyt_frame = QVBoxLayout()

        label = QLabel('About')
        lyt_frame.addWidget(label)
        frame.setLayout(lyt_frame)

        return frame

    def create_frame_menu_bar(self):
        self.frame_menu_bar = QFrame()
        self.frame_menu_bar.setStyleSheet(
            """
            background-color: grey;
            """
        )
        self.frame_menu_bar.setFixedSize(SIZE_WINDOW_WIDTH / 5.4, SIZE_WINDOW_HEIGHT)
        lyt_frame_menu_bar = QVBoxLayout()

        frame_home_action = self.create_menu_action('Home', PATH_ICON, self.action_clicked_home)
        frame_switches_action = self.create_menu_action('Switches', PATH_ICON, self.action_clicked_switches)
        spc_vertical_exp = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        frame_settings_action = self.create_menu_action('Settings', PATH_ICON, self.action_clicked_settings)
        frame_about_action = self.create_menu_action('About', PATH_ICON, self.action_clicked_about)

        lyt_frame_menu_bar.addWidget(frame_home_action)
        lyt_frame_menu_bar.addWidget(frame_switches_action)
        lyt_frame_menu_bar.addSpacerItem(spc_vertical_exp)
        lyt_frame_menu_bar.addWidget(frame_settings_action)
        lyt_frame_menu_bar.addWidget(frame_about_action)

        self.frame_menu_bar.setLayout(lyt_frame_menu_bar)

    def create_frame_page(self):
        self.frame_page = QFrame()
        self.frame_page.setFixedSize(SIZE_WINDOW_WIDTH / 1.23, SIZE_WINDOW_HEIGHT)
        self.frame_page.setStyleSheet(
            """
            background-color: white;
            """
        )
        lyt_page = QVBoxLayout()
        lyt_page.setAlignment(Qt.AlignCenter)

        self.page_home = self.init_page_home()
        lyt_page.addWidget(self.page_home)

        self.page_switches = self.init_page_switches()
        lyt_page.addWidget(self.page_switches)
        self.page_switches.hide()

        self.page_settings = self.init_page_settings()
        lyt_page.addWidget(self.page_settings)
        self.page_settings.hide()

        self.page_about = self.init_page_about()
        lyt_page.addWidget(self.page_about)
        self.page_about.hide()

        self.frame_page.setLayout(lyt_page)

    def build_ui(self):
        self.setWindowTitle('{} {}'.format(APP_NAME, __version__))
        self.setFixedSize(SIZE_WINDOW_WIDTH, SIZE_WINDOW_HEIGHT)

        # Main widget
        self.main_widget = QWidget()
        self.main_widget.setStyleSheet(
            """
            background-color: grey;
            """
        )

        lyt_main = QHBoxLayout()
        lyt_main.setAlignment(Qt.AlignLeft)
        lyt_main.setContentsMargins(0, 0, 0, 0)

        # Frames
        self.create_frame_page()
        self.create_frame_menu_bar()

        # Add to main layout
        lyt_main.addWidget(self.frame_menu_bar)
        lyt_main.addWidget(self.frame_page)

        self.main_widget.setLayout(lyt_main)
        self.setCentralWidget(self.main_widget)

        self.show()

    def init_tray_icon(self):
        # Init tray icon
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(PATH_ICON))
        self.tray_icon.activated.connect(self.sys_tray_activation)

        # Tray actions
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(self.close_app)

        # Tray menu
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def close_app(self):
        self.tray_icon.hide()
        qApp.quit()

    def sys_tray_activation(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()
        elif reason == QSystemTrayIcon.MiddleClick:
            self.hide()
    
    def selection_change(self, index):
        new_switch_name = self.switch_selector.itemText(index)
        img_path = '{}{}.png'.format(
            PATH_SWITCH_IMG,
            SWITCHES[new_switch_name]
            )
        img = QPixmap(img_path)
        self.img_container.setPixmap(img.scaled(QSize(SWITCH_HEIGHT, SWITCH_WIDTH)))
        self.__ctrl.change_switch_selected(SWITCHES[new_switch_name])

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            APP_NAME,
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )

    @staticmethod
    def create_menu_action(name, icon_path, callback):
        frame = QFrame()
        lyt_frame = QHBoxLayout()

        # Icon
        icon_container = QLabel()
        img = QPixmap(icon_path)
        icon_container.setPixmap(img.scaled(QSize(40, 40)))

        # Label
        button = QPushButton(name)
        button.clicked.connect(callback)

        lyt_frame.addWidget(icon_container)
        lyt_frame.addWidget(button)
        frame.setLayout(lyt_frame)

        return frame
