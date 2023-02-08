s = str(input())
l =[]

def sentence_reversed(s):
    h = ""
    for i in range(len(s)):
        if s[i] == " ":
            l.append(h)
            h = ""
        else:
            h += s[i]
    l.append(h)
    l.reverse()

sentence_reversed(s)

print(*l)