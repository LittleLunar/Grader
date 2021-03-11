class Stack:
    def __init__(self,lis = None):
        if lis == None:
            self.li = []
        else:
            self.li = lis
    def push(self,i):
        self.li.append(i)
    def pop(self):
        return self.li.pop()
    def peek(self):
        return self.li[-1]
    def isEmpty(self):
        return self.li == []
    def size(self):
        return len(self.li)

s = list(input("Enter Input : "))
n = Stack()
for i in s:
    if i in '({[':
        n.push(i)
    elif i in ')}]':
        if not n.isEmpty():
            if not '({['.index(n.pop()) == ')}]'.index(i):
                print("Parentheses : Unmatched ! ! !")
                break 
        else : 
            print("Parentheses : Unmatched ! ! !")
            break 
else:
    if n.isEmpty():
        print('Parentheses : Matched ! ! !')
    else : 
        print("Parentheses : Unmatched ! ! !")