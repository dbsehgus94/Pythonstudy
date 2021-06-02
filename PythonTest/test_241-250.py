import time
import datetime
now = datetime.datetime.now()
print(now)
print(type(now))

for i in range(5, 0, -1):
    delta = datetime.timedelta(days=i)
    date = now - delta
    print(date)

print(now.strftime("%H:%M:%S"))

day = "2020-05-04"
a = datetime.datetime.strptime(day, "%Y-%m-%d")
print(a, type(a))

#while True:
#    now = datetime.datetime.now()
#    print(now)
    #time.sleep(1)

import os
ret = os.getcwd()
print(ret, type(ret))

#os.rename("C:/Users/Yun/Desktop/before.txt", "C:/Users/Yun/Desktop/after.txt")

import numpy
for i in numpy.arange(0.0, 5.0, 0.1):
    print(round(i, 1))
