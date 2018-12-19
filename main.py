import csv
from matplotlib import pyplot as plt
x=[]
y=[]
filename = 'Data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    for row in reader:
        y.append(row[4])
        x.append(row[1])

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(y, c='red')

plt.title("Premier Leauge Match Dates", fontsize=24)
plt.xlabel('', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

