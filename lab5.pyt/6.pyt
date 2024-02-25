import re
string = input()
x = re.sub(r'[ ,.]', ':', string)
print(x)