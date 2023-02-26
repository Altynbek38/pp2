#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

text = "It's common to write commas in code the same way you would use them in a sentence, with no space before and a space after."

x = re.sub('\s', ':', text)
x = re.sub('[,]', ':', x)
x = re.sub('[.]', ':', x)
print(x)