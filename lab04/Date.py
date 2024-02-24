#1
import datetime
x = datetime.datetime.now()
print("Day will be:", x - datetime.timedelta(days=5))

#2
b = datetime.datetime.now()
a = b - datetime.timedelta(days=1)
c = b + datetime.timedelta(days=1)
print("Yesterday:", a)
print("Today:", b)
print("Tomorrow:", c)

#3
_date = datetime.datetime.now()
print("Without microseconds:", _date.replace(microsecond=0))

#4
from datetime import datetime
def date_difference_in_seconds(date1, date2):
    datetime1 = datetime.strptime(date1, "%Y-%m-%d")
    datetime2 = datetime.strptime(date2, "%Y-%m-%d")
    difference = abs((datetime2 - datetime1).total_seconds())
    
    return difference
date1 = "2024-02-19"
date2 = "2024-02-21"
difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference in seconds:", difference_seconds)