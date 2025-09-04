from treeLeetCode import Node


class Solution:
    def postorder(self, root) -> list[int]:
        ans = []

        # def _backtract(root):
        #     if not root:
        #         return
        #
        #     if root.children:
        #         for node in root.children:
        #             _backtract(node)
        #
        #     ans.append(root.val)
        #
        # _backtract(root)

        if not root:
            return []

        stack1 = [root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)

            if node.children:
                for node in node.children:
                    stack1.append(node)


        while stack2: 
            ans.append(stack2.pop())
            
        return ans 
