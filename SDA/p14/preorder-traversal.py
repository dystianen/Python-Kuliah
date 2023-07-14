class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def preorder_traversal(root):
    stack = []
    stack.append(root)

    while stack:
        current = stack.pop()
        print(current.data, end=" ")

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder Traversal:")
preorder_traversal(root)
