
from treeLeetCode import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        if not root:
            return []

        stack: list[TreeNode] = [root]

        while stack:
            current = stack.pop()
            ans.append(current.val)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)


        return ans

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        ans = []
        current = root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            ans.append(current.val)

            current = current.right

        return ans

    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return [] 
        ans = []

        stack1 = [root]
        stack2 = []
        while stack1:
            current = stack1.pop()
            stack2.append(current.val)

            if current.left:
                stack1.append(current.left)

            if current.right:
                stack1.append(current.right)

        while stack2:
            ans.append(stack2.pop())

        return ans

sol = Solution()
print(
    sol.postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3))))
)
        

