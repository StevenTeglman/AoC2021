import collections
from typing import Generator
import math

file = open('input.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]

chart = collections.defaultdict(lambda: 9)


def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1


for y, line in enumerate(lines):
    for x, c in enumerate(line):
        chart[(x, y)] = int(c)

total_risk = 0
minimas = []

for (x, y), n in chart.items():
    if all(chart.get(pt, 9) > n for pt in adjacent(x, y)):
        minimas.append((x,y))
        total_risk += n + 1

basins = []
for x,y in minimas:
    seen = set()
    todo = [(x, y)]

    while todo:
        x, y = todo.pop()
        seen.add((x, y))
        for pt in adjacent(x,y):
            if pt not in seen and chart[pt] != 9:
                todo.append(pt)

    basins.append(len(seen))

basins.sort()
result = math.prod(basins[-3:])
print(result)

