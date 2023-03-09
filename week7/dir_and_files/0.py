import os

print(os.name)

print(os.environ)

print(os.getenv('TMP'))

print(os.getcwd())

print(os.path.exists('C:\pp2\week7\dir_and_files\demofile.txt'))

print(os.path.isfile('C:\pp2\week7\dir_and_files\demofile.txt'))

print(os.path.isdir('C:\pp2\week7\dir_and_files\demofile.txt'))

# os.mkdir(r'C:\pp2\week8')

# os.makedirs(r'C:\pp2\folder\first\second\third')

# os.remove(r'C:\pp2\test.txt')

# os.rmdir(r'C:\pp2\week8')

# os.removedirs(r'C:\pp2\folder\first\second\third')

os.startfile(r'C:\Users\User\Desktop\Sublime Text.lnk')

print(os.path.basename('C:\pp2\week7\dir_and_files\demofile.txt'))

print(os.path.dirname('C:\pp2\week7\dir_and_files\demofile.txt'))

print(os.path.getsize('C:\pp2\week7\dir_and_files\demofile.txt'))

#os.rename(r'C:\pp2\week8', r'C:\pp2\w8')

#os.renames(r'C:\pp2\folder\first\second', r'C:\pp2\catalog\one\two')

print(os.listdir(r'C:\pp2'))

# for root, directories, files in os.walk(r"C:\pp2"):
#     print(root)
#     for directory in directories:
#         print(directory)
#     for file in files:
#         print(file)

print(os.stat(r'C:\pp2\week7\dir_and_files\demofile.txt'))

print(os.path.split('C:\pp2\week7\dir_and_files\demofile.txt'))

print(os.path.join(r'C:\pp2\week7\dir_and_files', r'demofile.txt'))