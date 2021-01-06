from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont
from .controllers.main_controller import MainController
from .utils import utils


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon(utils.get_path('kb_simulator/resources/icons/app_icon.png')))
    utils.load_style_sheet(utils.get_path('kb_simulator/resources/style/style.css'), app)
    font = QFont('Arial', 11, QFont.Bold)
    app.setFont(font)
    main_ctrl = MainController()
    app.exec_()


if __name__ == "__main__":
    main()