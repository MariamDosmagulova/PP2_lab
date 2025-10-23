import os

path = r"C:\Users\user\Documents\PP2\labs\lab6"
file_path = os.path.join(path, "file1.txt")
with open(file_path, "r") as f:
    lines = f.readlines() #читает весь файл целиком и возвращает их как список
    print(lines)
    print(len(lines))
