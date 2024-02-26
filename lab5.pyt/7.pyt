import re
string = "kka_nfetjng_jfietgm_nfirwknm_k"
x = re.sub(r'_\w', lambda match: match.group(0).replace('_', '').upper(),string)
print(x)