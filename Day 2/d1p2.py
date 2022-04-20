file = open('input1.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]
lines = [int(x) for x in lines]

num_greater = 0
i = 1

while i+2 != len(lines):
    a = lines[i]
    b = lines[i+1]
    c = lines[i+2]
    sum1 = a+b+c

    j = i-1
    a = lines[j]
    b = lines[j + 1]
    c = lines[j + 2]
    sum2 = a+b+c

    print(f"i: {i}\n j: {j}\n sum1: {sum1}\n sum2: {sum2}")
    if sum1 > sum2:
        num_greater += 1

    i += 1
print(num_greater)