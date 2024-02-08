class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def max_height(root):
    if root is None:
        return 0
    else:
        left_height = max_height(root.left)
        right_height = max_height(root.right)

        # Height of the tree is maximum of left and right subtrees plus 1 for the root
        return max(left_height, right_height) + 1


# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Maximum height of the tree:", max_height(root))
