#Write a Python program to drop microseconds from datetime.
import datetime

time = datetime.datetime.now()

time = time.replace(microsecond = 0)

print(time)