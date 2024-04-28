from cryptography.fernet import Fernet


def write_key():
    # Создаем ключ и сохраняем его в файл
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    # Загружаем ключ 'crypto.key' из текущего каталога
    return open('crypto.key', 'rb').read()


def encrypt(filename, key):
    # Зашифруем файл и записываем его
    f = Fernet(key)

    with open(filename, 'rb') as file:
        # прочитать все данные файла
        file_data = file.read()

    # Зашифровать данные
    encrypted_data = f.encrypt(file_data)

    # записать зашифрованный файл
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

    return encrypted_data


def decrypt(filename, key):
    # Расшифруем файл и записываем его
    f = Fernet(key)

    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


