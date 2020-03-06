# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(577, 377)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(577, 377))
        Form.setMaximumSize(QtCore.QSize(577, 377))
        Form.setWindowOpacity(0.9)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/register/图片资源/register_background.jpg);\n"
"}")
        self.main_menu_btn = QtWidgets.QPushButton(Form)
        self.main_menu_btn.setGeometry(QtCore.QRect(20, 10, 50, 50))
        self.main_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(202, 43, 255);\n"
"    color:rgb(255, 170, 0);\n"
"    border:3px solid rgb(255, 102, 197);\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px double rgb(251, 121, 255);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(208, 0, 208);\n"
"}")
        self.main_menu_btn.setCheckable(True)
        self.main_menu_btn.setObjectName("main_menu_btn")
        self.about_btn = QtWidgets.QPushButton(Form)
        self.about_btn.setGeometry(QtCore.QRect(100, 10, 50, 50))
        self.about_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(202, 43, 255);\n"
"    color:rgb(255, 170, 0);\n"
"    border:3px solid rgb(255, 102, 197);\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px double rgb(251, 121, 255);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(255, 29, 187);\n"
"}")
        self.about_btn.setCheckable(False)
        self.about_btn.setObjectName("about_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(70, 70, 50, 50))
        self.reset_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(202, 43, 255);\n"
"    color:rgb(255, 170, 0);\n"
"    border:3px solid rgb(255, 102, 197);\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px double rgb(251, 121, 255);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(255, 29, 187);\n"
"}")
        self.reset_btn.setCheckable(False)
        self.reset_btn.setObjectName("reset_btn")
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(10, 100, 50, 50))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(202, 43, 255);\n"
"    color:rgb(255, 170, 0);\n"
"    border:3px solid rgb(255, 102, 197);\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px double rgb(251, 121, 255);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(255, 29, 187);\n"
"}")
        self.exit_btn.setCheckable(False)
        self.exit_btn.setObjectName("exit_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(157, 100, 301, 264))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(17)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setStyleSheet("color:rgb(60, 193, 195);\n"
"font: 75 18pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setStyleSheet("color:rgb(60, 193, 195);\n"
"font: 75 18pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_le.setMinimumSize(QtCore.QSize(0, 37))
        self.password_le.setStyleSheet("background-color: transparent;\n"
"color: rgb(43, 53, 255);\n"
"border:none;\n"
"border-bottom:3px solid cyan;\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 35))
        self.label_3.setStyleSheet("color:rgb(60, 193, 195);\n"
"font: 75 18pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.repassword_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.repassword_le.setMinimumSize(QtCore.QSize(0, 37))
        self.repassword_le.setStyleSheet("background-color: transparent;\n"
"color: rgb(43, 53, 255);\n"
"border:none;\n"
"border-bottom:3px solid cyan;\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.repassword_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repassword_le.setClearButtonEnabled(True)
        self.repassword_le.setObjectName("repassword_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.repassword_le)
        self.account_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_le.setMinimumSize(QtCore.QSize(0, 37))
        self.account_le.setStyleSheet("background-color: transparent;\n"
"color: rgb(43, 53, 255);\n"
"border:none;\n"
"border-bottom:3px solid cyan;\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.account_le.setClearButtonEnabled(True)
        self.account_le.setObjectName("account_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_le)
        self.register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMinimumSize(QtCore.QSize(177, 43))
        self.register_btn.setMaximumSize(QtCore.QSize(177, 16777215))
        self.register_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.register_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(144, 255, 252);\n"
"    color: rgb(255, 97, 24);\n"
"    border-radius:7px;\n"
"    border:1px solid rgb(255, 102, 197);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-color: rgb(168, 150, 149);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(87, 233, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(112, 122, 255);\n"
"}")
        self.register_btn.setObjectName("register_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.register_btn)
        self.about_btn.raise_()
        self.reset_btn.raise_()
        self.exit_btn.raise_()
        self.layoutWidget.raise_()
        self.main_menu_btn.raise_()

        self.retranslateUi(Form)
        self.main_menu_btn.clicked['bool'].connect(Form.show_hide_menu)
        self.exit_btn.clicked.connect(Form.exit_pane)
        self.about_btn.clicked.connect(Form.about_author)
        self.reset_btn.clicked.connect(Form.reset)
        self.register_btn.clicked.connect(Form.check_register)
        self.account_le.textChanged['QString'].connect(Form.enable_register)
        self.password_le.textChanged['QString'].connect(Form.enable_register)
        self.repassword_le.textChanged['QString'].connect(Form.enable_register)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.account_le, self.password_le)
        Form.setTabOrder(self.password_le, self.repassword_le)
        Form.setTabOrder(self.repassword_le, self.register_btn)
        Form.setTabOrder(self.register_btn, self.main_menu_btn)
        Form.setTabOrder(self.main_menu_btn, self.exit_btn)
        Form.setTabOrder(self.exit_btn, self.reset_btn)
        Form.setTabOrder(self.reset_btn, self.about_btn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menu_btn.setText(_translate("Form", "菜单"))
        self.about_btn.setText(_translate("Form", "关于"))
        self.reset_btn.setText(_translate("Form", "重置"))
        self.exit_btn.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "账       号:"))
        self.label_2.setText(_translate("Form", "密       码:"))
        self.label_3.setText(_translate("Form", "确认密码:"))
        self.register_btn.setText(_translate("Form", "注册"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
