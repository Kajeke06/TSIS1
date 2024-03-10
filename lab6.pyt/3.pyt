import os
def analyz_test(path):
    if not os.path.exists(path):
        print("path does not exist")
        return
    filename=os.path.basename(path)
    directory=os.path.dirname(path)
    print(filename)
    print(directory)
path=input()
analyz_test(path)
"""
import os.path as file

filename = input()

if file.exists(filename):
    print("File exists")
else:
    print("File does not exists")
    """
"""
C:/Users/User/Desktop/kajy.python/lab6.pyt/3.pyt
"""