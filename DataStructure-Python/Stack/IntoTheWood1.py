class Stack:
    def __init__(self,li = None):
        if li == None:
            self.li = []
        else :
            self.li = li
    def push(self,i):
        self.li.append(i)
    def peek(self):
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
    def getStack(self):
        return self.li
inp = input('Enter Input : ').split(',')
temp = []
for i in inp:
    if i.startswith('A'):
        while len(temp) > 0 and int(i.split(' ')[1]) >= int(temp[-1].split(' ')[1]):
            temp.pop()
        temp.append(i)
    elif i.startswith('B'):
        print(len(temp))