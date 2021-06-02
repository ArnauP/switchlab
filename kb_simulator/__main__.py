from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont

from .controllers.main_controller import MainController
from resources import switchlab_rc
from .utils.utils import *
from .constants import *


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon(PATH_ICON))
    load_style_sheet(PATH_STYLE, app)
    font = QFont('Arial', 11, QFont.Bold)
    app.setFont(font)
    main_ctrl = MainController()
    app.exec_()


if __name__ == "__main__":
    main()
