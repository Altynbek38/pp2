import json

with open('C:\pp2\week5\json\data.json') as f:
    data = json.load(f)

    print("Interface Status")
    print("================================================================================")
    print("DN                                                 Description           Speed    MTU  ")
    print("-------------------------------------------------- --------------------  ------  ------")

    imdata = data["imdata"]

    for i in imdata:
        l1PhysIf = i["l1PhysIf"]
        attributes = l1PhysIf["attributes"]
        dn = attributes["dn"]
        speed = attributes["speed"]
        mtu = attributes["mtu"]
        if len(dn) == 42:
            print(dn + "                             " , speed , " ", mtu)
        elif len(dn) == 41:
            print(dn + "                              " , speed , " ", mtu)