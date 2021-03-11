class Stack:
    def __init__(self,li = None):
        if li == None:
            self.li = []
        else :
            self.li = li
    def push(self,i):
        self.li.append(i)
    def peek(self):
        if len(self.li) > 0:
            return self.li[-1]
    def pop(self,i=None):
        if i == None:
            return self.li.pop()
        else : 
            return self.li.pop(i)
    def isEmpty(self):
        return len(self.li) == 0
    def size(self):
        return len(self.li)
    def get(self):
        return self.li

inp = input("Enter Input : ").split(',')
s = Stack()
all_items = []
abnormal = False
count = 0
for i,j in enumerate(inp):            
    if j.startswith('A'):
        while (not s.isEmpty()) and int(inp[i].split(' ')[1]) >= int(s.peek().split(' ')[1]):
            s.pop()
        s.push(inp[i])
        all_items.append(inp[i])
    if j.startswith('B'):
        print(s.size())
    if j.startswith('S'):
        if len(all_items) > 0:
            for x,y in enumerate(all_items):
                if int(y.split(' ')[1]) % 2 == 0:
                    all_items[x] = 'A ' + str(int((y.split(' ')[1])) - 1) if int((y.split(' ')[1])) - 1 >= 1 else 'A 1'
                else :
                    all_items[x] = 'A ' + str(int((y.split(' ')[1])) + 2)
            s = Stack()
            for m in all_items:
                while s.size() > 0 and int(s.peek().split(' ')[1]) <= int(m.split(' ')[1]):
                    s.pop()
                s.push(m)