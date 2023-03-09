#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def directories(path):
    directory = []
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            directory.append(os.path.join(path, i))
    return directory

def files(path):
    file = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            file.append(os.path.join(path, i))
    return file

def both(path):
    all = []
    for i in os.listdir(path):
        all.append(os.path.join(path, i))
    return all

path = r'C:\pp2\week7'

print(directories(path))
print(files(path))
print(both(path))