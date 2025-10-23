import os

path = r"C:\Users\user\Documents\PP2\labs\lab6\a_z"

for i in range(65, 91):
    letter = chr(i)
    file_path = os.path.join(path, f"{letter}.txt")
    with open(file_path, 'w') as f:
        f.write(letter)

for i in range(65, 91):
    letter = chr(i)
    file_path = os.path.join(path, f"{letter}.txt")
    with open(file_path, 'r') as f:
        print(f.read())