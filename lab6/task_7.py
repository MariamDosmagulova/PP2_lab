path_1 = r"C:\Users\user\Documents\PP2\labs\lab6\file3.txt"
path_2 = r"C:\Users\user\Documents\PP2\labs\lab6\file1.txt"
with open(path_1,'r') as f:
    file = f.read()
with open(path_2, 'w') as f:
    copy = f.write(file)
with open(path_2, 'r') as f:
    print(f.read())
with open(path_1, 'r') as f:
    print(f.read())