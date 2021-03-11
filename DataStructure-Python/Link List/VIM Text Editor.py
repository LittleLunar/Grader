class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.sizes = 0

    def __str__(self):
        if self.isEmpty():
            return 'List is Empty'
        else:
            cur = self.head
            s = ""
            while cur.next != None:
                s += str(cur.data) + ' '
                cur = cur.next
            s += str(cur.data)
            return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, " "
        while cur.previous != None:
            s += str(cur.data) + " "
            cur = cur.previous
        s += str(cur.data)
        return s

    def isEmpty(self):
        return self.sizes == 0

    def size(self):
        return self.sizes

    def append(self, data):
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            t = Node(data)
            t.previous = self.tail
            t.next = self.tail.next
            self.tail.next = t
            self.tail = t
        self.sizes += 1

    def addHead(self, data):
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            t = Node(data)
            t.next = self.head
            t.previous = self.head.previous
            self.head.previous = t
            self.head = t
        self.sizes += 1

    def insert(self, index, data):
        if index == 0 or index < -1*self.sizes:
            self.addHead(data)
        elif index > self.sizes - 1:
            self.append(data)
        else:
            if index < 0:
                index = self.sizes + index
            q = Node(data)
            p = self.head
            for i in range(index - 1):
                p = p.next
            q.next = p.next
            q.previous = p
            p.next.previous = q
            p.next = q
            self.sizes += 1

    def index(self, data):
        p = self.head
        i = 0
        while p != None:
            if p.data == data:
                return i
            i += 1
            p = p.next
        return -1

    def pop(self, index=None):
        if index == 0 or index == -1*self.sizes:
            self.head.next.previous = self.head.previous
            self.head = self.head.next
        elif index == None or index == -1 or index == self.sizes - 1:
            self.tail.previous.next = self.tail.next
            self.tail = self.tail.previous

        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            if cur.next.next != None:
                cur.next.next.previous = cur
            cur.next = cur.next.next
        self.sizes -= 1

    def VIM_Action(self, act, data=None):
        if self.head == None:
            self.head = self.tail = Node('|')
            self.sizes += 1

        if act == 'I':
            self.insert(self.index('|'), data)
        elif act == 'L':
            if self.sizes >= 2:
                cur = self.tail
                while cur.previous != None:
                    if cur.data == '|':
                        break
                    cur = cur.previous
                q = Node(cur.data)
                if cur == self.tail:
                    q.previous = cur.previous.previous
                    q.next = cur.previous
                    if cur.previous.previous != None:
                        cur.previous.previous.next = q
                    else:
                        self.head = q
                    cur.previous.next = cur.next
                    cur.previous.previous = q
                    self.tail = cur.previous
                elif cur.previous != None:
                    q.previous = cur.previous.previous
                    q.next = cur.previous
                    if cur.previous != self.head:
                        cur.previous.previous.next = q
                    else:
                        self.head = q
                    cur.previous.next = cur.next
                    cur.previous.previous = q
                    cur.next.previous = cur.previous

        elif act == 'R':
            if self.sizes >= 2:
                cur = self.head
                while cur.next != None:
                    if cur.data == '|':
                        break
                    cur = cur.next
                q = Node(cur.data)
                if cur == self.head:
                    q.next = cur.next.next
                    q.previous = cur.next
                    if cur.next.next != None:
                        cur.next.next.previous = q
                    else:
                        self.tail = q
                    cur.next.next = q
                    cur.next.previous = cur.previous
                    self.head = cur.next
                elif cur.next != None:
                    q.next = cur.next.next
                    q.previous = cur.next
                    if cur.next != self.tail:
                        cur.next.next.previous = q
                    else:
                        self.tail = q
                    cur.previous.next = cur.next
                    cur.next.previous = cur.previous
                    cur.next.next = q

        elif act == 'B':
            if self.head.data != '|':
                self.pop(self.index('|') - 1)
        elif act == 'D':
            if self.tail.data != '|':
                self.pop(self.index('|') + 1)


L = LinkedList()

inp = input('Enter Input : ').split(',')

for i in inp:
    if i.startswith('I'):
        L.VIM_Action(i.split()[0], i.split()[1])
    else:
        L.VIM_Action(i)
print(L)
