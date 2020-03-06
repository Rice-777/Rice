from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import Ui_Form
from ConnectSqlServer import ConnectSqlServer
from ComprehensiveAnalysis import Analysis
import time
import os
import webbrowser
import qdarkgraystyle


class MainWindowPane(QWidget, Ui_Form):

    add_cash_pane_signal = pyqtSignal()
    modify_cash_pane_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.initUI()
        self.move_flag = False

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)
        self.setStyleSheet(qdarkgraystyle.load_stylesheet())

        self.time_lab.setText(time.strftime("%Y-%m-%d", time.gmtime()))
        self.time_lab.setFont(QFont("雅黑", 12))
        self.top_welcome_lab.setText("                       生活需要规划 , 理财拥有美好明天 ")

        self.close_btn = QPushButton("×", self)
        self.close_btn.resize(33, 33)
        self.mini_btn = QPushButton("－", self)
        self.mini_btn.resize(33, 33)
        self.max_btn = QPushButton("□", self)
        self.max_btn.resize(33, 33)
        self.mini_btn.setStyleSheet("QPushButton{\n"
                                    "    font: 75 18pt \"微软雅黑\";\n"
                                    "    border-radius: 3px;\n"
                                    "    background-color: transparent;\n"
                                    "    color: white;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "    background-color: rgb(69, 209, 209);\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background-color: rgb(97, 237, 237);\n"
                                    "}")
        self.max_btn.setStyleSheet("QPushButton{\n"
"    font: 75 18pt \"微软雅黑\";\n"
"    border-radius: 3px;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(69, 209, 209);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(97, 237, 237);\n"
"}")
        self.close_btn.setStyleSheet("QPushButton{\n"
"    font: 75 18pt \"微软雅黑\";\n"
"    border-radius: 3px;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 28, 21);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 57, 53);\n"
"}")

        self.close_btn.setToolTip("关闭")
        self.max_btn.setToolTip("最大化 / 普通")
        self.mini_btn.setToolTip("最小化")

        self.close_btn.clicked.connect(self.close)
        self.max_btn.clicked.connect(self.max_normal)
        self.mini_btn.clicked.connect(self.showMinimized)

        self.main_fun()

    def main_fun(self):
        self.connect_Sql = ConnectSqlServer(host='127.0.0.1', port=1433, user='sa', pwd='777', db='Rice')

        self.my_account_cb.activated[str].connect(self.Active1)
        self.guihua_cb.activated[str].connect(self.Active2)
        self.canpin_cb.activated[str].connect(self.Active3)
        self.tools_cb.activated[str].connect(self.Active4)
        self.remind_cb.activated[str].connect(self.Active5)

        self.cash_lab = [self.cash2_lab, self.cash3_lab, self.cash4_lab, self.cash5_lab, self.cash6_lab, self.cash7_lab]

        self.pushButton.clicked.connect(self.add_btn)
        self.pushButton_2.clicked.connect(self.modify_btn)
        self.pushButton_3.clicked.connect(self.del_btn)
        self.relash_btn.clicked.connect(self.re_flash_btn)

        self.qdl = QDialog(self, Qt.FramelessWindowHint)
        self.qdl.setSizeGripEnabled(True)
        self.qdl.resize(897, 581)

        self.cal = QCalendarWidget(self.qdl)
        self.cal.hide()

        self.label = QtWidgets.QLabel(self.qdl)
        self.label.setGeometry(QtCore.QRect(284, 58, 55, 33))
        self.label_2 = QtWidgets.QLabel(self.qdl)
        self.label_2.setGeometry(QtCore.QRect(284, 84, 55, 33))
        self.label_3 = QtWidgets.QLabel(self.qdl)
        self.label_3.setGeometry(QtCore.QRect(284, 110, 55, 33))
        self.label_4 = QtWidgets.QLabel(self.qdl)
        self.label_4.setGeometry(QtCore.QRect(284, 136, 55, 33))
        self.label_5 = QtWidgets.QLabel(self.qdl)
        self.label_5.setGeometry(QtCore.QRect(284, 162, 55, 33))
        self.label_6 = QtWidgets.QLabel(self.qdl)
        self.label_6.setGeometry(QtCore.QRect(284, 188, 55, 33))
        self.label_7 = QtWidgets.QLabel(self.qdl)
        self.label_7.setGeometry(QtCore.QRect(284, 214, 75, 33))
        self.label_8 = QtWidgets.QLabel(self.qdl)
        self.label_8.setGeometry(QtCore.QRect(284, 240, 55, 33))
        self.lineEdit = QtWidgets.QLineEdit(self.qdl)
        self.lineEdit.setGeometry(QtCore.QRect(350, 58, 133, 33))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.qdl)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 84, 133, 33))
        self.lineEdit_3 = QtWidgets.QLineEdit(self.qdl)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 110, 133, 33))
        self.lineEdit_4 = QtWidgets.QLineEdit(self.qdl)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 136, 133, 33))
        self.lineEdit_5 = QtWidgets.QLineEdit(self.qdl)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 162, 133, 33))
        self.lineEdit_6 = QtWidgets.QLineEdit(self.qdl)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 188, 133, 33))
        self.lineEdit_7 = QtWidgets.QLineEdit(self.qdl)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 214, 133, 33))
        self.textEdit = QtWidgets.QTextEdit(self.qdl)
        self.textEdit.setGeometry(QtCore.QRect(350, 240, 131, 192))
        self.pushButton = QtWidgets.QPushButton(self.qdl)
        self.pushButton.setGeometry(QtCore.QRect(360, 490, 75, 33))
        self.pushButton_2 = QtWidgets.QPushButton(self.qdl)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 20, 75, 33))
        self.pushButton_3 = QtWidgets.QPushButton(self.qdl)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 110, 75, 33))

        self.label.setText("摘要")
        self.label_2.setText("银行名称")
        self.label_3.setText("日期")
        self.label_4.setText("存款金额")
        self.label_5.setText("利息收入")
        self.label_6.setText("取款金额")
        self.label_7.setText("扣除手续费")
        self.label_8.setText("备注")
        self.pushButton.setText("保存")
        self.pushButton_2.setText("x")
        self.pushButton_3.setText("设置日期")

        self.pushButton_2.clicked.connect(self.close_add_cunkuan_pane)
        self.pushButton_3.clicked[bool].connect(self.cunkuan_cal_show_hide)
        self.pushButton_3.setCheckable(True)
        self.pushButton.clicked.connect(self.save)

        self.test_lab = QLabel(self)
        self.test_lab.hide()
        self.cunkuan_lab = [self.test_lab, self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
                             self.lineEdit_5, self.lineEdit_6, self.lineEdit_7, self.textEdit]

        self.qdl_jiekuan = QDialog(self, Qt.FramelessWindowHint)
        self.qdl_jiekuan.setSizeGripEnabled(True)
        self.qdl_jiekuan.resize(751, 545)

        self.cal_jiekuan = QCalendarWidget(self.qdl_jiekuan)
        self.cal_jiekuan.hide()

        self.jk_label = QtWidgets.QLabel(self.qdl_jiekuan)
        self.jk_label.setGeometry(QtCore.QRect(180, 30, 54, 33))
        self.jk_label_2 = QtWidgets.QLabel(self.qdl_jiekuan)
        self.jk_label_2.setGeometry(QtCore.QRect(170, 110, 54, 33))
        self.jk_label_3 = QtWidgets.QLabel(self.qdl_jiekuan)
        self.jk_label_3.setGeometry(QtCore.QRect(170, 190, 54, 33))
        self.jk_label_4 = QtWidgets.QLabel(self.qdl_jiekuan)
        self.jk_label_4.setGeometry(QtCore.QRect(170, 240, 54, 33))
        self.jk_label_5 = QtWidgets.QLabel(self.qdl_jiekuan)
        self.jk_label_5.setGeometry(QtCore.QRect(180, 300, 54, 33))
        self.jk_lineEdit = QtWidgets.QLineEdit(self.qdl_jiekuan)
        self.jk_lineEdit.setGeometry(QtCore.QRect(300, 30, 133, 33))
        self.jk_lineEdit_3 = QtWidgets.QLineEdit(self.qdl_jiekuan)
        self.jk_lineEdit_3.setGeometry(QtCore.QRect(300, 190, 133, 33))
        self.jk_lineEdit_4 = QtWidgets.QLineEdit(self.qdl_jiekuan)
        self.jk_lineEdit_4.setGeometry(QtCore.QRect(300, 240, 133, 33))
        self.jk_textEdit = QtWidgets.QTextEdit(self.qdl_jiekuan)
        self.jk_textEdit.setGeometry(QtCore.QRect(300, 280, 131, 192))
        self.jk_pushButton = QtWidgets.QPushButton(self.qdl_jiekuan)
        self.jk_pushButton.setGeometry(QtCore.QRect(470, 110, 75, 33))
        self.jk_lineEdit_2 = QtWidgets.QLineEdit(self.qdl_jiekuan)
        self.jk_lineEdit_2.setGeometry(QtCore.QRect(302, 110, 131, 33))
        self.jk_pushButton_2 = QtWidgets.QPushButton(self.qdl_jiekuan)
        self.jk_pushButton_2.setGeometry(QtCore.QRect(310, 500, 75, 33))
        self.jk_pushButton_3 = QtWidgets.QPushButton(self.qdl_jiekuan)
        self.jk_pushButton_3.setGeometry(QtCore.QRect(660, 10, 75, 33))

        self.jk_label.setText("摘要")
        self.jk_label_2.setText("日期")
        self.jk_label_3.setText("借入金额")
        self.jk_label_4.setText("借出金额")
        self.jk_label_5.setText("备注")
        self.jk_pushButton.setText("设置日期")
        self.jk_pushButton_2.setText("保存")
        self.jk_pushButton_3.setText("x")

        self.jk_pushButton_3.clicked.connect(self.close_add_jiekuan_pane)
        self.jk_pushButton.clicked[bool].connect(self.jiekuan_cal_show_hide)
        self.jk_pushButton.setCheckable(True)
        self.jk_pushButton_2.clicked.connect(self.jiekuan_save)

        self.jiekuan_lab = [self.test_lab, self.jk_lineEdit, self.jk_lineEdit_2, self.jk_lineEdit_3, self.jk_lineEdit_4, self.jk_textEdit]

        self.qdl_touzi = QDialog(self, Qt.FramelessWindowHint)
        self.qdl_touzi.setSizeGripEnabled(True)
        self.qdl_touzi.resize(757, 577)

        self.cal_touzi = QCalendarWidget(self.qdl_touzi)
        self.cal_touzi.hide()

        self.touzi_lineEdit_2 = QtWidgets.QLineEdit(self.qdl_touzi)
        self.touzi_lineEdit_2.setGeometry(QtCore.QRect(312, 120, 131, 33))
        self.touzi_label = QtWidgets.QLabel(self.qdl_touzi)
        self.touzi_label.setGeometry(QtCore.QRect(190, 40, 54, 33))
        self.touzi_label_2 = QtWidgets.QLabel(self.qdl_touzi)
        self.touzi_label_2.setGeometry(QtCore.QRect(190, 120, 54, 33))
        self.touzi_pushButton_2 = QtWidgets.QPushButton(self.qdl_touzi)
        self.touzi_pushButton_2.setGeometry(QtCore.QRect(320, 510, 75, 33))
        self.touzi_lineEdit_4 = QtWidgets.QLineEdit(self.qdl_touzi)
        self.touzi_lineEdit_4.setGeometry(QtCore.QRect(310, 250, 133, 33))
        self.touzi_label_5 = QtWidgets.QLabel(self.qdl_touzi)
        self.touzi_label_5.setGeometry(QtCore.QRect(190, 290, 54, 33))
        self.touzi_pushButton = QtWidgets.QPushButton(self.qdl_touzi)
        self.touzi_pushButton.setGeometry(QtCore.QRect(480, 120, 75, 33))
        self.touzi_lineEdit_3 = QtWidgets.QLineEdit(self.qdl_touzi)
        self.touzi_lineEdit_3.setGeometry(QtCore.QRect(310, 180, 133, 33))
        self.touzi_label_3 = QtWidgets.QLabel(self.qdl_touzi)
        self.touzi_label_3.setGeometry(QtCore.QRect(180, 180, 54, 33))
        self.touzi_label_4 = QtWidgets.QLabel(self.qdl_touzi)
        self.touzi_label_4.setGeometry(QtCore.QRect(180, 250, 54, 33))
        self.touzi_textEdit = QtWidgets.QTextEdit(self.qdl_touzi)
        self.touzi_textEdit.setGeometry(QtCore.QRect(310, 290, 131, 192))
        self.touzi_lineEdit = QtWidgets.QLineEdit(self.qdl_touzi)
        self.touzi_lineEdit.setGeometry(QtCore.QRect(310, 40, 133, 33))
        self.touzi_pushButton_3 = QtWidgets.QPushButton(self.qdl_touzi)
        self.touzi_pushButton_3.setGeometry(QtCore.QRect(660, 20, 75, 33))
        self.touzi_lineEdit_5 = QtWidgets.QLineEdit(self.qdl_touzi)
        self.touzi_lineEdit_5.setGeometry(QtCore.QRect(310, 220, 133, 33))
        self.touzi_label_6 = QtWidgets.QLabel(self.qdl_touzi)
        self.touzi_label_6.setGeometry(QtCore.QRect(180, 220, 54, 33))

        self.touzi_label.setText("摘要")
        self.touzi_label_2.setText("日期")
        self.touzi_pushButton_2.setText("保存")
        self.touzi_label_5.setText("备注")
        self.touzi_pushButton.setText("设置日期")
        self.touzi_label_3.setText("投资金额")
        self.touzi_label_4.setText("损失金额")
        self.touzi_pushButton_3.setText("x")
        self.touzi_label_6.setText("收益金额")

        self.touzi_pushButton_3.clicked.connect(self.close_add_touzi_pane)
        self.touzi_pushButton.clicked[bool].connect(self.touzi_cal_show_hide)
        self.touzi_pushButton.setCheckable(True)
        self.touzi_pushButton_2.clicked.connect(self.touzi_save)

        self.touzi_lab = [self.test_lab, self.touzi_lineEdit, self.touzi_lineEdit_2, self.touzi_lineEdit_3, self.touzi_lineEdit_5,
                          self.touzi_lineEdit_4, self.touzi_textEdit]

        self.qdl_import = QDialog(self, Qt.FramelessWindowHint)
        self.qdl_import.setSizeGripEnabled(True)
        self.qdl_import.resize(677, 537)

        self.cal_import_1 = QCalendarWidget(self.qdl_import)
        self.cal_import_1.hide()
        self.cal_import_2 = QCalendarWidget(self.qdl_import)
        self.cal_import_2.hide()

        self.event_pushButton = QtWidgets.QPushButton(self.qdl_import)
        self.event_pushButton.setGeometry(QtCore.QRect(220, 350, 75, 33))
        self.event_pushButton_2 = QtWidgets.QPushButton(self.qdl_import)
        self.event_pushButton_2.setGeometry(QtCore.QRect(577, 20, 75, 33))
        self.event_pushButton_3 = QtWidgets.QPushButton(self.qdl_import)
        self.event_pushButton_3.setGeometry(QtCore.QRect(370, 50, 75, 33))
        self.event_pushButton_4 = QtWidgets.QPushButton(self.qdl_import)
        self.event_pushButton_4.setGeometry(QtCore.QRect(360, 260, 75, 33))
        self.event_riqi_lab = QtWidgets.QLabel(self.qdl_import)
        self.event_riqi_lab.setGeometry(QtCore.QRect(100, 60, 54, 33))
        self.remind_event_riqi_lab = QtWidgets.QLabel(self.qdl_import)
        self.remind_event_riqi_lab.setGeometry(QtCore.QRect(100, 270, 54, 33))
        self.event_lab = QtWidgets.QLabel(self.qdl_import)
        self.event_lab.setGeometry(QtCore.QRect(100, 140, 54, 33))
        self.event_textEdit = QtWidgets.QTextEdit(self.qdl_import)
        self.event_textEdit.setGeometry(QtCore.QRect(180, 120, 141, 101))
        self.event_riqi_le = QtWidgets.QLineEdit(self.qdl_import)
        self.event_riqi_le.setGeometry(QtCore.QRect(180, 50, 141, 33))
        self.remind_event_riqi_le = QtWidgets.QLineEdit(self.qdl_import)
        self.remind_event_riqi_le.setGeometry(QtCore.QRect(180, 260, 141, 33))

        self.event_pushButton.setText("保存")
        self.event_pushButton_2.setText("x")
        self.event_pushButton_3.setText("设置日期")
        self.event_pushButton_4.setText("设置日期")
        self.event_riqi_lab.setText("事件日期")
        self.remind_event_riqi_lab.setText("提醒日期")
        self.event_lab.setText("内容")

        self.event_pushButton_2.clicked.connect(self.close_add_import_pane)
        self.event_pushButton_3.clicked[bool].connect(self.import_cal_1_show_hide)
        self.event_pushButton_3.setCheckable(True)
        self.event_pushButton_4.clicked[bool].connect(self.import_cal_2_show_hide)
        self.event_pushButton_4.setCheckable(True)
        self.event_pushButton.clicked.connect(self.import_save)

        self.import_lab = [self.test_lab, self.event_riqi_le, self.event_textEdit, self.remind_event_riqi_le]

        self.main_fram.hide()

    def add_btn(self):
        if self.pushButton.objectName() == "add_cash_btn":
            self.add_cash_pane_signal.emit()
        if self.pushButton.objectName() == "add_cunkuan_btn":
            self.add_cunkuan()
        if self.pushButton.objectName() == "add_jiekuan_btn":
            self.add_jiekuan()
        if self.pushButton.objectName() == "add_touzi_btn":
            self.add_touzi()
        if self.pushButton.objectName() == "add_import_btn":
            self.add_import()

    def re_flash_btn(self):
        if self.relash_btn.objectName() == "re_flash_cash_btn":
            for _ in range(len(self.cash_lab)):
                self.cash_lab[_].setText("")
            result = self.connect_Sql.ExecQuery("select * from Cash;")
            if not result:
                pass
            else:
                for _ in range(len(result)):
                    result[_] = str(result[_]).replace('(', '  ')
                    result[_] = str(result[_]).replace(')', ' ')
                    result[_] = str(result[_]).replace(',', '     ')
                for _ in range(len(result)):
                    self.cash_lab[_].setText(result[_])
        if self.relash_btn.objectName() == "re_flash_cunkuan_btn":
            self.re_flash_cunkuan()
        if self.relash_btn.objectName() == "re_flash_jiekuan_btn":
            self.re_flash_jiekuan()
        if self.relash_btn.objectName() == "re_flash_touzi_btn":
            self.re_flash_touzi()
        if self.relash_btn.objectName() == "re_flash_import_btn":
            self.re_flash_import()

    def del_btn(self):
        if self.pushButton_3.objectName() == "del_cash_btn":
            del_id = QInputDialog(self, Qt.FramelessWindowHint)
            del_id.setInputMode(1)
            del_id.setIntRange(1, 777)
            del_id.setIntValue(7)
            del_id.setLabelText("输入待删除记录的编号")
            del_id.setOkButtonText("确定")
            del_id.setCancelButtonText("取消")
            del_id.open()
            del_id.intValueSelected.connect(self.set_del_cash_id_btn)
        if self.pushButton_3.objectName() == "del_cunkuan_btn":
            self.del_cunkuan()
        if self.pushButton_3.objectName() == "del_jiekuan_btn":
            self.del_jiekuan()
        if self.pushButton_3.objectName() == "del_touzi_btn":
            self.del_touzi()
        if self.pushButton_3.objectName() == "del_import_btn":
            self.del_import()

    def set_del_cash_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Cash where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "删除失败 , 查无该记录 !!! ")
        else:
            sql = "delete from Cash where id = '{}';".format(val)
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " ", "删除成功")

    def modify_btn(self):
        if self.pushButton_2.objectName() == "modify_cash_btn":
            self.modify_cash_pane_signal.emit()
        if self.pushButton_2.objectName() == "modify_cunkuan_btn":
            self.modify_cunkuan()
        if self.pushButton_2.objectName() == "modify_jiekuan_btn":
            self.modify_jiekuan()
        if self.pushButton_2.objectName() == "modify_touzi_btn":
            self.modify_touzi()
        if self.pushButton_2.objectName() == "modify_import_btn":
            self.modify_import()

    def max_normal(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def cash_btn(self):
        self.pushButton.setObjectName("add_cash_btn")
        self.pushButton_3.setObjectName("del_cash_btn")
        self.pushButton_2.setObjectName("modify_cash_btn")
        self.relash_btn.setObjectName("re_flash_cash_btn")
        self.cash1_lab.setText(" 编号    摘要              日期                 收入金额   支出金额          备注")
        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
        result = self.connect_Sql.ExecQuery("select * from Cash;")
        for _ in range(len(result)):
            result[_] = str(result[_]).replace('(', '  ')
            result[_] = str(result[_]).replace(')', ' ')
            result[_] = str(result[_]).replace(',', '     ')
        for _ in range(len(result)):
            self.cash_lab[_].setText(result[_])
        self.main_fram.show()

    def cunkuan_btn(self):
        self.pushButton.setObjectName("add_cunkuan_btn")
        self.pushButton_3.setObjectName("del_cunkuan_btn")
        self.pushButton_2.setObjectName("modify_cunkuan_btn")
        self.relash_btn.setObjectName("re_flash_cunkuan_btn")
        self.cash1_lab.setText(" 编号    摘要         银行名称       日期         存款金额   利息收入  取款金额   扣除手续费   备注")

        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
        result = self.connect_Sql.ExecQuery("select * from Cunkuan;")
        for _ in range(len(result)):
            result[_] = str(result[_]).replace('(', '  ')
            result[_] = str(result[_]).replace(')', ' ')
            result[_] = str(result[_]).replace(',', '     ')
        for _ in range(len(result)):
            self.cash_lab[_].setText(result[_])
        self.main_fram.show()

    def add_cunkuan(self):
        self.pushButton.setObjectName("add_save")
        for _ in range(len(self.cunkuan_lab)):
            self.cunkuan_lab[_].setText("")
        self.qdl.show()
        self.hide()

    def cunkuan_cal_show_hide(self, press):
        self.cal.setGridVisible(True)
        self.cal.move(497, 157)
        self.cal.clicked[QDate].connect(self.cunkuan_calender)
        if press:
            self.cal.show()
        else:
            self.cal.hide()

    def cunkuan_calender(self, date):
        date = QDate(date)  # 对日期进行自定义的前提
        self.lineEdit_3.setText(date.toString("yyyy-MM-dd"))

    def close_add_cunkuan_pane(self):
        self.pushButton_5.click()
        self.qdl.close()
        self.show()

    def save(self):
        if self.pushButton.objectName() == "add_save":
            sql = "insert into Cunkuan values('{}','{}','{}','{}','{}','{}','{}','{}');".format(self.lineEdit.text(),
                                                                            self.lineEdit_2.text(),
                                                                            self.lineEdit_3.text(),
                                                                            self.lineEdit_4.text(),
                                                                            self.lineEdit_5.text(),
                                                                            self.lineEdit_6.text(),
                                                                            self.lineEdit_7.text(),
                                                                            self.textEdit.toPlainText())
            result = self.connect_Sql.ExecQuery("select * from Cunkuan;")
            if len(result) == 6:
                QMessageBox.information(self, " 错误 ", "添加失败 , 请联系管理员 ")
                self.pushButton_5.click()
                self.show()
                self.qdl.hide()
            else:
                self.connect_Sql.ExecNoneQuery(sql)
                QMessageBox.information(self, " 恭喜 ", "添加成功!!!")
                self.pushButton_5.click()
                self.show()
                self.qdl.hide()
        if self.pushButton.objectName() == "modify_save":
            sql = "update Cunkuan set zhaiyao = '{}', yinghnag_name = '{}', riqi = '{}', cunkuan_val = '{}', lixi_val = '{}', qukuan_val = '{}', shouxu_val = '{}', beizhu = '{}' where id = '{}';".format(
                                                                                    self.lineEdit.text(),
                                                                                    self.lineEdit_2.text(),
                                                                                    self.lineEdit_3.text(),
                                                                                    self.lineEdit_4.text(),
                                                                                    self.lineEdit_5.text(),
                                                                                    self.lineEdit_6.text(),
                                                                                    self.lineEdit_7.text(),
                                                                                    self.textEdit.toPlainText(),
                                                                                    self.test_lab.text())
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " 恭喜 ", "修改成功!!!")
            self.pushButton_5.click()
            self.show()
            self.qdl.hide()

    def modify_cunkuan(self):
        self.pushButton.setObjectName("modify_save")
        del_id = QInputDialog(self, Qt.FramelessWindowHint)
        del_id.setInputMode(1)
        del_id.setIntRange(1, 777)
        del_id.setIntValue(7)
        del_id.setLabelText("输入待修改记录的编号")
        del_id.setOkButtonText("确定")
        del_id.setCancelButtonText("取消")
        del_id.open()
        del_id.intValueSelected.connect(self.set_modify_cunkuan_id_btn)

    def set_modify_cunkuan_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Cunkuan where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "修改失败 , 查无该记录 !!! ")
        else:
            cash_info = result[0]
            for _ in range(9):
                self.cunkuan_lab[_].setText(str(cash_info[_]))
            self.qdl.show()
            self.hide()

    def del_cunkuan(self):
        del_id = QInputDialog(self, Qt.FramelessWindowHint)
        del_id.setInputMode(1)
        del_id.setIntRange(1, 777)
        del_id.setIntValue(7)
        del_id.setLabelText("输入待删除记录的编号")
        del_id.setOkButtonText("确定")
        del_id.setCancelButtonText("取消")
        del_id.open()
        del_id.intValueSelected.connect(self.set_del_cunkuan_id_btn)

    def set_del_cunkuan_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Cunkuan where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "删除失败 , 查无该记录 !!! ")
        else:
            sql = "delete from Cunkuan where id = '{}';".format(val)
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " ", "删除成功")

    def re_flash_cunkuan(self):
        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
        result = self.connect_Sql.ExecQuery("select * from Cunkuan;")
        if not result:
            pass
        else:
            for _ in range(len(result)):
                result[_] = str(result[_]).replace('(', '  ')
                result[_] = str(result[_]).replace(')', ' ')
                result[_] = str(result[_]).replace(',', '     ')
            for _ in range(len(result)):
                self.cash_lab[_].setText(result[_])

    def touzi_btn(self):
        self.pushButton.setObjectName("add_touzi_btn")
        self.pushButton_3.setObjectName("del_touzi_btn")
        self.pushButton_2.setObjectName("modify_touzi_btn")
        self.relash_btn.setObjectName("re_flash_touzi_btn")
        self.cash1_lab.setText(" 编号    摘要              日期                 投资金额   收益金额  损失金额        备注")

        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
        result = self.connect_Sql.ExecQuery("select * from Touzi;")
        for _ in range(len(result)):
            result[_] = str(result[_]).replace('(', '  ')
            result[_] = str(result[_]).replace(')', ' ')
            result[_] = str(result[_]).replace(',', '     ')
        for _ in range(len(result)):
            self.cash_lab[_].setText(result[_])
        self.main_fram.show()

    def add_touzi(self):
        self.touzi_pushButton_2.setObjectName("add_save")
        for _ in range(len(self.touzi_lab)):
            self.touzi_lab[_].setText("")
        self.qdl_touzi.show()
        self.hide()

    def modify_touzi(self):
        self.touzi_pushButton_2.setObjectName("modify_save")
        del_id = QInputDialog(self, Qt.FramelessWindowHint)
        del_id.setInputMode(1)
        del_id.setIntRange(1, 777)
        del_id.setIntValue(7)
        del_id.setLabelText("输入待修改记录的编号")
        del_id.setOkButtonText("确定")
        del_id.setCancelButtonText("取消")
        del_id.open()
        del_id.intValueSelected.connect(self.set_modify_touzi_id_btn)

    def del_touzi(self):
        del_id = QInputDialog(self, Qt.FramelessWindowHint)
        del_id.setInputMode(1)
        del_id.setIntRange(1, 777)
        del_id.setIntValue(7)
        del_id.setLabelText("输入待删除记录的编号")
        del_id.setOkButtonText("确定")
        del_id.setCancelButtonText("取消")
        del_id.open()
        del_id.intValueSelected.connect(self.set_del_touzi_id_btn)

    def set_del_touzi_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Touzi where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "删除失败 , 查无该记录 !!! ")
        else:
            sql = "delete from Touzi where id = '{}';".format(val)
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " ", "删除成功")

    def re_flash_touzi(self):
        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
        result = self.connect_Sql.ExecQuery("select * from Touzi;")
        for _ in range(len(result)):
            result[_] = str(result[_]).replace('(', '  ')
            result[_] = str(result[_]).replace(')', ' ')
            result[_] = str(result[_]).replace(',', '     ')
        for _ in range(len(result)):
            self.cash_lab[_].setText(result[_])

    def set_modify_touzi_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Touzi where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "修改失败 , 查无该记录 !!! ")
        else:
            cash_info = result[0]
            for _ in range(7):
                self.touzi_lab[_].setText(str(cash_info[_]))
            self.qdl_touzi.show()
            self.hide()

    def close_add_touzi_pane(self):
        self.pushButton_6.click()
        self.qdl_touzi.close()
        self.show()

    def touzi_cal_show_hide(self, press):
        self.cal_touzi.setGridVisible(True)
        self.cal_touzi.move(497, 157)
        self.cal_touzi.clicked[QDate].connect(self.touzi_calender)
        if press:
            self.cal_touzi.show()
        else:
            self.cal_touzi.hide()

    def touzi_calender(self, date):
        date = QDate(date)  # 对日期进行自定义的前提
        self.touzi_lineEdit_2.setText(date.toString("yyyy-MM-dd"))

    def touzi_save(self):
        if self.touzi_pushButton_2.objectName() == "add_save":
            sql = "insert into Touzi values('{}','{}','{}','{}','{}','{}');".format(self.touzi_lineEdit.text(),
                                                                                self.touzi_lineEdit_2.text(),
                                                                                self.touzi_lineEdit_3.text(),
                                                                                self.touzi_lineEdit_5.text(),
                                                                                self.touzi_lineEdit_4.text(),
                                                                                self.touzi_textEdit.toPlainText())
            result = self.connect_Sql.ExecQuery("select * from Touzi;")
            if len(result) == 6:
                QMessageBox.information(self, " 错误 ", "添加失败 , 请联系管理员 ")
                self.pushButton_6.click()
                self.show()
                self.qdl_touzi.hide()
            else:
                self.connect_Sql.ExecNoneQuery(sql)
                QMessageBox.information(self, " 恭喜 ", "添加成功!!!")
                self.pushButton_6.click()
                self.show()
                self.qdl_touzi.hide()
        if self.touzi_pushButton_2.objectName() == "modify_save":
            sql = "update Touzi set zhaiyao = '{}', riqi = '{}', touzi_val = '{}', shouyi_val = '{}', shunshi_val = '{}', beizhu = '{}' where id = '{}';".format(
                self.touzi_lineEdit.text(),
                self.touzi_lineEdit_2.text(),
                self.touzi_lineEdit_3.text(),
                self.touzi_lineEdit_5.text(),
                self.touzi_lineEdit_4.text(),
                self.touzi_textEdit.toPlainText(),
                self.test_lab.text())
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " 恭喜 ", "修改成功!!!")
            self.pushButton_6.click()
            self.show()
            self.qdl_touzi.hide()

    def loan_btn(self):
        self.pushButton.setObjectName("add_jiekuan_btn")
        self.pushButton_3.setObjectName("del_jiekuan_btn")
        self.pushButton_2.setObjectName("modify_jiekuan_btn")
        self.relash_btn.setObjectName("re_flash_jiekuan_btn")
        self.cash1_lab.setText(" 编号    摘要              日期                 借入金额   借出金额          备注")

        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
        result = self.connect_Sql.ExecQuery("select * from Jiedai;")
        for _ in range(len(result)):
            result[_] = str(result[_]).replace('(', '  ')
            result[_] = str(result[_]).replace(')', ' ')
            result[_] = str(result[_]).replace(',', '     ')
        for _ in range(len(result)):
            self.cash_lab[_].setText(result[_])
        self.main_fram.show()

    def add_jiekuan(self):
        self.jk_pushButton_2.setObjectName("add_save")
        for _ in range(len(self.jiekuan_lab)):
            self.jiekuan_lab[_].setText("")
        self.qdl_jiekuan.show()
        self.hide()

    def modify_jiekuan(self):
        self.jk_pushButton_2.setObjectName("modify_save")
        del_id = QInputDialog(self, Qt.FramelessWindowHint)
        del_id.setInputMode(1)
        del_id.setIntRange(1, 777)
        del_id.setIntValue(7)
        del_id.setLabelText("输入待修改记录的编号")
        del_id.setOkButtonText("确定")
        del_id.setCancelButtonText("取消")
        del_id.open()
        del_id.intValueSelected.connect(self.set_modify_jiekuan_id_btn)

    def re_flash_jiekuan(self):
        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
        result = self.connect_Sql.ExecQuery("select * from Jiedai;")
        if not result:
            pass
        else:
            for _ in range(len(result)):
                result[_] = str(result[_]).replace('(', '  ')
                result[_] = str(result[_]).replace(')', ' ')
                result[_] = str(result[_]).replace(',', '     ')
            for _ in range(len(result)):
                self.cash_lab[_].setText(result[_])

    def del_jiekuan(self):
        del_id = QInputDialog(self, Qt.FramelessWindowHint)
        del_id.setInputMode(1)
        del_id.setIntRange(1, 777)
        del_id.setIntValue(7)
        del_id.setLabelText("输入待删除记录的编号")
        del_id.setOkButtonText("确定")
        del_id.setCancelButtonText("取消")
        del_id.open()
        del_id.intValueSelected.connect(self.set_del_jiekuan_id_btn)

    def set_del_jiekuan_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Jiedai where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "删除失败 , 查无该记录 !!! ")
        else:
            sql = "delete from Jiedai where id = '{}';".format(val)
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " ", "删除成功")

    def set_modify_jiekuan_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Jiedai where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "修改失败 , 查无该记录 !!! ")
        else:
            cash_info = result[0]
            for _ in range(6):
                self.jiekuan_lab[_].setText(str(cash_info[_]))
            self.qdl_jiekuan.show()
            self.hide()

    def close_add_jiekuan_pane(self):
        self.pushButton_7.click()
        self.qdl_jiekuan.close()
        self.show()

    def jiekuan_cal_show_hide(self, press):
        self.cal_jiekuan.setGridVisible(True)
        self.cal_jiekuan.move(457, 157)
        self.cal_jiekuan.clicked[QDate].connect(self.jiekuan_calender)
        if press:
            self.cal_jiekuan.show()
        else:
            self.cal_jiekuan.hide()

    def jiekuan_calender(self, date):
        date = QDate(date)  # 对日期进行自定义的前提
        self.jk_lineEdit_2.setText(date.toString("yyyy-MM-dd"))

    def jiekuan_save(self):
        if self.jk_pushButton_2.objectName() == "add_save":
            sql = "insert into Jiedai values('{}','{}','{}','{}','{}');".format(self.jk_lineEdit.text(),
                                                                                self.jk_lineEdit_2.text(),
                                                                                self.jk_lineEdit_3.text(),
                                                                                self.jk_lineEdit_4.text(),
                                                                                self.jk_textEdit.toPlainText())
            result = self.connect_Sql.ExecQuery("select * from Jiedai;")
            if len(result) == 6:
                QMessageBox.information(self, " 错误 ", "添加失败 , 请联系管理员 ")
                self.pushButton_7.click()
                self.show()
                self.qdl_jiekuan.hide()
            else:
                self.connect_Sql.ExecNoneQuery(sql)
                QMessageBox.information(self, " 恭喜 ", "添加成功!!!")
                self.pushButton_7.click()
                self.show()
                self.qdl_jiekuan.hide()
        if self.jk_pushButton_2.objectName() == "modify_save":
            sql = "update Jiedai set zhaiyao = '{}', riqi = '{}', jieru_val = '{}', jiechu_val = '{}', beizhu = '{}' where id = '{}';".format(
                self.jk_lineEdit.text(),
                self.jk_lineEdit_2.text(),
                self.jk_lineEdit_3.text(),
                self.jk_lineEdit_4.text(),
                self.jk_textEdit.toPlainText(),
                self.test_lab.text())
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " 恭喜 ", "修改成功!!!")
            self.pushButton_7.click()
            self.show()
            self.qdl_jiekuan.hide()

    def zonghe_btn(self):
        ca = Analysis()
        ca.fun()

    def import_btn(self):
        self.pushButton.setObjectName("add_import_btn")
        self.pushButton_3.setObjectName("del_import_btn")
        self.pushButton_2.setObjectName("modify_import_btn")
        self.relash_btn.setObjectName("re_flash_import_btn")
        self.cash1_lab.setText(" 编号    事件日期      事件内容                                        "
                               "                                                           提醒日期   ")

        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
        result = self.connect_Sql.ExecQuery("select * from Important;")
        for _ in range(len(result)):
            result[_] = str(result[_]).replace('(', '  ')
            result[_] = str(result[_]).replace(')', ' ')
            result[_] = str(result[_]).replace(',', '     ')
        for _ in range(len(result)):
            self.cash_lab[_].setText(result[_])
        self.main_fram.show()

    def add_import(self):
        self.event_pushButton.setObjectName("add_save")
        for _ in range(len(self.import_lab)):
            self.import_lab[_].setText("")
        self.qdl_import.show()
        self.hide()

    def modify_import(self):
        self.event_pushButton.setObjectName("modify_save")
        del_id = QInputDialog(self, Qt.FramelessWindowHint)
        del_id.setInputMode(1)
        del_id.setIntRange(1, 777)
        del_id.setIntValue(7)
        del_id.setLabelText("输入待修改记录的编号")
        del_id.setOkButtonText("确定")
        del_id.setCancelButtonText("取消")
        del_id.open()
        del_id.intValueSelected.connect(self.set_modify_import_id_btn)

    def set_modify_import_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Important where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "修改失败 , 查无该记录 !!! ")
        else:
            cash_info = result[0]
            for _ in range(4):
                self.import_lab[_].setText(str(cash_info[_]))
            self.qdl_import.show()
            self.hide()

    def del_import(self):
        del_id = QInputDialog(self, Qt.FramelessWindowHint)
        del_id.setInputMode(1)
        del_id.setIntRange(1, 777)
        del_id.setIntValue(7)
        del_id.setLabelText("输入待删除记录的编号")
        del_id.setOkButtonText("确定")
        del_id.setCancelButtonText("取消")
        del_id.open()
        del_id.intValueSelected.connect(self.set_del_import_id_btn)

    def set_del_import_id_btn(self, val):
        result = self.connect_Sql.ExecQuery("select * from Important where id = '{}';".format(val))
        if not result:
            QMessageBox.information(self, " 错误 ", "删除失败 , 查无该记录 !!! ")
        else:
            sql = "delete from Important where id = '{}';".format(val)
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " ", "删除成功")

    def re_flash_import(self):
        for _ in range(len(self.cash_lab)):
            self.cash_lab[_].setText("")
            result = self.connect_Sql.ExecQuery("select * from Important;")
        if not result:
            pass
        else:
            for _ in range(len(result)):
                result[_] = str(result[_]).replace('(', '  ')
                result[_] = str(result[_]).replace(')', ' ')
                result[_] = str(result[_]).replace(',', '     ')
            for _ in range(len(result)):
                self.cash_lab[_].setText(result[_])

    def close_add_import_pane(self):
        self.pushButton_11.click()
        self.qdl_import.close()
        self.show()

    def import_cal_1_show_hide(self, press):
        self.cal_import_1.setGridVisible(True)
        self.cal_import_1.move(363, 107 - 57)
        self.cal_import_1.clicked[QDate].connect(self.import_1_calender)
        if press:
            self.cal_import_1.show()
        else:
            self.cal_import_1.hide()

    def import_1_calender(self, date):
        date = QDate(date)  # 对日期进行自定义的前提
        self.event_riqi_le.setText(date.toString("yyyy-MM-dd"))

    def import_cal_2_show_hide(self, press):
        self.cal_import_2.setGridVisible(True)
        self.cal_import_2.move(363, 257 + 57)
        self.cal_import_2.clicked[QDate].connect(self.import_2_calender)
        if press:
            self.cal_import_2.show()
        else:
            self.cal_import_2.hide()

    def import_2_calender(self, date):
        date = QDate(date)  # 对日期进行自定义的前提
        self.remind_event_riqi_le.setText(date.toString("yyyy-MM-dd"))

    def import_save(self):
        if self.event_pushButton.objectName() == "add_save":
            sql = "insert into Important values('{}','{}','{}');".format(self.event_riqi_le.text(), self.event_textEdit.toPlainText(), self.remind_event_riqi_le.text())
            result = self.connect_Sql.ExecQuery("select * from Important;")
            if len(result) == 6:
                QMessageBox.information(self, " 错误 ", "添加失败 , 请联系管理员 ")
                self.pushButton_11.click()
                self.show()
                self.qdl_import.hide()
            else:
                self.connect_Sql.ExecNoneQuery(sql)
                QMessageBox.information(self, " 恭喜 ", "添加成功!!!")
                self.pushButton_11.click()
                self.show()
                self.qdl_import.hide()
        if self.event_pushButton.objectName() == "modify_save":
            sql = "update Important set event_riqi = '{}', event = '{}', remind_riqi = '{}'  where id = '{}';".format(
                self.event_riqi_le.text(),
                self.event_textEdit.toPlainText(),
                self.remind_event_riqi_le.text(),
                self.test_lab.text())
            self.connect_Sql.ExecNoneQuery(sql)
            QMessageBox.information(self, " 恭喜 ", "修改成功!!!")
            self.pushButton_11.click()
            self.show()
            self.qdl_import.hide()

    def zixun_btn(self):
        os.system("C:\\Windows\\System32\\notepad.exe\
                    Stock_Data.txt")

    def Active1(self, str_):
        if str_ == "现金":
            self.cash_btn()
        if str_ == "存款":
            self.cunkuan_btn()
        if str_ == "投资":
            self.touzi_btn()
        if str_ == "借贷":
            self.loan_btn()
        if str_ == "综合分析        ":
            self.zonghe_btn()
        
    def Active2(self, str_):
        if str_ == "理财规划案例":
            webbrowser.open('file:///E:/web/case.htm', new=0, autoraise=True)
        if str_ == "理财规划交流":
            webbrowser.open('https://tieba.baidu.com/f?kw=%E7%90%86%E8%B4%A2%E8%A7%84%E5%88%92&fr=fenter&prequery=%E7%'
                            '90%86%E8%B4%A2%E8%A7%84%E5%88%92%E4%BA%A4%E6%B5%81', new=0, autoraise=True)

    def Active3(self, str_):
        if str_ == "银行本币理财":
            webbrowser.open('https://finance.sina.com.cn/', new=0, autoraise=True)
        if str_ == "银行外币理财":
            webbrowser.open('https://finance.sina.com.cn/', new=0, autoraise=True)
        if str_ == "人寿保险":
            webbrowser.open('https://finance.sina.com.cn/', new=0, autoraise=True)
        if str_ == "财产保险":
            webbrowser.open('https://finance.sina.com.cn/', new=0, autoraise=True)
        if str_ == "基金公司查询":
            webbrowser.open('http://finance.sina.com.cn/fund/jjlm/index.shtml', new=0, autoraise=True)

    def Active4(self, str_):
        if str_ == "理财计算器":
            webbrowser.open('http://www.icbc.com.cn/icbc/', new=0, autoraise=True)
        if str_ == "生活工具":
            webbrowser.open('https://s.taobao.com/search?q=%E7%94%9F%E6%B4%BB%E5%B7%A5%E5%85%B7&imgfile=&commend=all&s'
                            'sid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&in'
                            'itiative_id=tbindexz_20170306', new=0, autoraise=True)
        if str_ == "理财网站导航":
            webbrowser.open('file:///E:/web/lczs.htm', new=0, autoraise=True)

    def Active5(self, str_):
        if str_ == "重要事件       ":
            self.import_btn()
        if str_ == "重点资讯":
            os.system("C:\\Windows\\System32\\mspaint.exe\
                        Important_event_picture.png")

    def resizeEvent(self, QResizeEvent):
        self.close_btn_w = self.close_btn.width()
        self.mwp_w = self.width()
        self.close_btn.move(self.mwp_w - self.close_btn_w + 1, -1)
        self.max_btn.move(self.mwp_w - self.close_btn_w + 3 - self.max_btn.width(), -1)
        self.mini_btn.move(self.mwp_w - self.close_btn_w + 5 - self.max_btn.width() - 33, -1)

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


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = MainWindowPane()
    window.show()

    sys.exit(app.exec_())
