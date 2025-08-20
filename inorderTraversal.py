from typing import Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        def _backtract(root: TreeNode | None):
            if root is None:
                return
                
            _backtract(root.left)
            ans.append(root.val)
            _backtract(root.right)

        _backtract(root)

        return ans


sol = Solution()

root = TreeNode(1, TreeNode(1))

# sol.inorderTraversal()
