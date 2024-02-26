import re
string = "Kazhymukan Almas Sanzhar Arsen Beibarys azim Aresiii Balzhan Akniet mashina"
pattern = r"([A-Z]{1}+[a-z]*)"
x = re.findall(pattern, string)
print(x)