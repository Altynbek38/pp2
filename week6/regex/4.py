#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

text = ["Name", "Surname", "age", "IIN", "num"]

pattern = r"[A-Z][a-z]+"

for i in text:
    if re.search(pattern, i):
        print(i)