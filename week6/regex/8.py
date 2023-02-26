#Write a Python program to split a string at uppercase letters.
import re

text = "WriteAPythonProgramToSplitAStringAtUppercaseLetters"

pattern = r"[A-Z][a-z]*"

words = re.findall(pattern, text)

answer = ""

for i in range(len(words)):
    if i == 0:
        answer += words[i]
    else:
        answer += " " + words[i]

print(answer)
print(words)