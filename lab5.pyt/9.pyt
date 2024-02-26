import re
capitals = "OttawaKazakhstanRussiaChinaUsaTurkey"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', capitals)
print(x)