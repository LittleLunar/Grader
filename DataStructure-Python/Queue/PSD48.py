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


inp = input("Enter Input : ").split(',')

q_en = Queue()

q_es = Queue()

for i in inp:
    if i.startswith('EN'):
        q_en.enQueue(i.split(' ')[1])

    elif i.startswith('ES'):
        q_es.enQueue(i.split(' ')[1])

    elif i.startswith('D'):
        if not q_es.isEmpty():
            print(q_es.deQueue())

        elif not q_en.isEmpty():
            print(q_en.deQueue())

        else:
            print('Empty')
