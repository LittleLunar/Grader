class Stack:
    def __init__(self, lst = []):
        self.stack = lst
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self, lst):
        self.queue = lst
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

class Singly:

    class Node:
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insert(self, index, data):
        if 0 <= index <= self.size:
            if self.head == None:
                self.head = self.Node(data)
            else:
                if index == 0:
                    self.head = self.Node(data, self.head)
                else:
                    p = self.head     
                    for i in range(index - 1):
                        p = p.next
                    self.
            self.size += 1

    def append(self, data):

        if self.head == None:
            self.head = self.Node(data)

        else:
            newNode = self.Node(data)
            p = self.head
            while p.next != None:
                p = p.next
            p.next = newNode

        self.size += 1

    def pop(self, index = -1):

        if self.size != 0:
            
            if -self.size <= index <= self.size - 1:
                
                if index < 0:
                    index += self.size

                if index == 0:
                    r = self.head
                    self.head = self.head.next
                else:
                    p = self.head
                    for i in range(index - 1):
                        p = p.next
                    r = p.next
                    p = p.next.next
                    
                    self.size -= 1

                return r
        
        return -1

    def indexOf(self, data):

        p = self.head
        i = 0
        while p != None:
            if p.data == data:
                return i
            i += 1
            p = p.next
        return -1
    