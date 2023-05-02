class Solution:
    def __init__(self, s):
        self.s = s
    def isValid(self, s: str) -> bool:
        chr = {'(': ')', '[': ']', '{': '}'}
        opp = []
        for i in s:
            if i in chr.keys():
                opp.append(chr[i])
            elif opp[-1] != i:
                return False
            elif opp[-1] == i:
                opp.pop()
        if len(opp) == 0:
            return True
        else: return False
             

s = str(input())

ans = Solution(s)

print(ans.isValid(s))