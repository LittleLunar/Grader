class Node:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None
        self.height = 1

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        pass

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)

        return root

    def bfs(self, root):
        q = [root]
        while q:
            d = q.pop(0)
            # do sth
            print(f"{d}", end=" ")
            # do sth
            if d.left:
                q.append(d.left)
            if d.right:
                q.append(d.right)

    def dfs(self, root, s):
        if s == "preOrder":
            self.preOrder(root)
        elif s == "inOrder":
            self.inOrder(root)
        elif s == "postOrder":
            self.postOrder(root)

    def preOrder(self, root):
        if root:
            print(f"{root.data}", end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(f"{root.data}", end=" ")
            self.inOrder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(f"{root.data}", end=" ")

    def printTree(self, root, level=0):
        if root:
            self.printTree(root.right, level + 1)
            print("     " * level, root)
            self.printTree(root.left, level + 1)


class AVL:
    def __init__(self):
        pass

    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balance = self.getBalance(root)
        # Left left
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)
        # Right right
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)
        # Left right
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Right left
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, root):
        mid = root.right
        root.right = mid.left
        mid.left = root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        mid.height = 1 + max(self.getHeight(mid.left),
                             self.getHeight(mid.right))
        return mid

    def rightRotate(self, root):
        mid = root.left
        root.left = mid.right
        mid.right = root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        mid.height = 1 + max(self.getHeight(mid.left),
                             self.getHeight(mid.right))
        return mid

    def getHeight(self, root):
        return root.height if root else 0

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right) if root else 0

    def printTree(self, root, level=0):
        if root:
            self.printTree(root.right, level + 1)
            print("     " * level, root)
            self.printTree(root.left, level + 1)

    def preOrder(self, root):
        if root:
            print(f"{root.data}", end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)


T = BST()
root = None
for i in list(map(int, input("Enter : ").split(','))):
    root = T.insert(root, i)

T.printTree(root)
print("preorder : ")
T.dfs(root, "preOrder")
print("\ninorder: ")
T.dfs(root, "inOrder")
print("\npostorder : ")
T.dfs(root, "postOrder")
print("\nbreadth : ")
T.bfs(root)
