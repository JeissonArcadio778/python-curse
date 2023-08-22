def timeConversion(s):
    new_format = ""  # 12:45:54PM 07:05:45PM
    hours = ""
    if s[len(s) - 2] == "P":
        format_time = s[0:len(s) - 2]
        if s[0:2] != "12":
            format_time = s[2:len(s) - 2]
            hours = str(int(s[0:2]) + 12)
        new_format = hours + format_time
    else:
        new_format = s[0:len(s) - 2]

    print(new_format)

timeConversion("12:45:54PM")