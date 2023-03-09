#Write a Python program to copy the contents of a file to another file
import os 

init_file = open(r'C:\pp2\week7\dir_and_files\demofile.txt', 'rt')

init_read = init_file.read()

final_file = open(r'C:\pp2\week7\dir_and_files\write.txt', 'wt')

final_file.write(init_read)