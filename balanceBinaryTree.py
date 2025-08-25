from typing import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def getHeight(node: TreeNode | None) -> int:
            if not node:
                return 0

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            if (
                leftHeight == -1
                or rightHeight == -1
                or abs(leftHeight - rightHeight) > 1
            ):
                return -1

            return 1 + max(leftHeight, rightHeight)

        return getHeight(root) != -1
