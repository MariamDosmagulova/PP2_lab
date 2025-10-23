import os 

path = r"C:\Users\user\Documents\PP2\labs\lab6\file3.txt"
list = ['banana', 'shadiyar', 'water']

with open(path, 'w') as f:
    for i in list:
        f.write(i + "\n")

with open(path, 'r') as f:
    print(f.read())
        
print("spisok uspeshno sohranen")