import threading, queue

file = open('input6.txt', 'r')
lines = file.readline()
lines = lines.split(",")

school = []


class feesh:
    global school
    def __init__(self, age):
        self.age = age

    def get_older(self):
        self.age -= 1
        if self.age < 0:
            self.age = 6
            new_feesh = feesh(8)
            school.append(new_feesh)

# build school
for a in lines:
    new_feesh = feesh(int(a))
    school.append(new_feesh)


def age_feesh(qq):
    while True:
        f = qq.get()
        f.get_older()
        qq.task_done()


q = queue.Queue()
j = 0
tp = []
while j < 4:
    t = threading.Thread(target=age_feesh, args=[q])
    t.daemon = True
    tp.append(t)
    j += 1

for t in tp:
    t.start()

i = 1
while i < 257:

    for f in school[:]:
        q.put(f)

    print("all feesh in queue")

    q.join()

    print("Queue joined")

    print("Day {}, FEESH: {}".format(i,len(school)))
    i += 1
