class Node:
    def __init__(self, value=None, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        return str(self.data)


class AVLBST:
    def __init__(self):
        self.root = None

    def _rightRotate(node):
        mid = node.left
        node.left = mid.right
        mid.right = node
        node.height = max(AVLBST._getHeight(node.right),
                          AVLBST._getHeight(node.left)) + 1
        mid.height = max(AVLBST._getHeight(mid.right),
                         AVLBST._getHeight(mid.left)) + 1
        return mid

    def _leftRotate(node):
        mid = node.right
        node.right = mid.left
        mid.left = node
        node.height = max(AVLBST._getHeight(node.right),
                          AVLBST._getHeight(node.left)) + 1
        mid.height = max(AVLBST._getHeight(mid.right),
                         AVLBST._getHeight(mid.left)) + 1
        return mid

    def _getHeight(node):
        return node.height if node else 0

    def _findMin(node):
        return AVLBST._findMin(node.left) if node.left else node

    def _findMax(node):
        return AVLBST._findMax(node.right) if node.right else node

    def _delete(node, value):
        if node == None:
            return node

        if value < node.data:
            node.left = AVLBST._delete(node.left, value)
        elif value > node.data:
            node.right = AVLBST._delete(node.right, value)
        else:
            if not node.left and not node.right:
                node = None

            elif node.left and not node.right:
                temp = node.left
                node.left = None
                node = temp

            elif node.right and not node.left:
                temp = node.right
                node.right = None
                node = temp

            else:
                balance = AVLBST._getHeight(
                    node.left) - AVLBST._getHeight(node.right)
                if balance >= 0:
                    temp = AVLBST._findMin(node.right)
                    node.data = temp.data
                    node.right = AVLBST._delete(node.right)
                else:
                    temp = AVLBST._findMax(node.left)
                    node.data = temp.data
                    node.left = AVLBST._delete(node.left)

        return node

    def insert(self, value):
        AVLBST._insert(self.root, value)

    def _insert(node, value):
        if node == None:
            return node
        if value < node.data:
            node.left = AVLBST._insert(node.left, value)
        if value >= node.data:
            node.right = AVLBST._insert(node.right, value)
        node.height = max(AVLBST._getHeight(node.left),
                          AVLBST._getHeight(node.right)) + 1
        
    
        return node

    def printTree(self):
        AVLBST._printTree(self.root, 0)

    def _printTree(node, level):
        if node:
            AVLBST._printTree(node.right, level + 1)
            print('     ' * level, node)
            AVLBST._printTree(node.left, level + 1)
