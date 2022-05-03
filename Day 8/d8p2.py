file = open('input.txt', 'r')
lines = file.readlines()

result = 0

for line in lines:
    start, end = line.split(" | ")
    end_parts = [''.join(sorted(s)) for s in end.split()]
    digits = [''.join(sorted(s)) for s in start.split()]

    num_to_s = {}
    num_to_s[1], = (s for s in digits if len(s) == 2)
    num_to_s[4], = (s for s in digits if len(s) == 4)
    num_to_s[7], = (s for s in digits if len(s) == 3)
    num_to_s[8], = (s for s in digits if len(s) == 7)
    len6 = {s for s in digits if len(s) == 6}

    num_to_s[6], = (s for s in len6 if len(set(s) & set(num_to_s[1])) == 1)
    num_to_s[9], = (s for s in len6 if len(set(s) & set(num_to_s[4])) == 4)
    num_to_s[0], = len6 - {num_to_s[6], num_to_s[9]}

    len5 = {s for s in digits if len(s) == 5}
    num_to_s[5], = (s for s in len5 if len(set(s) & set(num_to_s[6])) == 5)
    num_to_s[2], = (s for s in len5 if len(set(s) & set(num_to_s[9])) == 4)
    num_to_s[3], = len5 - {num_to_s[5], num_to_s[2]}

    sipher = {v: k for k, v in num_to_s.items()}
    output = ""
    for p in end_parts:
        num = sipher[p]
        output += str(num)
    result += int(output)
print(result)





