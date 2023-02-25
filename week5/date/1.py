#Write a Python program to subtract five days from current date.
import datetime

time = datetime.datetime.now()

five_days_ago = time - datetime.timedelta(days = 5)

print(five_days_ago)