#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

text = ["abb", "baba", "bbba", "aaab", "aabb", "abbb", "abbbb"]

pattern1 = r"a[b]{2}"
pattern2 = r"a[b]{3}"

for i in text:
    if re.search(pattern1, i) or re.search(pattern2, i):
        print(i)

#or

text = "abb baba bbba aaab aabb abbb abbbb"

x = re.findall(pattern1, text) + re.findall(pattern2, text)

print(x)