from typing import Self

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is None or root.right is None:
            return False

        lStack: list[None | TreeNode] = [root.left]
        rStack: list[None | TreeNode] = [root.right]

        while len(lStack) != 0 or len(rStack) != 0:
            left = lStack.pop()
            right = rStack.pop()

            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False

            if left.val != right.val:
                return False

            lStack.append(left.left)
            lStack.append(left.right)
            rStack.append(right.right)
            rStack.append(right.left)

        return True

sol = Solution()

tree = TreeNode(1, TreeNode(2), TreeNode(2))

print(
    sol.isSymmetric(tree)
)


