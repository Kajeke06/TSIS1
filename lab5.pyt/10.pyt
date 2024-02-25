import re
capitals = "CanberraBrasiliaOttawaBeijingParisBerlinNewdelhiJakartaRomeTokyoMexicoCityAmsterdamMoscowRiyadhSeoulAnkaraKievAbujaLagosLondon"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', capitals)
x = x.lower()
print(x)