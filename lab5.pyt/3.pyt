import re
string = "almas_krasavchik mini_bmv Mercedes_En kushti"
pattern = r"([a-z]+_[a-z])"
x = re.findall(pattern, string)
print(x)