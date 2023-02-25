#Write a Python program to print yesterday, today, tomorrow.
import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)

print(yesterday, yesterday.strftime("%A"))
print(today, today.strftime("%A"))
print(tomorrow, tomorrow.strftime("%A"))