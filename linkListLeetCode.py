from typing import Self

class ListNode:
    def __init__(self, val: int=0, next: Self | None = None):
        self.val: int = val
        self.next: Self | None = next



def fromArray(arr: list[int]) -> ListNode | None:
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head

def printListNode(head: ListNode | None):
    ans = "["
    current = head
    while current is not None:
        ans += f'{current.val}, '
        current = current.next

    ans += ']' 
    print(ans)

