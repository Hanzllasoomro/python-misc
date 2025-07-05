from datetime import datetime

now = datetime.now() # current date and time
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
print("day: ", day)
time = now.strftime("%H:%M:%S")
print("time: ", time)
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)

now.year
now.month
 
 #strptime() method creates a datetime object from a string.

date_string = "21 June, 2018"
type(date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
type(date_object)