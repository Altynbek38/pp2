def histogram(num):
    l = []
    for i in num:
        for j in range(i):
            l.append("*")
        print("".join(l))
        l.clear()




histogram([4, 9, 7])