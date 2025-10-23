

#Task 1

import os 


path = r"C:\Users\user\Documents\PP2\labs\lab6" #r сырая строка, позволяет прогр не воспринимать \ как спец символы

items = os.listdir(path) #os.listdir функция возвращает список всех объектов (файлов и папок) в заданом директории

files = []
dirs = []

for i in items:
    full_path = os.path.join(path,i) #os.losdir() возвращает имена а не полные  пути, поэтому добавляем join
    if os.path.isdir(full_path): #os.path.isdir() функция которая проверяет является ли указанный путь папкой
        dirs.append(i)
    else:
        files.append(i)
        
print(f"only directiries: {dirs}")
print(f"only files: {files}")
print(f"all items {items}")

