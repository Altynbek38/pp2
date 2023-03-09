#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
s = "Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters"

s = str(input())

upper_num = 0
lower_num = 0
for i in s:
    if i.isupper():
        upper_num += 1
    elif i.islower():
        lower_num += 1

print("The number of upper case letters", upper_num)
print("The number of lower case letters", lower_num)