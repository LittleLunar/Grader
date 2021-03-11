class Stack:
    def __init__(self, li=None):
        if li == None:
            self.li = []
        else:
            self.li = li

    def push(self, i):
        self.li.append(i)

    def pop(self, i=None):
        if i == None:
            return self.li.pop()
        else:
            return self.li.pop(i)

    def peek(self):
        return self.li[-1]

    def isEmpty(self):
        return len(self.li) == 0

    def size(self):
        return len(self.li)


class StackCalc:
    def __init__(self):
        self.stack = Stack()

    def run(self, arg):
        for i in arg.split():
            if '0' <= i <= '9':
                self.stack.push(int(i))
            elif i == 'POP':
                self.stack.pop()
            elif i == 'DUP':
                self.stack.push(int(self.stack.peek()))
            elif i == '+':
                self.stack.push(self.stack.pop() + self.stack.pop())
            elif i == '-':
                self.stack.push(self.stack.pop() - self.stack.pop())
            elif i == '*':
                self.stack.push(self.stack.pop() * self.stack.pop())
            elif i == '/':
                self.stack.push(self.stack.pop() / self.stack.pop())
            else:
                print(f"Invalid instruction: {i}")
                break

    def getValue(self):
        return str(self.stack.pop()) if self.stack.size() > 0 else ''


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
