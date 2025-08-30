from typing import Self

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Self | None = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head

        while current is not None:
            newNext = current.next
            current.next = prev
            prev = current
            current = newNext

        return prev 


sol = Solution()
a = sol.reverseList(ListNode(1, ListNode(2, ListNode(3))))
while a is not None:
    print(a.val)
    a = a.next


