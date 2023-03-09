#Write a Python program to write a list to a file.
import os

path = r'C:\pp2\week7\dir_and_files\write.txt'

file = open(path, 'wt')

list = ["Write ", "a ", "Python ", "program ", "to ", "write ", "a ", "list ", "to ", "a ", "file."]

for i in list:
    file.write(i)