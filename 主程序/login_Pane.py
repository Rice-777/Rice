from PyQt5.Qt import *
from login import Ui_Form


class Erweima(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pm = QPixmap(":/login/图片资源/WeChat.png")

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(657, 300, 597, 597)

        self.lab = QLabel(self)
        self.lab.setPixmap(self.pm)
        self.lab.setGeometry(0, 0, 597, 597)  # 设置载体的大小
        self.btn = QPushButton(" X ", self)
        self.btn.setGeometry(553, 9, 37, 37)
        self.btn.clicked.connect(self.close)


class LoginPane(QWidget, Ui_Form):

    show_register_pane_signal = pyqtSignal()
    login_signal = pyqtSignal(str, str)
    show_erweima_signal = pyqtSignal()
    face_recognition_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.initUI()
        self.move_flag = False

    def initUI(self):
        self.setWindowOpacity(0.9)
        self.setWindowFlags(Qt.FramelessWindowHint)

        movie = QMovie(":/login/图片资源/login_top_label.gif")
        movie.setScaledSize(QSize(577, 147))
        self.login_top_label.setMovie(movie)
        movie.start()

    def show_register_pane(self):
        self.show_register_pane_signal.emit()

    def face_recognition(self):
        self.face_recognition_signal.emit()

    def login(self):
        self.account = self.account_cb.currentText()
        if self.account[0] == " ":
            self.account = self.account[3:]
        self.login_signal.emit(self.account, self.pwd_le.text())

    def show_erweima(self):
        self.show_erweima_signal.emit()

    def enable_login_btn(self):
        account = self.account_cb.currentText()
        if len(account) > 0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def auto_login(self, checked):
        if checked:
            self.remenber_pwd_cb.setChecked(True)

    def remenber_pwd(self, checked):
        if not checked:
            self.auto_login_cb.setChecked(False)

    def show_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.login_bottom.pos())
        animation.setKeyValueAt(0.2, self.login_bottom.pos() + QPoint(13, 0))
        animation.setKeyValueAt(0.5, self.login_bottom.pos())
        animation.setKeyValueAt(0.7, self.login_bottom.pos() + QPoint(-13, 0))
        animation.setKeyValueAt(1, self.login_bottom.pos())

        animation.setDirection(370)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def close_pane(self):
        self.close()

    def mini_pane(self):
        self.setWindowState(Qt.WindowMinimized)

    def mousePressEvent(self, qme):
        if qme.button() == Qt.LeftButton:
            self.move_flag = True
            self.mouse_x = qme.globalX()
            self.mouse_y = qme.globalY()
            self.origin_x = self.x()
            self.origin_y = self.y()

    def mouseMoveEvent(self, qme):
        if self.move_flag:
            move_x = qme.globalX() - self.mouse_x
            move_y = qme.globalY() - self.mouse_y
            target_x = self.origin_x + move_x
            target_y = self.origin_y + move_y
            self.move(target_x, target_y)

    def mouseReleaseEvent(self, qme):
        self.move_flag = False

    def keyPressEvent(self, kpe):
        account = self.account_cb.currentText()
        if account[0] == " ":
            account = account[3:]
        self.login_signal.emit(account, self.pwd_le.text())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())
