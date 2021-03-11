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

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


inp = input('Enter Input : ').split(',')

q = Queue()

for i in inp:
    if i.startswith('E'):
        q.enQueue(i.split(' ')[1])
        print('Add {} index is {}'.format(i.split(' ')[1], q.size() - 1))

    elif i.startswith('D'):
        if q.size() > 0:
            print('Pop {} size in queue is {}'.format(q.deQueue(), q.size()))

        else:
            print(-1)

else:
    if not q.isEmpty():
        print(f'Number in Queue is :  {q.queue}')

    else:
        print('Empty')
