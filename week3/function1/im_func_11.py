s = str(input())

def pallindrome(s):
    ok = True
    for i in range(len(s)):
        if(s[i] != s[-1 - i]):
            ok = False
            break
    return ok

print(pallindrome(s))