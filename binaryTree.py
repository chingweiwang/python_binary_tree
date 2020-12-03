
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def leftChild(self, left):
        self.left = left

    def rightChild(self, right):
        self.right = right

# Traversal
def preorder(n):
    if n:
        print(n.value, ' ', end='')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n:
        #print('@@1', n.value)
        inorder(n.left)
        print(n.value, ' ', end='')
        #print(n.value)
        #print('@@2')
        inorder(n.right)

def postorder(n):
    if n:
        postorder(n.left)
        postorder(n.right)
        print(n.value, ' ', end='')

qu = []
def levelorder(n):
    qu.append(n)

    while len(qu) > 0:
        print(qu[0].value, ' ', end='')
        if qu[0].left != None:
            qu.append(qu[0].left)
        if qu[0].right != None:
            qu.append(qu[0].right)
        del qu[0]    

n1 = Node('A')
root = n1
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n7 = Node('F')

n1.leftChild(n2)
n1.rightChild(n3)

n2.leftChild(n4)
n2.rightChild(n5)

n3.rightChild(n7)

print('Preorder Traversal: ', end='')
preorder(root)

print()

print('Inorder Traversal: ', end='')
inorder(root)

print()

print('Postorder Traversal: ', end='')
postorder(root)

print()

print('Levelorder Traversal: ', end='')
levelorder(root)

