class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            t = self.root
            if data < self.root.data:
                if self.root.left == None:
                    self.root.left = Node(data)
                else:
                    self.root = self.root.left
                    self.insert(data)
            else:
                if self.root.right == None:
                    self.root.right = Node(data)
                else:
                    self.root = self.root.right
                    self.insert(data)
            self.root = t
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)            
            self.printTree(node.left, level + 1)

    def mini(self):
        if self.root.left == None:
            return self.root.data
        t = self.root
        self.root = self.root.left
        min_ = self.mini()
        self.root = t
        return min_

    def maxi(self):
        if self.root.right == None:
            return self.root.data
        t = self.root
        self.root = self.root.right
        max_ = self.maxi()
        self.root = t
        return max_


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print('Min :', T.mini())
print('Max :', T.maxi())
