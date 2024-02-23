from datetime import datetime
#1
"""today = datetime.now()
day = today - timedelta(days=5)

print(day)
#2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday, today, tomorrow)

#3
x = datetime.now().replace(microsecond=0)
print(x)
"""
#4
def date_difference(date1, date2):

    timestamp1 = date1.timestamp()
    timestamp2 = date2.timestamp()

    difference = abs(timestamp1 - timestamp2)

    return difference



date1 = datetime(2024, 2, 20, 17, 21, 38)
date2 = datetime(2022, 2, 19, 17, 21, 36)

difference = date_difference(date1, date2)

print(difference)































