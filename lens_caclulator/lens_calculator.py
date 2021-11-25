from PySide6.QtWidgets import QApplication, QWidget, QPushButton


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):

        quit_button = QPushButton("Quit", self)
        quit_button.move(320, 570)
        quit_button.clicked.connect(QApplication.instance() .quit)


        self.setFixedSize(400, 600)
        self.setWindowTitle("Login Window")

        self.show()


if __name__ == " __main__":
    app = QApplication([])

    login_window = LoginWindow()

    app.exec()

# import sys
# from PySide6.QtWidgets import QApplication, QPushButton
#
# app = QApplication(sys.argv)
#
# window = QPushButton("Push Me")
# window.show()
#
# app.exec_()
