import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("c:/Users/User/Desktop/kajy.python/lab4.pyt/sample-data.json", "r") as file:
    data = json.load(file)
    for item in data['imdata']:
        print (f"{item['l1PhysIf']['attributes']['dn']}{item['l1PhysIf']['attributes']['speed']}  {item['l1PhysIf']['attributes']['mtu']}")