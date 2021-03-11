# append __str__ __len__ clear isEmpty remove(index)
class DummyDoublyCircular:
    def __init__(self):
        self.head = Node()
        self.head.prev = self.head.next = self.head
        self.size = 0

    def __str__(self):
        s = str(self.head.next.data)
        cur = self.head.next
        while cur.next != self.head:
            s += ' ' + str(cur.next.data)
            cur = cur.next
        return s

    def __len__(self):
        return self.size

    def reverse(self):
        cur = self.head
        for i in range(-1, len(self)):
            cur.prev, cur.next = cur.next, cur.prev
            cur = cur.prev

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, value):
        cur = self.head.next
        for i in range(len(self)):
            if cur.data == value:
                return i
            cur = cur.next
        return -1

    def nodeAt(self, index):
        if index < 0:
            index += self.size
        if index > self.size:
            index = self.size
        cur = self.head
        for i in range(-1, index):
            cur = cur.next
        return cur

    def insert(self, index, value):
        nodeAfter = self.nodeAt(index)
        nodeBefore = nodeAfter.prev
        newNode = Node(value, nodeAfter, nodeBefore)
        nodeBefore.next = nodeAfter.prev = newNode
        self.size += 1

    def appendFront(self, value):
        self.insert(0, value)

    def append(self, value):
        self.insert(len(self), value)

    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
        return node.data

    def pop(self, index=-1):
        if not self.isEmpty():
            if -self.size <= index <= self.size - 1:
                return self.removeNode(self.nodeAt(index))
            return 'POP Out of Range'
        return 'Empty'

    def remove(self, value):
        self.removeNode(self.nodeAt(self.indexOf(value)))

    def removeAll(self, value):
        while self.indexOf(value) != -1:
            self.removeNode(self.nodeAt(self.indexOf(value)))

    def removeDuplicate(self):
        temp = DummyDoublyCircular()
        cur = self.head.next
        for i in range(len(self)):
            if temp.indexOf(cur.data) == -1:
                temp.append(cur.data)
                self.append(cur.data)
            cur = cur.next
            self.removeNode(cur.prev)

    def clear(self):
        self.head.prev = self.head.next = self.head
        self.size = 0


class Queue:
    def __init__(self, li=None):
        if li == None:
            self.items = DummyDoublyCircular()
        else:
            self.items = li

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items.nodeAt(0).data


def get_digit(num, _round):
    for i in range(_round):
        num //= 10
    return num % 10


def get_max_digit(queue):
    max_digit = 0
    for i in range(len(queue)):
        max_digit = len(str(queue.peek())) if max_digit < len(
            str(queue.peek())) else max_digit
        queue.enQueue(queue.deQueue())
    return max_digit


def radix_sort(queue):
    num_digit = [Queue(), Queue(), Queue(), Queue(), Queue(),
                 Queue(), Queue(), Queue(), Queue(), Queue()]

    for i in range(get_max_digit(queue)):
        while len(queue) != 0:
            t = queue.deQueue()
            num = get_digit(t, i)
            num_digit[num].enQueue(t)
        for j in num_digit:
            while len(j) != 0:
                queue.enQueue(j.deQueue())


q = Queue()
for i in input('Enter Input : ').split(', '):
    q.enQueue(int(i))
print(q)
radix_sort(q)
print(q)
