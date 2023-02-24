import json

with open('data.json') as f:
   data = json.load(f)


print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

imdata = data["imdata"]

for i in imdata:
    print(i["dn"] + "                              " + i["fecmode"] + "   " + i["mtu"])
