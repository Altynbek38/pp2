numheads = 35
numlegs = 94

def solve(numheads, numlegs):
    for x in range(numheads):
        chicken = x
        rabbit = 35 - x
        if 2 * chicken + 4 * rabbit == numlegs:
            return chicken, rabbit

chicken, rabbit = solve(numheads, numlegs)

print(chicken, rabbit)