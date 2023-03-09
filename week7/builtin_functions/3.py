#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

s = str(input())

r1 = reversed(s)

s1 = ""
for i in r1:
    s1 += i

if s == s1:
    print("Is Palindrome")
else:
    print("Is not Palindrome")