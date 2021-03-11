class Node:
    def __init__(self, value=None, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, li=None):
        if li == None:
            self.queue = []
        else:
            self.queue = li

    def __len__(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def enQ(self, value):
        self.queue.append(value)

    def deQ(self):
        return self.queue.pop(0)

    def peak(self):
        return self.queue[-1]


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            t = self.root
            if value < self.root.data:
                if self.root.left != None:
                    self.root = self.root.left
                    self.insert(value)
                else:
                    self.root.left = Node(value)
            else:
                if self.root.right != None:
                    self.root = self.root.right
                    self.insert(value)
                else:
                    self.root.right = Node(value)
            self.root = t

    def printTree(self, level=0, node=-999):
        if node == -999:
            node = self.root
        if node != None:
            self.printTree(level + 1, node.right)
            print('     ' * level, node)
            self.printTree(level + 1, node.left)

    def PreOrder(self, node=-999):
        if node == -999:
            node = self.root
        if node == None:
            return ''
        return str(node) + ' ' + self.PreOrder(node.left) + self.PreOrder(node.right)

    def InOrder(self, node=-999):
        if node == -999:
            node = self.root
        if node == None:
            return ''
        return self.InOrder(node.left) + str(node) + ' ' + self.InOrder(node.right)

    def PostOrder(self, node=-999):
        if node == -999:
            node = self.root
        if node == None:
            return ''
        return self.PostOrder(node.left) + self.PostOrder(node.right) + str(node) + ' '

    def Breadth(self):
        s = ''
        if self.root != None:
            queue = Queue()
            queue.enQ(self.root)
            while not queue.isEmpty():
                n = queue.deQ()
                s += str(n) + ' '
                if(n.left != None):
                    queue.enQ(n.left)
                if(n.right != None):
                    queue.enQ(n.right)
        return s


T = BST()
inp = list(map(int, input('Enter Input : ').split()))
for i in inp:
    T.insert(i)
print('Preorder : {}'.format(T.PreOrder()))
print('Inorder : {}'.format(T.InOrder()))
print('Postorder : {}'.format(T.PostOrder()))
print('Breadth : {}'.format(T.Breadth()))
