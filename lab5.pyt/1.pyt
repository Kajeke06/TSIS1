import re
given = r"a{1}b*"
ab = input()
sol = re.findall(given, ab)
if sol:
    print(sol)
else:
    print("error")