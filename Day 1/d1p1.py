file = open('input1.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]
lines = [int(x) for x in lines]

num_greater = 0
i = 1

for l in lines:
    if len(lines) == i:
        break

    if l < lines[i]:
        num_greater += 1

    i += 1

print(num_greater)