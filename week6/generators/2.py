#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(n):
    m = 0
    while m <= n:
        yield m
        m = m + 2
    
n = int(input())

even_num = even_generator(n)

print(*even_num, sep = ", ")