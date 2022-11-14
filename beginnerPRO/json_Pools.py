import json
from datetime import datetime

w = 0
l = 0
result = []
with open("./beginnerPRO/pools.json", "r", encoding="utf8") as f:
    data = json.load(f)

    for n in data:
        width = n["DimensionsSummer"]["Width"]
        lenght = n["DimensionsSummer"]["Length"]
        list_times_monday = n["WorkingHoursSummer"]["Понедельник"].split("-")
        start_time_mon = datetime.strptime(list_times_monday[0], "%H:%M")
        end_time_mon = datetime.strptime(list_times_monday[1], "%H:%M")
        if start_time_mon.hour == 10 and start_time_mon.minute == 00:
            if end_time_mon.hour - start_time_mon.hour >= 2:
                if width > w or lenght > l:
                    w = width
                    l = lenght
                    result.append([l, w, n["Address"]])
                    print(n["ObjectName"])
print(
    f"""{result[-1][0]}x{result[-1][1]}
{result[-1][2]}"""
)
