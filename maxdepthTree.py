
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def _maxDepth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    return 1 + max(_maxDepth(root.left), _maxDepth(root.right))

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        stacks = [(root, 1)]
        ans = 0
        while len(stacks) != 0:
            node, depth = stacks.pop()
            ans = max(depth, ans)

            depth = depth + 1
            if node.left is not None:
                stacks.append((node.left, depth))

            if node.right is not None:
                stacks.append((node.right, depth))
        return ans

sol = Solution()

test1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

print(
    sol.maxDepth(test1)
)
