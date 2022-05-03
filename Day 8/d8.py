file = open('input.txt', 'r')
lines = file.readlines()


num_occur = 0

lines = [x.split(" | ")[1].strip() for x in lines]
lines = [x.split(" ") for x in lines]
for l in lines:
    for d in l:
        if len(d) in (2, 4, 3, 7):
            num_occur += 1

print(f"There are {num_occur} instances of (2, 3, 4, 7)")