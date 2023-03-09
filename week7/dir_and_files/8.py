#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

if os.path.exists(r'C:\pp2\week7\2.txt'):
    os.remove(r'C:\pp2\week7\2.txt')
else:
    print("The file does not exist")