from typing_extensions import Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []

        def _bactrack(root: TreeNode | None, path: list[int], sum: int):
            if root.left is None and root.right is None:
                if sum == targetSum:
                    ans.append(path.copy())

                return

            if root.left is not None:
                path.append(root.left.val)
                _bactrack(root.left, path, sum + root.left.val)
                path.pop()

            if root.right is not None:
                path.append(root.right.val)
                _bactrack(root.right, path, sum + root.right.val)
                path.pop()

        if root is not None:
            _bactrack(root, [root.val], root.val)

        return ans


sol = Solution()

test1 = TreeNode(0, TreeNode(3), TreeNode(4))

print(
    sol.pathSum(test1, 3)
)

