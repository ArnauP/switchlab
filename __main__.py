from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont
from kb_simulator.controllers.main_controller import MainController
from kb_simulator.utils.utils import *
from kb_simulator.constants import *


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon(get_path(PATH_ICON)))
    load_style_sheet(get_path(PATH_STYLE), app)
    font = QFont('Arial', 11, QFont.Bold)
    app.setFont(font)
    main_ctrl = MainController()
    app.exec_()


if __name__ == "__main__":
    main()