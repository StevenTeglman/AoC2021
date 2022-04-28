file = open('Day 3\input2.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]

length = len(lines[0])
oxy = ""
c02 = ""

olines = lines.copy()
clines = lines.copy()

for i in range(0,length):
    num0 = 0
    num1 = 0
    if len(olines) == 1:
        oxy = olines[0]
        print("One left, Oxy: {}".format(oxy))
    for l in olines:
        num = l[i]
        if num == "0":
            num0 += 1
        if num == "1":
            num1 += 1
    
    if num1 >= num0:
        cur_num = "1"
    else:
        cur_num = "0"

    olines = [l for l in olines if l[i] != cur_num]


for i in range(0,length):
    num0 = 0
    num1 = 0
    if len(clines) == 1:
        print("One left, Oxy: {}")
        c02 = clines[0]
    for l in clines:
        num = l[i]
        if num == "0":
            num0 += 1
        if num == "1":
            num1 += 1
    
    if num1 >= num0:
        cur_num = "0"
    else:
        cur_num = "1"

    clines = [l for l in clines if l[i] != cur_num]

print("Clines: {}\nOlines: {}".format(clines,olines))
if oxy == "":
    oxy = olines[0]
if c02 == "":
    c02 = clines[0]


dg = int(oxy, 2)
de = int(c02, 2)

print("c02: {}\noxy: {}".format(c02, oxy))
print("c02 Decimal: {}\noxy Decimal: {}".format(dg, de))
result = dg * de
print(result)