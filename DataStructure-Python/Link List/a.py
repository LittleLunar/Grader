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
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += "->" + str(cur.next.value)
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
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p
        self.sizes += 1

    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head.previous = p
            self.head = p
        self.sizes += 1

    def insert(self, pos, item):
        p = Node(item)

        if pos >= self.sizes-1:
            self.append(item)
        elif pos < 0 and pos >= -self.sizes:
            cur = self.tail
            i = -1
            while i != pos:
                cur = cur.previous
                i -= 1
            p.next = cur
            p.previous = cur.previous
            cur.previous.next = p
            cur.previous = p
            self.sizes += 1
        else:
            self.addHead(item)

    def search(self, item):
        if self.isEmpty():
            return "Not Found"
        i = 0
        cur = self.head
        if cur.value == item:
            return "Found"
        while cur.value != item and i < self.sizes-1:
            i += 1
            cur = cur.next
            if cur.value == item:
                return "Found"
        else:
            return "Not Found"

    def searchVal(self, index):
        i = 0
        cur = self.head
        while i < index:
            i += 1
            cur = cur.next
        return cur.value

    def index(self, item):
        if self.search(item) == "Found":
            i = 0
            cur = self.head
            if cur.value == item:
                return i
            while cur.value != item:
                i += 1
                cur = cur.next
                if cur.value == item:
                    return i
        else:
            return -1

    def size(self):
        return self.sizes

    def pop(self, pos):
        if pos < self.sizes and pos >= 0 and self.sizes > 0:
            self.sizes -= 1
            if pos == 0:
                temp = self.head
                self.head = self.head.next
                temp.previous = None
            elif pos == self.sizes-1:
                self.tail.previous.next = None
                self.tail = self.tail.previous
            else:
                i = 0
                cur = self.head

                while i < pos and i < self.sizes:
                    i += 1
                    cur = cur.next
                cur.previous.next = cur.next
                cur.next.previous = cur.previous
                cur.next = None
                cur.previous = None
            return "Success"
        else:
            return "Out of Range"

    def setNewNext(self, old, new):
        i = 0
        j = 0
        curOld = self.head
        curNew = self.head
        while i < old:
            i += 1
            curOld = curOld.next
        while j < new:
            j += 1
            curNew = curNew.next

        curOld.next = curNew

    def checkLoop(self):
        mem = []
        count = 0
        buffer = self.head
        for x in range(500):
            count += 1
            if buffer is None:
                break
            if buffer in mem:
                return 1
            mem.append(buffer)
            buffer = buffer.next
        return 0

inp = input("Enter input : ").split(",")
L = LinkedList()

for i in inp:
    if i[0] == 'A':
        L.append(i[2:])
        print(L)
    elif i[0] == 'S':
        if L.size() == 0:
            print("Error! {list is empty}")
        elif int(i[2]) >= L.size():
            print("Error! {}index not in length{}: {}".format("{", "}", i[2]))
        elif int(i[4:]) >= L.size():
            print("index not in length, append : {}".format(i[4:]))
            L.append(i[4:])
        else:
            print("Set node.next complete!, index:value = {}:{} -> {}:{}".format(
                i[2], L.searchVal(int(i[2])), i[4], L.searchVal(int(i[4]))))
            L.setNewNext(int(i[2]), int(i[4]))

print("Found Loop" if L.checkLoop() else "No Loop\n{}".format(L))

# print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
#       "Success" else ("{0} | {1}".format(k, L)))
