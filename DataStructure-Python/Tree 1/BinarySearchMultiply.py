class Node:
    def __init__(self, value=None, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            t = self.root
            if value < self.root.data:
                if self.root.left == None:
                    self.root.left = Node(value)
                else:
                    self.root = self.root.left
                    self.insert(value)
            else:
                if self.root.right == None:
                    self.root.right = Node(value)
                else:
                    self.root = self.root.right
                    self.insert(value)
            self.root = t

    def printTree(self, node=-999, level=0):
        if node == -999:
            node = self.root
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def multiply(self, value, node=-999):
        if node == -999:
            node = self.root
        if node != None:
            if value < node.data:
                node.data *= 3
            if node.left != None:
                self.multiply(value, node.left)
            if node.right != None:
                self.multiply(value, node.right)


T = BinaryTree()
inp = list(map(str, input('Enter Input : ').split('/')))
for i in inp[0].split():
    root = T.insert(int(i))
T.printTree()
T.multiply(int(inp[1]))
print('--------------------------------------------------')
T.printTree()
