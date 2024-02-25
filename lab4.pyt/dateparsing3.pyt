from datetime import datetime, timedelta
n = datetime.now()
timestamp = n.timestamp()
timestamp_without_microseconds = int(timestamp // 1000000)
n_without_microseconds = datetime.fromtimestamp(timestamp_without_microseconds)

print(n_without_microseconds)

"""
import datetime 
x = datetime.datetime.now()
x = x.replace(microsecond = 0)
print(x)
"""