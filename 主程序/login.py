# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 377)
        Form.setMinimumSize(QtCore.QSize(577, 377))
        Form.setMaximumSize(QtCore.QSize(577, 377))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.login_top_label = QtWidgets.QLabel(self.widget)
        self.login_top_label.setGeometry(QtCore.QRect(0, 0, 581, 131))
        self.login_top_label.setStyleSheet("")
        self.login_top_label.setText("")
        self.login_top_label.setObjectName("login_top_label")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 157, 47))
        self.label.setMinimumSize(QtCore.QSize(157, 47))
        self.label.setMaximumSize(QtCore.QSize(157, 47))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 18pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.close_btn = QtWidgets.QPushButton(self.widget)
        self.close_btn.setGeometry(QtCore.QRect(540, 0, 33, 33))
        self.close_btn.setMinimumSize(QtCore.QSize(33, 33))
        self.close_btn.setMaximumSize(QtCore.QSize(33, 33))
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
        self.close_btn.setObjectName("close_btn")
        self.mini_btn = QtWidgets.QPushButton(self.widget)
        self.mini_btn.setGeometry(QtCore.QRect(510, 0, 33, 33))
        self.mini_btn.setMinimumSize(QtCore.QSize(33, 33))
        self.mini_btn.setMaximumSize(QtCore.QSize(33, 33))
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
        self.mini_btn.setObjectName("mini_btn")
        self.verticalLayout.addWidget(self.widget)
        self.login_bottom = QtWidgets.QWidget(Form)
        self.login_bottom.setStyleSheet("background-color: rgb(188, 252, 255);")
        self.login_bottom.setObjectName("login_bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.login_bottom)
        self.horizontalLayout.setContentsMargins(13, 0, 13, 13)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_btn = QtWidgets.QPushButton(self.login_bottom)
        self.register_btn.setFlat(True)
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.login_bottom)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.auto_login_cb = QtWidgets.QCheckBox(self.widget_3)
        self.auto_login_cb.setMinimumSize(QtCore.QSize(73, 0))
        self.auto_login_cb.setObjectName("auto_login_cb")
        self.gridLayout.addWidget(self.auto_login_cb, 4, 0, 1, 1)
        self.remenber_pwd_cb = QtWidgets.QCheckBox(self.widget_3)
        self.remenber_pwd_cb.setMinimumSize(QtCore.QSize(73, 0))
        self.remenber_pwd_cb.setObjectName("remenber_pwd_cb")
        self.gridLayout.addWidget(self.remenber_pwd_cb, 4, 2, 1, 1)
        self.pwd_le = QtWidgets.QLineEdit(self.widget_3)
        self.pwd_le.setMinimumSize(QtCore.QSize(0, 37))
        self.pwd_le.setStyleSheet("QLineEdit{\n"
"    font-size: 17px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom: 1px solid lightgray;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom: 1px solid rgb(85, 255, 255);\n"
"}\n"
"")
        self.pwd_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_le.setClearButtonEnabled(True)
        self.pwd_le.setObjectName("pwd_le")
        self.gridLayout.addWidget(self.pwd_le, 1, 0, 1, 3)
        self.account_cb = QtWidgets.QComboBox(self.widget_3)
        self.account_cb.setMinimumSize(QtCore.QSize(0, 37))
        self.account_cb.setStyleSheet("QComboBox{\n"
"    font-size: 17px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox:hover{\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QComboBox:focus{\n"
"    border-bottom: 1px solid rgb(85, 255, 255);\n"
"}\n"
"QComboBox::drop-down{\n"
"    background-color: transparent;\n"
"    width: 60px;\n"
"    height: 40px;\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: url(:/login/图片资源/login_combtn.png);\n"
"    width: 60px;\n"
"    height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    min-height: 47px;\n"
"}")
        self.account_cb.setEditable(True)
        self.account_cb.setObjectName("account_cb")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/register/图片资源/register_background.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/图片资源/Rice.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon1, "")
        self.gridLayout.addWidget(self.account_cb, 0, 0, 1, 3)
        self.login_btn = QtWidgets.QPushButton(self.widget_3)
        self.login_btn.setEnabled(True)
        self.login_btn.setMinimumSize(QtCore.QSize(223, 47))
        self.login_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 7px;\n"
"    background-color: rgb(71, 214, 214);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(80, 184, 229);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(51, 133, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/login/图片资源/login_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QtCore.QSize(27, 27))
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 5, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font-size:17px;\n"
"    border-radius: 7px;\n"
"    background-color: rgb(188, 252, 255);\n"
"    color: rgb(255, 75, 240);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(157, 237, 237);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(66, 198, 198);\n"
"}")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)
        self.erweima_btn = QtWidgets.QPushButton(self.login_bottom)
        self.erweima_btn.setMinimumSize(QtCore.QSize(77, 77))
        self.erweima_btn.setMaximumSize(QtCore.QSize(77, 77))
        self.erweima_btn.setToolTip("")
        self.erweima_btn.setStyleSheet("border-image: url(:/login/图片资源/WeChat.png);")
        self.erweima_btn.setText("")
        self.erweima_btn.setObjectName("erweima_btn")
        self.horizontalLayout.addWidget(self.erweima_btn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.login_bottom)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.show_register_pane)
        self.erweima_btn.clicked.connect(Form.show_erweima)
        self.login_btn.clicked.connect(Form.login)
        self.account_cb.editTextChanged['QString'].connect(Form.enable_login_btn)
        self.pwd_le.textChanged['QString'].connect(Form.enable_login_btn)
        self.remenber_pwd_cb.clicked['bool'].connect(Form.remenber_pwd)
        self.auto_login_cb.clicked['bool'].connect(Form.auto_login)
        self.mini_btn.clicked.connect(Form.mini_pane)
        self.close_btn.clicked.connect(Form.close_pane)
        self.pushButton.clicked.connect(Form.face_recognition)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.account_cb, self.pwd_le)
        Form.setTabOrder(self.pwd_le, self.auto_login_cb)
        Form.setTabOrder(self.auto_login_cb, self.remenber_pwd_cb)
        Form.setTabOrder(self.remenber_pwd_cb, self.pushButton)
        Form.setTabOrder(self.pushButton, self.login_btn)
        Form.setTabOrder(self.login_btn, self.erweima_btn)
        Form.setTabOrder(self.erweima_btn, self.register_btn)
        Form.setTabOrder(self.register_btn, self.mini_btn)
        Form.setTabOrder(self.mini_btn, self.close_btn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "个人理财系统"))
        self.close_btn.setToolTip(_translate("Form", "关闭"))
        self.close_btn.setText(_translate("Form", "×"))
        self.mini_btn.setToolTip(_translate("Form", "最小化"))
        self.mini_btn.setText(_translate("Form", "－"))
        self.register_btn.setText(_translate("Form", "注册账号"))
        self.auto_login_cb.setText(_translate("Form", "自动登录"))
        self.remenber_pwd_cb.setText(_translate("Form", "记住密码"))
        self.account_cb.setItemText(0, _translate("Form", "   Admin"))
        self.account_cb.setItemText(1, _translate("Form", "   Rice"))
        self.login_btn.setText(_translate("Form", "安全登录"))
        self.pushButton.setText(_translate("Form", "刷脸登录"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
