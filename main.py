import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from buttons import Ui_Dialog

class table(QMainWindow):
    def __init__(self):
        super(table, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = table()
    window.show()

    sys.exit(app.exec())