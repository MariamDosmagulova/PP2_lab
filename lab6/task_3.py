import os

path = r"C:\Users\user\Documents\PP2\labs\lab6\file1.txt"

if os.path.exists(path):
    print("path exist")
    print("file name:", os.path.basename(path))#укажет последнюю часть пути
    print("directory:", os.path.dirname(path))#укажет весь путь до указанного файла
else:
    print("no such path")