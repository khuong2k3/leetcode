from typing import Self


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is not None and q is not None:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(
                    p.right, q.right
                )
        elif p is None and q is None:
            return True

        return False


sol = Solution()

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

print(sol.isSameTree(p, q))
