import datetime

last_activity_time = str(input('Enter a date in YYYY-MM-DD hh:mm:ss format: '))
date = datetime.datetime.strptime(last_activity_time, "%Y-%m-%d %H:%M:%S+%f")

try:
    last_time = datetime.datetime(date.year, date.month, date.day, date.hour, date.minute, date.second,date.microsecond)
    current_time = datetime.datetime.utcnow()
    diff = (current_time - last_time).total_seconds()

    if (0 < diff) and (diff < 60):
        print("Just Now")
    elif (60 < diff) and (diff < (60 * 60)):
        a = int(diff / 60)
        print(f"{a} mintues now")
    elif (diff > (60 * 60)) and (diff < (60 * 60 * 24)):
        a = int(diff / 3600)
        print(f"{a} hours ago")
    elif diff > (60 * 60 * 24) and (diff < (60 * 60 * 24 * 30)):
        a = int(diff / (60 * 60 * 24))
        print(f"{a} days ago")
    elif (diff > (60 * 60 * 24 * 30)) and (diff < (60 * 60 * 24 * 30 * 12)):
        a = int(diff / (60 * 60 * 24 * 28))
        print(f"{a} months ago")
    else:
        a = int(diff / (60 * 60 * 24 * 30 * 12))
        print(f"{a} years ago")

except:
    print("Invaild Input")