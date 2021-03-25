from statistics import mode

class Node:
    def __init__(self, data = None,next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)

class DummySingly:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __str__(self):
        if not self.isEmpty():
            s = str(self.head.next.data)
            cur = self.head.next
            while cur.next != None:
                s += ' ' + str(cur.next.data)
                cur = cur.next
            return s

    def reverse(self):
        if not self.isEmpty():
            q = None
            cur = self.head.next
            p = cur.next
            while p != None:
                cur.next = q
                q = cur
                cur = p
                p = p.next
            cur.next = q
            self.head.next = cur
            return str(self)

    def __len__(self):
        return self.size

    def insert(self, index, data):
        if 0 <= index <= self.size:
            cur = self.head
            for i in range(index):
                cur = cur.next
            newNode = Node(data, cur.next)
            cur.next = newNode
            self.size += 1

    def pop(self, index = -1):
        if not self.isEmpty():
            if -self.size <= index <= self.size - 1:
                if index < 0:
                    index += self.size
                cur = self.head
                for i in range(index):
                    cur = cur.next
                r = cur.next
                cur.next = cur.next.next
                self.size -= 1
                return r.data


    def addHead(self, data):
        self.insert(0,data)

    def append(self, data):
        self.insert(self.size, data)
    
    def isEmpty(self):
        return self.size == 0

class DummyDoubly:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __str__(self):
        if not self.isEmpty():
            s = str(self.head.next.data)
            cur = self.head.next
            while cur.next != None:
                s += ' ' + str(cur.next.data)
                cur = cur.next
            return s
        else:
            return 'Empty'

    def __len__(self):
        return self.size
    
    def reverse(self):
        if not self.isEmpty():
            cur = self.head
            for i in range(self.size):
                cur = cur.next
            s = str(cur.data)
            while cur.prev != self.head:
                s += ' ' + str(cur.prev.data)
                cur = cur.prev
            return s
        else:
            return 'Empty'

    def insert(self, index, data):
        if 0 <= index <= self.size:
            cur = self.head
            for i in range(index):
                cur = cur.next
            newNode = Node(data, cur.next, cur)
            if cur.next != None:
                cur.next.prev = newNode
            cur.next = newNode
            self.size += 1

    def pop(self, index = -1):
        if not self.isEmpty():
            if -self.size <= index <= self.size - 1:
                if index < 0:
                    index += self.size
                cur = self.head
                for i in range(index):
                    cur = cur.next
                r = cur.next
                cur.next = cur.next.next
                if cur.next != None:
                    cur.next.prev = cur
                self.size -= 1
                return r.data
            else:
                return 'Out of Range'
    
    def append(self, data):
        self.insert(self.size, data)
    
    def addHead(self, data):
        self.insert(0, data)

    def isEmpty(self):
        return self.size == 0

    def get_data(self, index):
        if not self.isEmpty():
            if 0 <= index <= self.size - 1:
                cur = self.head
                
                for i in range(index):
                    cur = cur.next
                return cur.next.data

    def indexOf(self, data):
        cur = self.head.next
        i = 0
        while cur != None:
            if cur.data == data:
                return i
            i += 1
            cur = cur.next
        return -1

    def get_list(self):
        l = []
        for i in range(self.size):
            l.append(self.get_data(i))
        return l

    def contentEquivalence(self, other):
        if len(self) == len(other):
            for i in range(len(self)):
                if other.indexOf(self.get_data(i)) == -1:
                    return False
            return True
        return False

    def duplicate(self):
        lst = []
        p = self.head.next
        while p != None:
            lst.append(p.data)
            while p.next != None and p.next.data in lst:
                p.next = p.next.next # 1 1 1 2 3 3 3
            p = p.next
        

# ll1 = DummyDoubly()
# ll2 = DummyDoubly()
# inp = input("Enter Input : ").split(',')
# for i in inp:
#     a = i.split()
#     if a[0] == 'AP':
#         ll1.append(a[1])
#     elif a[0] == 'PO':
#         t =  ll1.pop(int(a[1]))
#         if t == 'Out of Range':
#             print(f'Out of Range | {ll1}')
#         else:
#             print(f'Success | {t} -> {ll1}')

#     elif a[0] == 'SI':
#         print(f'Linked List size = {len(ll1)} : {ll1}')
#     elif a[0] == 'AH':
#         ll1.addHead(a[1])
# print("Linked List :",ll1)
# print("Linked List Reverse :",ll1.reverse())

# ll1 = DummyDoubly()
# inp = input("Enter input : ").split()
# for i in inp:
#     if ll1.isEmpty():
#         ll1.append(int(i))
#     else:
#         j = 0
#         while j < len(ll1) and ll1.get_data(j) < int(i) :
#             j += 1
#         ll1.insert(j, int(i))
# print(mode(ll1.get_list()))
ll1 = DummyDoubly()
ll2 = DummyDoubly()
for i in [0,1,2,3,4,2,3,7,8]:
    ll1.append(i)
for i in [2,1,4,5,0]:
    ll2.append(i)
print(ll1)
ll1.duplicate()
print(ll1)
# if ll1.contentEquivalence(ll2):
#     print('Equal')
# else:
#     print('Not Equal')