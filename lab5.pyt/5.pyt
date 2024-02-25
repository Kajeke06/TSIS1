import re
string = input()
matches = re.findall(r'a\w*b', string)
print("")
for match in matches:
    print(match)