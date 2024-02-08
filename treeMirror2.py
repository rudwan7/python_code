class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isMirror(root1, root2):
    # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
        return True

    # For two trees to be mirror images, the following three conditions must be true:
    # 1. Their root nodes' values must be equal
    # 2. The left subtree of the first tree should be the mirror image of the right subtree of the second tree
    # 3. The right subtree of the first tree should be the mirror image of the left subtree of the second tree
    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            return (isMirror(root1.left, root2.right) and
                    isMirror(root1.right, root2.left))
    return False


# Test the code
# Create a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

if isMirror(root, root):
    print("The tree is a mirror of itself.")
else:
    print("The tree is not a mirror of itself.")
