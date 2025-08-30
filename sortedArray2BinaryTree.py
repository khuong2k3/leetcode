from typing import Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Self | None = left
        self.right: Self | None = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        n = len(nums)
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(nums[0])

        mid = int(n / 2)

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

sol = Solution()
print(sol.sortedArrayToBST([-10,-3,0,5,9]))

