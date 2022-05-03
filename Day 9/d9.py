file = open('input.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]

chart = [[int(c) for c in l] for l in lines]

print(f"y levels: {len(chart)}")
print(f"x levels: {len(chart[0])}")

risk = 0
y = 0
while y < len(chart):
    x = 0
    print(f"[!] Current y level: {y}")
    while x < len(chart[0]):
        print(f"Current x level: {x}")
        l, r, u, d = False, False, False, False
        cur_pos = chart[y][x]
        if y != 0:
            if cur_pos < chart[y-1][x]:
                u = True
        else: u = True

        if y != len(chart)-1:
            if cur_pos < chart[y+1][x]:
                d = True
        else: d = True

        if x != 0:
            if cur_pos < chart[y][x-1]:
                l = True
        else: l = True

        if x != len(chart[0])-1:
            if cur_pos < chart[y][x+1]:
                r = True
        else: r = True

        if all([l, r, u, d]):
            risk += cur_pos+1

        x += 1

    y += 1

print(risk)