file = open('input.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]

fpairs = {'{': '}', '[': ']', '(': ')', '<': '>'}
rpairs = { v: k for k, v in fpairs.items()}
score_list = {')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137}

stack = []
scores = []
for l in lines:
    for c in l:
        if c in fpairs.keys():
            stack.append(c)
            continue

        if len(stack) == 0:
            scores.append(score_list[c])
            break

        f = stack.pop()
        if fpairs[f] != c:
            scores.append(score_list[c])
            break

print(sum(scores))
