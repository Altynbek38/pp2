#Implement a generator that returns all numbers from (n) down to 0.
def numbers(n):
    while n >= 0:
        yield n
        n = n - 1

n = int(input())

for i in numbers(n):
    print(i)