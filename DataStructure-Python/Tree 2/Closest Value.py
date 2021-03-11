class Node:
    def __init__(self, value=None, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        self.root = BST._insert(self.root, value)

    def _insert(node, value):
        if not node:
            return Node(value)
        if value < node.data:
            node.left = BST._insert(node.left, value)
        else:
            node.right = BST._insert(node.right, value)
        return node

    def printTree(self, node=-999, level=0):
        if node == -999:
            node = self.root
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


def closestValue(node, value):
    # if not node:
    #     return 999
    # if node.data == value:
    #     return node.data
    # l = closestValue(node.left, value)
    # r = closestValue(node.right, value)
    # s = sorted([abs(value - l), abs(value - node.data), abs(value - r)])
    # if s[0] == abs(value - l):
    #     return l
    # elif s[0] == abs(value - r):
    #     return r
    # elif s[0] == abs(value - node.data):
    #     return node.data
    if node:
        cur = node
        theClosestOne = node.data
        while True:
            if value == cur.data:
                return cur.data

            if abs(value - cur.data) < abs(value - theClosestOne):
                theClosestOne = cur.data

            if value < cur.data:
                if cur.left:
                    cur = cur.left
                    continue
                else:
                    return theClosestOne

            if value > cur.data:
                if cur.right:
                    cur = cur.right
                    continue
                else:
                    return theClosestOne


inp = input('Enter Input : ').split('/')
T = BST()
for i in inp[0].split():
    T.insert(int(i))
    T.printTree()
    print('--------------------------------------------------')
print('Closest value of {} : {}'.format(
    int(inp[1]), closestValue(T.root, int(inp[1]))))
