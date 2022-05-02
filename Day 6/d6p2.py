from collections import defaultdict
import numpy as np

file = open('input6.txt', 'r')
lines = file.readline()
lines = lines.split(",")
un = np.unique(lines).tolist()
school = {}

for u in un:
    school[u] = lines.count(u)

def age(old_school):
    new_school = defaultdict(int)
    for key, value in old_school.items():
        nkey = int(key) -1
        if nkey < 0:
            new_school[8] = value
            nkey = 6
        new_school[nkey] = int(new_school[nkey]) + value

    return new_school

days = 256

print(f"Day: 0 \n Feesh: {sum(school.values())}")
for d in range(256):
    school = age(school)
    print(f"Day: {d+1} \n Feesh: {sum(school.values())}")

