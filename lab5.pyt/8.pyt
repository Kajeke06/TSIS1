import re
f = r'[A-Z][a-z]*'
capitals = "TemaOmirBilimPekinAtlas"
x = re.findall(f, capitals)
print(x)