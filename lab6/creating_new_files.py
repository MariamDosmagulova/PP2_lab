#создаю папку с файлами для заданий:

'''import os 

path = r"C:\Users\user\Documents\PP2\labs\lab6"

f1 = open(os.path.join(path, "file1.txt"), "x") #x - создает новый файл, только если его еще  нет, иначе выдаст ошибку
f1.write("Hiii everyone!")
f1.close()

f2 = open(os.path.join(path, "file2.txt"), "x") #a - создает новый файл, если файл уже есть, он его не трогает, просто добавляет новую инфу в конец 
f2.write("There is nothing interesting('>')") #os.path.join() это функция из модуля помогает соединять папки и имена файлов(чтобы не печатать путь воечную)
f2.close()

f3 = open(os.path.join(path,"file3.txt"), "x") #w - создает новый файл, если он есть, но стирает все старое и записывает новое 
f3.write("Still nothing (->-)")
f3.close()

print("все окк")'''