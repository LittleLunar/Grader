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
        if not self.isEmpty():
            cur = self.head
            s = ""
            while cur.next != None:
                s += str(cur.data) + ' -> '
                cur = cur.next
            s += str(cur.data)
            return s
        else:
            return ''

    def str_without(self):
        if not self.isEmpty():
            cur = self.head
            s = ""
            while cur.next != None:
                s += str(cur.data) + ' '
                cur = cur.next
            s += str(cur.data)
            return s
        else:
            return ''

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

    def search(self, data):
        cur = self.head
        while cur != None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

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


def RadixSort(L=LinkedList()):
    before_sort, after_sort = L, LinkedList()
    roundtake = 1
    cur = before_sort.head
    q = -1
    while True:
        print('------------------------------------------------------------')
        print(f'Round : {roundtake}')
        for j in range(10):
            print(f'{j} : ', end='')
            m = LinkedList()
            t = before_sort.head
            while t != None:
                w = len(t.data)
                if '-' in t.data:
                    w -= 1
                if (q < -w and j == 0):
                    if m.size() == 0:
                        m.append(t.data)
                    else:
                        if int(m.tail.data) >= int(t.data) >= int(m.head.data):
                            a = m.head
                            ind = 0
                            while a != None:
                                if int(a.data) >= int(t.data):
                                    m.insert(ind, t.data)
                                    break
                                ind += 1
                                a = a.next
                        elif int(m.head.data) > int(t.data):
                            m.addHead(t.data)
                        elif int(m.tail.data) < int(t.data):
                            m.append(t.data)
                if q >= -w:
                    if t.data[q] == str(j):
                        if m.size() == 0:
                            m.append(t.data)
                        else:
                            if int(m.tail.data) >= int(t.data) >= int(m.head.data):
                                a = m.head
                                ind = 0
                                while a != None:
                                    if int(a.data) >= int(t.data):
                                        m.insert(ind, t.data)
                                        break
                                    ind += 1
                                    a = a.next
                            elif int(m.head.data) > int(t.data):
                                m.addHead(t.data)
                            elif int(m.tail.data) < int(t.data):
                                m.append(t.data)
                t = t.next
            print(m.str_without())
            if m.size() == before_sort.size() and j == 0:
                after_sort = m
        if before_sort.size() == after_sort.size():
            break
        roundtake += 1
        q -= 1
    print('------------------------------------------------------------')
    print(f'{roundtake - 1} Time(s)')
    print(f'Before Radix Sort : {before_sort}')
    print(f'After  Radix Sort : {after_sort}')
    L = after_sort


inp = input("Enter Input : ").split()
L = LinkedList()
for i in inp:
    L.append(i)
RadixSort(L)
