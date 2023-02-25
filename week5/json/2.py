import json

file = open('data.json', 'r')

data = json.load(file)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
""")


imdata = data["imdata"]

for i in imdata:
    l1PhysIf = i["l1PhysIf"]
    attributes = l1PhysIf["attributes"]
    if attributes["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/33]" or attributes["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/34]" or attributes["dn"] == "topology/pod-1/node-201/sys/phys-[eth1/35]":
        print(attributes["dn"], "                            ", attributes["speed"], "  ", attributes["mtu"])