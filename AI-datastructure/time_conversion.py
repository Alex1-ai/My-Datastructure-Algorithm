def timeConversion(s):
    # Write your code here
    if "PM" in s:
        time = s.split(":")
        if int(time[0])< 12:
            time[0] = str(int(time[0])+12)
        time[2] = time[2].replace("PM", "")
    elif "AM" in s:
        time = s.split(":")
        if int(time[0]) == 12:
            time[0] = "00"
        time[2] = time[2].replace("AM","")

    return ":".join(time)


print(timeConversion("12:40:22AM"))
