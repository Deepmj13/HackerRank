print("Format : HH:MM:SSAM/PM")
time = input("Enter the time")

def timeconversion(time):

    period = time[-2:]
    hour = time[0:2]
    minutes = time[3:5]
    seconds = time[6:8]

    if period == "AM":
        hour = "00"

    if period == "PM":
        if hour != "12":
            hour = str(int(hour)+12)

    print(str(hour+':'+minutes+':'+seconds))

timeconversion(time)
