# que : Print current date and time. Based on the time print good morning, afternoon, evening and good night

from datetime import datetime, timedelta
# today = datetime.now().strftime("%H:%M:%S")
# strftime("%H:%M:%S") it will give full time
today1 = datetime.now().hour

if 5 < today1 < 12:
    print("good morning")
elif 12 < today1 < 15:
    print("good afternoon")
elif 15 < today1 < 22:
    print("good night")
