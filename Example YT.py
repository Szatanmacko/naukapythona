from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit
from PySide6.QtGui import QCloseEvent, QPixmap


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.login_line_edit = QLabel()

        self.setup()

    def setup(self):
        width = 400

        pix_label = QLabel(self)
        pixmap = QPixmap("profile_pic_mask.png").scaled(250, 250)
        pix_label.setPixmap(pixmap)
        pix_label.move((width - 250) / 2, 50)

        self.login_line_edit = QLineEdit("login", self)
        self.login_line_edit.setFixedWidth(200)
        self.login_line_edit.move(100, 350)

        pass_line_edit = QLineEdit("password", self)
        pass_line_edit.setFixedWidth(200)
        pass_line_edit.move(100, 380)

        submit_btn = QPushButton("Submit", self)
        submit_btn.move((width - submit_btn.size().width()) / 2, 410)

        quit_btn = QPushButton("Quit", self)
        quit_btn.move(320, 570)

        submit_btn.clicked.connect(self.submit)
        quit_btn.clicked.connect(QApplication.instance().quit)

        self.setFixedSize(width, 600)
        self.setWindowTitle("Login Window")

        self.show()

    def submit(self):
        print(self.login_line_edit.text())

    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self, "Close App", "Do you want to close",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication([])

    login_window = LoginWindow()

    app.exec()

