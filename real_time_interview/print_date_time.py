from datetime import datetime, timedelta

today = datetime.now()
print(today)

add_time = timedelta(minutes=10)
print(today + add_time)