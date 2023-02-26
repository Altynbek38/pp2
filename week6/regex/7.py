#Write a python program to convert snake case string to camel case string.
import re

def snake_to_camel(snake, camel):
    pattern = r"_"
    to = re.split(pattern, snake)
    for i in range(len(to)):
        if i == 0:
            camel += to[i]
        else:
            camel += to[i].capitalize()
    return camel

camel = ""
snake = "write_a_python_program_to_convert_snake_case_string_to_camel_case_string."

print(snake_to_camel(snake, camel))