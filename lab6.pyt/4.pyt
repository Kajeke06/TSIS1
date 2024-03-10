import os
path = input("Enter path: ")
with open (path, 'r') as file:
    count_lines = len(file.readlines())
    print("lines: ", count_lines)
"""
C:/Users/User/Desktop/kajy.python/lab6.pyt/3.pyt
"""