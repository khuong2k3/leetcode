from typing import Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        ans = []
        path = []

        def dfs(root: TreeNode | None):
            if root is None:
                return
            else:
                path.append(str(root.val))

            if root.left is None and root.right is None:
                ans.append("->".join(path))

            dfs(root.left)
            if root.left is not None:
                path.pop()

            dfs(root.right)
            if root.right is not None:
                path.pop()

        dfs(root)

        return ans


sol = Solution()
print(
    sol.binaryTreePaths(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)))
)
