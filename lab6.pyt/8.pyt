import os
path = input("Enter path for your file: ")
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File successfully deleted!")
else:
    print("File not found!")
    