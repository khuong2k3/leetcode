
# Definition for singly-linked list.

from linkListLeetCode import ListNode, fromArray, printListNode


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

    def deleteDuplicates2(self, head: ListNode | None) -> ListNode | None:
        newHead = ListNode(0, head)
        prev = newHead
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                while current.next is not None and current.next.val == current.val:
                    current.next = current.next.next

                prev.next = current.next
            else:
                prev = prev.next

            current = current.next

        return newHead.next


sol = Solution()

head = sol.deleteDuplicates2(fromArray([2,3,3,4,5,5,6,6]))
printListNode(head)





