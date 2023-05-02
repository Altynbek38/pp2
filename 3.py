import re

txt = "hello"

res = 'HELLO'

pattern = r"[a-z]*"

ans = re.findall(pattern, txt)

ans[0] = ans[0].upper()

print(ans[0])

file = open("ans.txt", 'wt')

data = file.write(ans[0])