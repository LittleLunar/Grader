class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.sizes = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
            self.sizes += 1
        else:
            q = Node(item)
            p = self.head
            while p.next != None:
                p = p.next
            p.next = q
            self.sizes += 1

    def addHead(self, item):
        q = self.head
        self.head = Node(item)
        self.head.next = q
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


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
