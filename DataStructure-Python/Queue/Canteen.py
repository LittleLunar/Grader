class Queue:
    def __init__(self, li=None):
        if li == None:
            self.queue = []
        else:
            self.queue = list(li)

    def enQueue(self, i):
        self.queue.append(i)

    def deQueue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def getCopy(self):
        return self.queue.copy()

    def insert(self, i, j):
        self.queue.insert(i, j)

    def getItem(self):
        return self.queue


inp = input("Enter Input : ").split('/')

s = inp[0].split(',').copy()
prio = {}

q = Queue()

for i in inp[1].split(','):

    if i.startswith('E'):
        for k, j in enumerate(s):
            if i.split()[1] == j.split()[1]:
                if j.split()[0] not in prio.keys():
                    q.enQueue(j)
                    prio[j.split()[0]] = 1
                else:
                    x = list(prio).index(j.split()[0])
                    wheretoinsert = 0
                    while x != -1:
                        wheretoinsert += prio.get(list(prio)[x])
                        x -= 1
                    q.insert(wheretoinsert, j)
                    prio[j.split()[0]] += 1

    elif i.startswith('D'):
        if not q.isEmpty():
            print(q.peek().split()[1])
            temp = q.deQueue().split()[0]
            prio[temp] -= 1
            if prio[temp] == 0:
                prio.pop(temp)
        else:
            print('Empty')
