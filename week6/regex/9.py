#Write a Python program to insert spaces between words starting with capital letters.
import re

text = "WriteAPythonProgramToInsertSpacesBetweenWordsStartingWithCapitalLetters"

pattern = r"[A-Z][a-z]*"

words = re.findall(pattern, text)

answer = ""

for i in range(len(words)):
    if i == 0:
        answer += words[i]
    else: 
        answer += " " + words[i]

print(answer)