class Node:
    def __init__(self, value=None, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            print('*', end='')
            self.root = Node(value)
        else:
            t = self.root
            if value < self.root.data:
                print('L', end='')
                if self.root.left == None:
                    print('*', end='')
                    self.root.left = Node(value)
                else:

                    self.root = self.root.left
                    self.insert(value)
            else:
                print('R', end='')
                if self.root.right == None:
                    print('*', end='')
                    self.root.right = Node(value)

                else:
                    self.root = self.root.right
                    self.insert(value)
            self.root = t

    def insertN(self, value, cur=-999):
        if self.root == None:
            self.root = Node(value)
            return

        if cur == -999:
            cur = self.root

        if cur == None:
            cur = Node(value)
            return cur

        if value < cur.data:
            cur.left = self.insertN(value, cur.left)
        else:
            cur.right = self.insertN(value, cur.right)

        return cur

    def printTree(self, node=-999, level=0):
        if node == -999:
            node = self.root
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


inp = list(map(int, input('Enter Input : ').split()))
B = BST()
for i in inp:
    B.insertN(i)
B.printTree()
