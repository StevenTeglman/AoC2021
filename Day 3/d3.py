file = open('Day 2\input3.txt', 'r')
lines = file.readlines()

directions = []
print("START HERE")
print(" |")
print(" .")

for l in lines:
    l = l.split(" ")
    directions.append((l[0], int(l[1])))
horizontal = 0
depth = 0
aim = 0

for d in directions:
    if d[0] == "forward":
        horizontal += d[1]
        depth += d[1] * aim
    elif d[0] == "up":
        aim -= d[1]
    elif d[0] == "down":
        aim += d[1]
    
result = horizontal * depth

print(result)