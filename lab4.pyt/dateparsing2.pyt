import datetime
x = datetime.datetime.now()
print("Yesterday:", x-datetime.timedelta(days=1))
print("Today:", x)
print("tommorraw:", x+datetime.timedelta(days=1))