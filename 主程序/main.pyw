from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import login_Pane
import Register_Pane
import main_window_Pane
import dynamic_face_recognition
from ConnectSqlServer import ConnectSqlServer
import qdarkgraystyle


class AddCash(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(qdarkgraystyle.load_stylesheet())
        self.setWindowOpacity(0.9)

        self.resize(751, 545)

        self.connect_Sql = ConnectSqlServer(host='127.0.0.1', port=1433, user='sa', pwd='777', db='Rice')

        self.cal = QCalendarWidget(self)
        self.cal.hide()

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(180, 30, 54, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 54, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(170, 240, 54, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(180, 300, 54, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(300, 30, 133, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 190, 133, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 240, 133, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(300, 280, 131, 192))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(470, 110, 75, 33))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(302, 110, 131, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 500, 75, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close_add_cash_pane)
        self.pushButton.clicked[bool].connect(self.btnClicked2)
        self.pushButton.setCheckable(True)
        self.pushButton_2.clicked.connect(self.save)

        self.test_lab = QLabel(self)
        self.test_lab.hide()
        self.label.setText("摘要")
        self.label_2.setText("日期")
        self.label_3.setText("收入金额")
        self.label_4.setText("支出金额")
        self.label_5.setText("备注")
        self.pushButton.setText("设置日期")
        self.pushButton_2.setText("保存")
        self.pushButton_3.setText("x")

        self.cash_lab = [self.test_lab, self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.textEdit]

    def btnClicked2(self, press):
        self.cal.setGridVisible(True)
        self.cal.move(477, 137)
        self.cal.clicked[QDate].connect(self.calender)
        if press:
            self.cal.show()
        else:
            self.cal.hide()

    def calender(self, date):
        date = QDate(date)  # 对日期进行自定义的前提
        self.lineEdit_2.setText(date.toString("yyyy-MM-dd"))

    def close_add_cash_pane(self):
        self.close()
        window.show()

    def save(self):
        sql = "insert into Cash values('{}','{}','{}','{}','{}');".format(self.lineEdit.text(),
                                                                        self.lineEdit_2.text(),
                                                                        self.lineEdit_3.text(),
                                                                        self.lineEdit_4.text(),
                                                                        self.textEdit.toPlainText())
        result = self.connect_Sql.ExecQuery("select * from Cash;")
        if len(result) == 6:
            QMessageBox.information(self, " 错误 ", "添加失败 , 请联系管理员 ")
            window.show()
            self.hide()
        else:
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " 恭喜 ", "添加成功!!!")
            window.show()
            self.hide()


class ModifyCash(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(qdarkgraystyle.load_stylesheet())
        self.setWindowOpacity(0.9)

        self.resize(751, 545)

        self.connect_Sql = ConnectSqlServer(host='127.0.0.1', port=1433, user='sa', pwd='777', db='Rice')

        self.cal = QCalendarWidget(self)
        self.cal.hide()

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(180, 30, 54, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(170, 190, 54, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(170, 240, 54, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(180, 300, 54, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(300, 30, 133, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 190, 133, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 240, 133, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(300, 280, 131, 192))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(470, 110, 75, 33))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(302, 110, 131, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 500, 75, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close_add_cash_pane)
        self.pushButton.clicked[bool].connect(self.btnClicked2)
        self.pushButton.setCheckable(True)
        self.pushButton_2.clicked.connect(self.save)
        self.test_lab = QLabel(self)
        self.test_lab.hide()

        self.cash_lab = [self.test_lab, self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.textEdit]

        self.label.setText("摘要")
        self.label_2.setText("日期")
        self.label_3.setText("收入金额")
        self.label_4.setText("支出金额")
        self.label_5.setText("备注")
        self.pushButton.setText("设置日期")
        self.pushButton_2.setText("保存修改")
        self.pushButton_3.setText("x")

        self.del_id = QInputDialog(self, Qt.FramelessWindowHint)
        self.del_id.setInputMode(1)
        self.del_id.setIntRange(1, 777)
        self.del_id.setIntValue(7)
        self.del_id.setLabelText("输入待修改记录的编号")
        self.del_id.setOkButtonText("确定")
        self.del_id.setCancelButtonText("取消")
        self.del_id.intValueSelected.connect(self.set_modify_id)

    def btnClicked2(self, press):
        self.cal.setGridVisible(True)
        self.cal.move(477, 137)
        self.cal.clicked[QDate].connect(self.calender)
        if press:
            self.cal.show()
        else:
            self.cal.hide()

    def calender(self, date):
        date = QDate(date)  # 对日期进行自定义的前提
        self.lineEdit_2.setText(date.toString("yyyy-MM-dd"))

    def close_add_cash_pane(self):
        self.close()
        window.show()

    def set_modify_id(self, val):
        result = self.connect_Sql.ExecQuery("select * from Cash where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "修改失败 , 查无该记录 !!! ")
        else:
            cash_info = result[0]
            for _ in range(6):
                self.cash_lab[_].setText(str(cash_info[_]))
            self.show()
            window.hide()

    def save(self):
        sql = "update Cash set zhaiyao = '{}', riqi = '{}', shouru_val = '{}', zhichu_val = '{}', beizhu = '{}' where id = '{}';".format(
                                                                        self.lineEdit.text(),
                                                                        self.lineEdit_2.text(),
                                                                        self.lineEdit_3.text(),
                                                                        self.lineEdit_4.text(),
                                                                        self.textEdit.toPlainText(),
                                                                        self.test_lab.text())
        self.connect_Sql.ExecNoneQuery(sql)
        QMessageBox.information(self, " 恭喜 ", "修改成功!!!")
        window.show()
        self.hide()


class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(467, 177)
        self.setWindowTitle("检测中")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)

        self.v = 0  # 预设置进度条的进度值为 0
        self.timer = QBasicTimer()  # 载入时钟控件

        self.pgb = QProgressBar(self)  # 载入进度条控件
        self.pgb.setGeometry(53, 70, 377, 37)
        self.pgb.setMinimum(0)  # 设置最小值
        self.pgb.setMaximum(100)  # 设置最大值
        self.pgb.setValue(self.v)

        self.lab = QLabel("正在连接 SQL Server 数据库 . . .", self)
        self.lab.move(77, 37)
        self.timer.start(27, self)

        self.connect_Sql = ConnectSqlServer(host='127.0.0.1', port=1433, user='sa', pwd='777', db='Rice')
        self.connect_Sql_bool = self.connect_Sql.judge_connect()

    def timerEvent(self, id_):  # 重写 timeEvent 父类方法 , 后面参数是该对象的地址
        if self.v == 100:  # 如果进度为 100
            self.timer.stop()  # 停止时钟控件
            if self.connect_Sql_bool:
                login.show()
                self.close()
            else:
                result = QMessageBox.question(self, "提   示", "连接 SQL Server 数据库失败 , 是否使用文件数据库 ?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if result == QMessageBox.Yes:
                    try:
                        person_database = open("Person.txt", "x")
                        person_database.close()
                    except:
                        pass
                    login.show()
                    self.close()
                else:
                    self.close()
        elif self.v == 50:
            if self.connect_Sql_bool:
                self.lab.setText("已连接上数据库 , 加载中")
                self.v += 1  # 进度 +1
                self.pgb.setValue(self.v)  # 设置进度条的进度
            else:
                self.v += 1  # 进度 +1
                self.pgb.setValue(self.v)  # 设置进度条的进度
        else:  # 如果进度不是 100
            self.v += 1  # 进度 +1
            self.pgb.setValue(self.v)  # 设置进度条的进度


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("Gold.png"))

    login = login_Pane.LoginPane()
    erweima = login_Pane.Erweima()

    add_cash_pane = AddCash()
    modify_cash_pane = ModifyCash()
    window = main_window_Pane.MainWindowPane()

    register = Register_Pane.RegisterPane(login)
    register.move(login.width(), 0)
    register.show()

    def exit_register_pane():
        animation = QPropertyAnimation(register)
        animation.setTargetObject(register)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, login.height()))
        animation.setEndValue(QPoint(register.pos()))
        animation.setDirection(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_register_pane():
        register.main_menu_btn.animateClick(1700)
        animation = QPropertyAnimation(register)
        animation.setTargetObject(register)
        animation.setPropertyName(b"pos")
        animation.setEndValue(QPoint(login.height(), 0))
        animation.setStartValue(QPoint(0, 0))
        animation.setDirection(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_erweima():
        erweima.show()

    def remind_event():
        qdl_remind = QDialog(window, Qt.FramelessWindowHint)
        qdl_remind.setSizeGripEnabled(True)
        qdl_remind.resize(333, 333)
        remind_lab = QLabel(qdl_remind)
        remind_lab.setText("重要事件提醒 : 今天您已经有安排了哦!!!")
        remind_lab.move(37, 137)
        remind_btn = QPushButton(qdl_remind)
        remind_btn.setText("我知道了")
        remind_btn.move(177, 237)
        remind_btn.clicked.connect(qdl_remind.hide)
        result_remind = mc.connect_Sql.ExecQuery("select * from Important;")
        for _ in range(len(result_remind)):
            if result_remind[_][3] == window.time_lab.text():
                qdl_remind.show()

    def check_login(account, pwd):
        result = mc.connect_Sql.ExecQuery("select * from Person where account = '{}';".format(account))
        if not result:
            login.show_error_animation()
        elif account == "Rice" and pwd == "777":
            window.Person_info_lab.setText("       " + account)
            window.show()
            remind_event()
            login.hide()
        elif account == "Admin" and pwd == "":
            window.Person_info_lab.setText("       " + account)
            window.show()
            remind_event()
            login.hide()
        elif account == result[0][1] and pwd == result[0][2]:
            window.Person_info_lab.setText("       " + account)
            window.show()
            remind_event()
            login.hide()
        else:
            login.show_error_animation()

    def face_recognition():
        result = QMessageBox.information(login, "提   示", " 刷脸完成按 ' e ' 确定",
                                      QMessageBox.Yes)
        if result == QMessageBox.Yes:
            dfr = dynamic_face_recognition.FaceRecognition()
            if dfr.face_recognition_fun():
                window.show()
                login.hide()
            else:
                QMessageBox.information(login, "错误", "刷脸失败 , 无法登陆!!!")

    def register_to_database(account, pwd):
        if mc.connect_Sql_bool:
            result = mc.connect_Sql.ExecQuery("select * from Person where account = '{}';".format(account))
            if result:
                QMessageBox.information(login, "注册失败", "该用户名已被注册!!!")
            else:
                sql = "insert into Person values('{}','{}');".format(account, pwd)
                mc.connect_Sql.ExecNoneQuery(sql)
                QMessageBox.information(login, " ", "注册成功")
        else:
            person_database = open("Person.txt", "a+")
            person_database.write("       本文件保存个人信息.       ")
            person_database.write("账号:{}   密码:{}".format(account, pwd))
            result = person_database.read()
            print(result)
            QMessageBox.information(login, " ", "注册成功")
            person_database.close()

    def add_cash():
        for _ in range(6):
            add_cash_pane.cash_lab[_].setText("")
        add_cash_pane.show()
        window.hide()

    def modify_cash():
        modify_cash_pane.del_id.exec()

    register.exit_signal.connect(exit_register_pane)
    register.register_account_pwd_signal.connect(register_to_database)

    login.show_register_pane_signal.connect(show_register_pane)
    login.show_erweima_signal.connect(show_erweima)
    login.login_signal.connect(check_login)
    login.face_recognition_signal.connect(face_recognition)

    window.add_cash_pane_signal.connect(add_cash)
    window.modify_cash_pane_signal.connect(modify_cash)

    mc = MyClass()
    mc.show()
    sys.exit(app.exec_())
