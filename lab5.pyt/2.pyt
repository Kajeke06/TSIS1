import re
string = "semle a ab abb aaabbb abababa"
x = re.findall("a{1}b{2,3}", string)
print(x)