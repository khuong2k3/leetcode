from linkListLeetCode import ListNode, fromArrayWithCycle

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False

    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if fast is None or fast.next is None:
            return None

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow 

sol = Solution()

print(sol.detectCycle(fromArrayWithCycle([3,2,0,-4], 1)))



