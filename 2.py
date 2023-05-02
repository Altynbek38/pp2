n = int(input())

k = 0
print(n)
n = str(n)

while len(n) < 32:
    n = '0' + n
print(n)
ans = 0
for i in n:
    if i == '1':
        ans += pow(2, k)
    k += 1

print(ans)