import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import json

open_times = {
    "Terminal 2": {
        'Monday': ["04:00:00", "20:30:00"],
        'Tuesday': ["04:00:00", "20:30:00"],
        'Wednesday': ["04:00:00", "20:30:00"],
        'Thursday': ["04:00:00", "20:30:00"],
        'Friday': ["04:00:00", "20:30:00"],
        'Saturday': ["04:00:00", "20:30:00"],
        'Sunday': ["04:00:00", "20:30:00"]
    },
    "Terminal 5F": {
        'Monday': ["03:30:00", "22:35:00"],
        'Tuesday': ["03:00:00", "01:15:00"],
        'Wednesday': ["03:30:00", "23:30:00"],
        'Thursday': ["02:50:00", "00:15:00"],
        'Friday': ["02:45:00", "23:15:00"],
        'Saturday': ["01:15:00", "00:15:00"],
        'Sunday': ["01:15:00", "23:55:00"]
    },

    "Terminal 5D": {
        'Monday': ["03:30:00", "20:30:00"],
        'Tuesday': ["03:30:00", "20:30:00"],
        'Wednesday': ["02:45:00", "20:30:00"],
        'Thursday': ["03:30:00", "20:30:00"],
        'Friday': ["03:30:00", "20:30:00"],
        'Saturday': ["03:30:00", "20:30:00"],
        'Sunday': ["03:30:00", "20:30:00"]
    }
}


# make up some data

def get_week_day(date_str):
    return datetime.date.fromisoformat(date_str).strftime("%A")


def get_opening_times(weekday, terminal_name):
    return open_times[terminal_name][weekday]


def get_time_value(date_str):
    h, m, s = date_str.split(":")
    value = int(h)
    value += (int(m) + int(s) / 60) / 60

    return value


date_file = "2022-06-16"

json_data = {}
with open("wait_data/" + date_file + ".json") as json_file:
    json_data = json.load(json_file)

times = []
T_2 = []
T_5F = []
T_5D = []

i = 0
for key, value in json_data.items():
    times.append(get_time_value(key))
    T_2.append(value["Terminal 2"])
    T_5D.append(value["Terminal 5D"])
    T_5F.append(value["Terminal 5F"])
    # i += 1
    # if i > 5:
    #   break

#print(times)
#print(T_5D)

# plot
plt.plot(times, T_2, label="Terminal 2", color="r")
plt.plot(times, T_5F, label="Terminal 5F", color="g")
plt.plot(times, T_5D, label="Terminal 5D", color="b")

# beautify the x-labels
# plt.gca().xaxis.set_minor_locator(dates.MinuteLocator(interval=30))


x_t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
x_l = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00",
     "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]

plt.xticks(x_t, x_l)
plt.xticks(rotation=45)

a = 0.25
r = 45

week_day = get_week_day(date_file)

open_time, close_time = get_opening_times(week_day, "Terminal 2")
plt.axvline(get_time_value(open_time), color="r", linestyle='--', alpha=a)
plt.text(get_time_value(open_time), 48,'Terminal 2 Opens',rotation=r)
plt.axvline(get_time_value(close_time), color="r", linestyle='--', alpha=a)
plt.text(get_time_value(close_time)-0.5, 48,'Terminal 2 Closes',rotation=r)

open_time, close_time = get_opening_times(week_day, "Terminal 5F")
plt.axvline(get_time_value(open_time), color="g", linestyle='--', alpha=a)
plt.text(get_time_value(open_time), 48,'Terminal 5F Opens',rotation=r)
plt.axvline(get_time_value(close_time), color="g", linestyle='--', alpha=a)
plt.text(get_time_value(close_time), 48,'Terminal 5F Closes',rotation=r)

open_time, close_time = get_opening_times(week_day, "Terminal 5D")
plt.axvline(get_time_value(open_time), color="b", linestyle='--', alpha=a)
plt.text(get_time_value(open_time), 48,'Terminal 5D Opens',rotation=r)
plt.axvline(get_time_value(close_time)+0.05, color="b", linestyle='--', alpha=a)
plt.text(get_time_value(close_time)+0.25, 48,'Terminal 5D Closes',rotation=r)


plt.xlabel("Time (h)")
plt.ylabel("Queue time (min)")

plt.legend()
plt.show()
