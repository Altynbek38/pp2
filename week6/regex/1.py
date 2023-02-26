#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

text = ["abb", "bab", "bbb", "aaa", "aab"]


pattern = r"a[b]*"

for i in text:
    if re.search(pattern, i):
        print(i)
