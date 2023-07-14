class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.data, end=" ")
            self.inOrder(node.right)

    def preOrder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=" ")

    def fullBinaryTree(self, arr, size, location):
        if location >= size:
            return None
        
        head = TreeNode(arr[location])
        head.left = self.fullBinaryTree(arr, size, (location * 2) + 1)
        head.right = self.fullBinaryTree(arr, size, (location * 2) + 2)
        
        return head

if __name__ == "__main__":
    tree = BinaryTree()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    size = len(arr)
    tree.root = tree.fullBinaryTree(arr, size, 0)

    print("Creating binary tree:")
    print("In-order Data:")
    tree.inOrder(tree.root)
    print("\nPre-order Data:")
    tree.preOrder(tree.root)
    print("\nPost-order Data:")
    tree.postOrder(tree.root)
