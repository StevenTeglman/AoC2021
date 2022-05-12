file = open('input.txt', 'r')
lines = file.readlines()
lines = [x.strip() for x in lines]

fpairs = {'{': '}', '[': ']', '(': ')', '<': '>'}
rpairs = { v: k for k, v in fpairs.items()}
score_list = {')': 1,
            ']': 2,
            '}': 3,
            '>': 4}

stack = []
del_indexes = []
for i, l in enumerate(lines[:]):
    for c in l:
        if c in fpairs.keys():
            stack.append(c)
            continue

        if len(stack) == 0:
            del_indexes.append(i)
            break

        f = stack.pop()
        if fpairs[f] != c:
            del_indexes.append(i)
            break

lines = [v for i, v in enumerate(lines) if i not in del_indexes]


scores = []
for i, l in enumerate(lines[:]):
    stack = []
    for c in l:
        if c in fpairs.keys():
            stack.append(c)
            continue

        f = stack.pop()
        if fpairs[f] != c:
            print("Something's wrong I can feel it")
            continue
    cur_score = 0
    for t in stack:
        cur_score = cur_score * 5
        cur_score += score_list[fpairs[t]]
    scores.append(cur_score)

scores.sort()
m_index = int((len(scores)-1)/2)
print(scores[m_index+1])
