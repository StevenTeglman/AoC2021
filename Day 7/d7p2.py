from collections import defaultdict
import statistics, math

file = open('input7.txt', 'r')
lines = file.readline()
lines = lines.split(",")
crabs = [int(x) for x in lines]


minp = min(crabs)
maxp = max(crabs)

fuel_levels = defaultdict(int)
print(f"Min: {minp}, Max: {maxp}")
for p in range(minp, maxp):
    print(f"Current Position: {p}")
    pos_fuel = 0
    for c in crabs[:]:
        crab_fuel = 0
        for movement in range(abs(c-p)+1):
            crab_fuel += movement

        pos_fuel += crab_fuel

    fuel_levels[p] = pos_fuel

for key, value in fuel_levels.items():
    print(f"Current Position: {key}\nTotal Fuel: {value}\n\n")

print(f"Minimum Value: {min(fuel_levels.values())}")