file = open('input5.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]
lines = [l.split(" -> ") for l in lines]
lines = [[i.split(",") for i in line] for line in lines]

chart = [["."]*1000 for i in range(1000)]

for vent in lines:
    if vent[0][0] != vent[1][0] and vent[0][1] != vent[1][1]:
        continue

    x1 = int(vent[0][0])
    y1 = int(vent[0][1])
    x2 = int(vent[1][0])
    y2 = int(vent[1][1])
    location = []

    if y1 == y2:
        if x1 < x2:
            location = [*range(x1, x2 + 1)]
        else:
            location = [*range(x2, x1 + 1)]
        for pos in location:
            if chart[y1][pos] == ".":
                chart[y1][pos] = "1"
            else:
                chart[y1][pos] = str(int(chart[y1][pos])+1)

    elif x1 == x2:
        if y1 < y2:
            location = [*range(y1, y2 + 1)]
        else:
            location = [*range(y2, y1 + 1)]
        for pos in location:
            if chart[pos][x1] == ".":
                chart[pos][x1] = "1"
            else:
                chart[pos][x1] = str(int(chart[pos][x1])+1)

num_pos = 0

for r in chart:
    print(''.join(r))

for r in chart:
    for c in r:
        if c != ".":
            if int(c) > 1:
                num_pos += 1

print(num_pos)

