from PyQt5.Qt import *
from register import Ui_Form


class RegisterPane(QWidget, Ui_Form):

    exit_signal = pyqtSignal()  # 自定义信号
    register_account_pwd_signal = pyqtSignal(str, str)  # 自定义信号

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.animation_targets = [self.about_btn, self.reset_btn, self.exit_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]
        self.initUI()

    def initUI(self):
        self.main_menu_btn.animateClick(1000)

    def show_hide_menu(self, checked):

        animation_group = QSequentialAnimationGroup(self)  # 创建动画组

        for idx, target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()  # 创建属性动画
            animation.setTargetObject(target)  # 设置动画目标对象
            animation.setPropertyName(b"pos")  # 设置属性名(位置)
            animation.setEndValue(self.main_menu_btn.pos())  # 设置动画的起始位置
            animation.setStartValue(self.animation_targets_pos[idx])
            animation.setDuration(137)  # 设置动画时长(毫秒)
            animation.setEasingCurve(QEasingCurve.OutBounce)  # 设置动画效果弹性
            animation_group.addAnimation(animation)  # 向动画组中加入动画
        animation_group.setDirection(checked)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)  # 开始执行动画 , 执行结束后删除动画组

    def exit_pane(self):
        self.exit_signal.emit()  # 发射该信号

    def about_author(self):
        QMessageBox.about(self, "毕业设计", "个人理财系统")

    def reset(self):
        self.account_le.clear()  # 清空编辑框
        self.password_le.clear()  # 清空编辑框
        self.repassword_le.clear()  # 清空编辑框

    def check_register(self):
        self.register_account_pwd_signal.emit(self.account_le.text(), self.password_le.text())

    def enable_register(self):
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        rp_txt = self.repassword_le.text()
        if len(account_txt) > 0 and len(password_txt) > 0 and len(rp_txt) > 0:
            if password_txt == rp_txt:
                self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_signal.connect(lambda: print("exit"))  # 将该信号连接槽函数
    window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()
    sys.exit(app.exec_())
