import csv
from matplotlib import pyplot as plt

filename = 'Data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    highs = []
    for row in reader:

        highs.append(row[1])

    print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

plt.title("Premier Leauge Match Dates", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Dates (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
