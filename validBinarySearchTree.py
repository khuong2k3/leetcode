from collections import deque
from treeLeetCode import TreeNode

class Solution:
    # def isValidBST(self, root: TreeNode | None) -> bool:
    #     def order(root: TreeNode | None, left: TreeNode | None, right: TreeNode | None) -> bool:
    #         if root is None:
    #             return True
    #
    #         leftTrav = order(root.left, left, root)
    #         if left is not None and left.val >= root.val:
    #             return False
    #
    #         if right is not None and right.val <= root.val:
    #             return False
    #
    #         rightTrav = order(root.right, root, right)
    #
    #         return leftTrav and rightTrav
    #
    #     return order(root, None, None)

    def isValidBST(self, root: TreeNode | None) -> bool:
        current = root
        stack = []
        arr = deque()

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            arr.append(current)
            if len(arr) > 1:
                if arr[0].val >= arr[1].val:
                    return False
                arr.popleft()

            current = current.right

        return True


sol = Solution()
print(sol.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
print(sol.isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))))
#      5
#   4     6
#       3   7
