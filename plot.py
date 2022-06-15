import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import json

# make up some data

def get_time_value(date_str):
    h, m, s = date_str.split(":")
    value = int(h)
    value += (int(m) + int(s) / 60) / 60

    return value
date_file = "2022-06-15"

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
    #i += 1
    #if i > 5:
     #   break



print(times)
print(T_5D)


# plot
plt.plot(times, T_2, label="Terminal 2")
plt.plot(times, T_5F, label="Terminal 5F")
plt.plot(times, T_5D, label="Terminal 5D")

# beautify the x-labels
#plt.gca().xaxis.set_minor_locator(dates.MinuteLocator(interval=30))
#plt.xticks(rotation=90, fontweight='light',  fontsize='x-small',)



plt.xlabel("Time")

plt.ylabel("wait time")

plt.legend()
plt.show()


