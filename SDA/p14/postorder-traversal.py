class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def postorder_traversal(root):
    stack = []
    result = []

    if root is None:
        return result

    stack.append(root)

    while stack:
        current = stack.pop()
        result.append(current.data)

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    result.reverse()
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Postorder Traversal:")
result = postorder_traversal(root)
print(' '.join(str(val) for val in result))
