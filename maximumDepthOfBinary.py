from typing import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
