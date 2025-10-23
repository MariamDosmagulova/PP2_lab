import os

path = r"C:\Users\user\Documents\PP2\labs\lab6\lol.txt"

if os.path.exists(path): 
    if os.access(path, os.W_OK):  # Проверяем доступ на запись 
        os.remove(path)
        print("Файл удален")
    else:
        print("Нет доступа")
else:
    print("Файл не существует")