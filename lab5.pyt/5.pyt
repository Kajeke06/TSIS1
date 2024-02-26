import re
string = input()
x = r'(a\w*b)'
matches = re.findall(x, string)
for match in matches:
    print(match)