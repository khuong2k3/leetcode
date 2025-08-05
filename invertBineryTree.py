

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        stacks = [root]

        while len(stacks) != 0:
            currentNode = stacks.pop()

            tempNode = currentNode.left
            currentNode.left = currentNode.right
            currentNode.right = tempNode

            if currentNode.left is not None:
                stacks.append(currentNode.left)

            if currentNode.right is not None:
                stacks.append(currentNode.right)

        return root


