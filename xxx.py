from PySide6.QtWidgets import QApplication, QWidget, QPushButton


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):

        self.setFixedSize(400, 600)
        self.setWindowTitle("Login window")

        self.show()


if __name__ == " __main__":
    app = QApplication([])

    login_window = LoginWindow()

    app.exec()