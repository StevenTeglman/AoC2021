file = open('input7.txt', 'r')
lines = file.readline()
lines = lines.split(",")
lines = [int(x) for x in lines]

import statistics, math


avg = statistics.median(lines)
avg = int(math.ceil(avg))
print(avg)

fuel = 0

for i in lines:
    fuel_spent = abs(i - avg)
    fuel += fuel_spent

print(fuel)