
#Task 2

import os

path = r"C:\Users\user\Documents\PP2\labs\lab6"

print("Path exist", os.path.exists(path))
print("Redable:", os.access(path, os.R_OK))
print("Writsble:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

