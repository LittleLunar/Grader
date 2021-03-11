class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = Node(item)
        else:
            q = Node(item)
            p = self.head
            while p.next != None:
                p = p.next
            p.next = q
            q.previous = p
            self.tail = q
        self.sizes += 1

    def addHead(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = Node(item)
        else:
            q = Node(item)
            p = self.tail
            while p.previous != None:
                p = p.previous
            p.previous = q
            q.next = p
            self.head = q
        self.sizes += 1

    def insert(self, pos, item):
        if pos < -1*self.sizes:
            self.addHead(item)
        elif pos > self.sizes - 1:
            self.append(item)
        else:
            if pos < 0:
                pos = self.sizes + pos
            q = Node(item)
            p = self.head
            for i in range(pos - 1):
                p = p.next
            q.next = p.next
            q.previous = p
            p.next.previous = q
            p.next = q
            self.sizes += 1

    def search(self, item):
        p = self.head
        while p != None:
            if p.value == item:
                return 'Found'
            p = p.next
        return 'Not Found'

    def index(self, item):
        p = self.head
        i = 0
        while p != None:
            if p.value == item:
                return i
            i += 1
            p = p.next
        return -1

    def size(self):
        return self.sizes

    def pop(self, pos):
        if 0 <= pos <= self.sizes - 1:
            p = self.head
            for i in range(pos - 1):
                p = p.next
            if pos == 0:
                self.head = self.head.next
                self.sizes -= 1
                return 'Success'
            else:
                p.next = p.next.next
                self.sizes -= 1
                return 'Success'

        else:
            return 'Out of Range'


L1 = LinkedList()
L2 = LinkedList()
inp = input('Enter Input (L1,L2) : ').split()
for i in inp[0].split('->'):
    L1.append(i)
for i in inp[1].split('->'):
    L2.append(i)
print(f'L1    : {L1}')
print(f'L2    : {L2}')
print(f'Merge : {L1}{L2.reverse()}')
