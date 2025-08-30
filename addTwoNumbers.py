from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Self | None = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        head = ListNode(0)

        current = head
        carry = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + carry
            if val > 9:
                carry = 1
                val -= 10
            else:
                carry = 0

            current.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            current = current.next

        for ln in [l1, l2]:
            while ln is not None:
                val = ln.val + carry
                if val > 9:
                    carry = 1
                    val -= 10
                else:
                    carry = 0

                current.next = ListNode(val)
                ln = ln.next
                current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return head.next
