

# Definition for a binary tree node.
from typing_extensions import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        stacks: list[tuple[TreeNode, int]] = []
        if root is not None:
            stacks.append((root, root.val))

        while len(stacks) != 0:
            currentNode, val = stacks.pop()

            if currentNode.left is None and currentNode.right is None and val == targetSum:
                return True

            if currentNode.left is not None:
                stacks.append((currentNode.left, val + currentNode.left.val))

            if currentNode.right is not None:
                stacks.append((currentNode.right, val + currentNode.right.val))

        return False

