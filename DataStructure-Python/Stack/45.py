class Stack:
    def __init__ (self, item=None):
        if item == None:
            self.item = []
        else:
            self.item = item

    def push(self, new_items):
        self.item.append(new_items)
        #print(self.item)
    
    def peek(self):
        return self.item[-1]
    
    def pop(self):
        temp = self.item[-1]
        self.item.pop(-1)
        return temp

    def is_empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)

stack = Stack()
master_stack = []
_inp = input("Enter Input : ").split(",")   
#_inp = "A 4,A 3,B,S,B,A 5,A 6,B,S,B".split(",")
for x in _inp:
    if x[0] == 'A':
        _split = x.split()
        while(stack.size() and stack.peek() <= int(_split[1])):
            stack.pop()
        stack.push(int(_split[1]))
        master_stack.append(int(_split[1]))
        print(stack.item)
    elif x[0] == 'B':
        print(str(stack.size()))
    elif x[0] == 'S':
        if len(master_stack):
            for i in range(len(master_stack)):
                if master_stack[i]%2==0:
                    master_stack[i] -= 1
                else:
                    master_stack[i] +=2
        temp = master_stack.copy()
        stack = Stack()
        for xx in temp:
            while(stack.size() and stack.peek() <= xx):
                stack.pop()
            stack.push(xx)