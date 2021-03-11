class Node:
    def __init__(self, value=None, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self, li=None):
        if li == None:
            self.items = []
        else:
            self.items = li

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1]


class BST:
    def __init__(self):
        self.root = None

    def printTree(self, node=-999, level=0):
        if node == -999:
            node = self.root
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insertByPostFix(self, items):
        S = Stack()
        for i in items:
            if i in '+-*/^':
                r = S.pop()
                l = S.pop()
                newNode = Node(i, l, r)
                S.push(newNode)
            else:
                S.push(Node(i))
        self.root = S.pop()

    def PreOrder(self, node=-999):
        if node == -999:
            node = self.root
        if node == None:
            return ''
        return str(node) + self.PreOrder(node.left) + self.PreOrder(node.right)

    def InOrder(self, node=-999):
        if node == -999:
            node = self.root
        if node == None:
            return ''
        return self.InOrder(node.left) + str(node) + self.InOrder(node.right)

    def Infix_withBracket(self):
        S = Stack()
        for i in self.PostOrder():
            if i in '+-*/^':
                r = S.pop()
                l = S.pop()
                t = '(' + str(l) + i + str(r) + ')'
                S.push(t)
            else:
                S.push(i)
        return S.pop()

    def PostOrder(self, node=-999):
        if node == -999:
            node = self.root
        if node == None:
            return ''
        return self.PostOrder(node.left) + self.PostOrder(node.right) + str(node)


inp = input('Enter Postfix : ')
T = BST()
T.insertByPostFix(inp)
print('Tree : ')
T.printTree()
print('--------------------------------------------------')
print('Infix : {}'.format(T.Infix_withBracket()))
print('Prefix : {}'.format(T.PreOrder()))
