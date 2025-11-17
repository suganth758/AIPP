# Simple BST Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Simple BST
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def inorder_traversal(self):
        self._inorder(self.root)
        print()  # new line

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)


# --- Test ---
bst = BST()
bst.insert(40)
bst.insert(20)
bst.insert(60)
bst.insert(10)
bst.insert(30)

print("Inorder traversal:")
bst.inorder_traversal()  # Expected: 10 20 30 40 60
