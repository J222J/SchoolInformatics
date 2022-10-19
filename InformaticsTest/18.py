import time

gmt = eval(input("Enter GMT value : "))

t = int(time.time())

seconds = t%60
minutes = t//60%60
hours = (t//60//60 + gmt) % 24

print("Current time is ", hours, minutes, seconds, sep=":")

