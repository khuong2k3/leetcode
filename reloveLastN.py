# Definition for singly-linked list.
from typing import Self


class ListNode:
    def __init__(self, val: int=0, next: Self | None=None):
        self.val: int = val
        self.next: Self | None = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        currentNode = head
        nLastNode = head
        if head is None:
            return None

        index = 0
        while currentNode is not None:
            if index > n:
                nLastNode = nLastNode.next

            currentNode = currentNode.next 
            index += 1

        otherhalf = None
        if nLastNode.next is not None:
            otherhalf = nLastNode.next
            nLastNode.next = nLastNode.next.next
        else:
            otherhalf = nLastNode.next
            nLastNode.next = None

        if index == n:
            return otherhalf 

        return head 

test1 = ListNode(1, ListNode(2))
test4 = ListNode(1, ListNode(2))
test2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
test3 = ListNode(1)

# 1
# [1, 2]
sol = Solution()

def printList(head: ListNode | None):
    currentNode = head
    ans = ""
    while currentNode is not None:
        ans += f'{currentNode.val},'
        currentNode = currentNode.next
    print(ans)

printList(
    sol.removeNthFromEnd(test1, 1)
)

printList(
    sol.removeNthFromEnd(test2, 2)
)

printList(
    sol.removeNthFromEnd(test3, 1)
)

printList(
    sol.removeNthFromEnd(test4, 2)
)
