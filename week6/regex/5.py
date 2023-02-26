#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

text = ["abcdefg", "abcdefb", "bcdfa", "alongb"]

pattern = r"^[a].*[b]$"

for i in text:
    if re.search(pattern, i):
        print(i)
