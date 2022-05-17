#Temperature graphs from PCC.

import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/2193109.csv"
# filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')


    place_name = ''    
    # Get dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        if not place_name:
            place_name = row[name_index]
            print(place_name)

        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = float(row[high_index])
            low = float(row[low_index])
        except ValueError:
            print(f'Missing data for {current_date}.')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# print(highs)
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha = .5, linewidth = .5)
ax.plot(dates, lows, c = 'blue', alpha = .5, linewidth = .5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = .1)

# Format plot.
plt.title(f"{place_name} \nhigh and low temperatures - 2018", fontsize = 20)
plt.xlabel('Dates', fontsize = 16)
fig.autofmt_xdate(bottom = .2, rotation = 45, ha = 'center')
plt.ylabel("Temperature (C)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 10, pad = 10, length = 10)
plt.ylim(0, 33)

plt.show()
