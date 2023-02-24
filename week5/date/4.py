import datetime

x = datetime.datetime.now()
y = datetime.datetime(2020, 5, 17, 22, 36, 45)

z = x - y

print(z.total_seconds())