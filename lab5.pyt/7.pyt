import re
string = "almab,Aazhymukab anzhab. Arsen, .Beibaryb. .azim .Aresiib Balzhan, Ak,.niet .aashinb"
pattern = r"[ ,.]"
x = re.sub(pattern, ':', string)
print(x)