from typing import Generator

file = open('input.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]

coords = {}
for y, line in enumerate(lines):
    for x, value in enumerate(line):
        coords[x, y] = int(value)


def adjacent(x:int, y:int) -> Generator[tuple[int,int], None, None]:
    for x_d in (-1, 0, 1):
        for y_d in (-1, 0, 1):
            if x_d == y_d == 0:
                continue
            yield x + x_d, y + y_d

flashes = 0
for _ in range(100):
    todo = []
    for k, v in coords.items():
        coords[k] += 1
        if coords[k] > 9:
            todo.append(k)

    while todo:
        d_k = todo.pop()
        if coords[d_k] == 0:
            continue

        coords[d_k] = 0
        flashes += 1

        for surround in adjacent(*d_k):
            if surround in coords and coords[surround] != 0:
                coords[surround] += 1

                if coords[surround] > 9:
                    todo.append(surround)



print(f"Flashes: {flashes}")


