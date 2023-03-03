#Write a Python program to convert a given camel case string to snake case.
import re

def camel_to_snake(camel, snake):
    pattern = r"[A-Z]?[a-z]*"
    words = re.findall(pattern, camel)
    for i in range(len(words)):
        if i == 0:
            snake += words[i].lower()
        elif i != len(words) - 1:
            snake += "_" + words[i].lower()
    return snake

snake = ""
camel = "writeAPythonProgramToConvertAGivenCamelCaseStringToSnakeCase"

print(camel_to_snake(camel, snake))