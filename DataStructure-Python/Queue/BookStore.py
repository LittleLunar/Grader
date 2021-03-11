class Queue:
    def __init__(self, li=None):
        if li == None:
            self.queue = []
        else:
            self.queue = li

    def enQueue(self, i):
        self.queue.append(i)

    def deQueue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def getCopy(self):
        return self.queue.copy()


inp = input('Enter Input : ').split('/')

q = Queue(inp[0].split(' '))

for i in inp[1].split(','):
    if i.startswith('E'):
        q.enQueue(i.split(' ')[1])

    elif i.startswith('D'):
        q.deQueue()

if set(q.getCopy()) != q.size():
    print('Duplicate')

else:
    print('NO Duplicate')
