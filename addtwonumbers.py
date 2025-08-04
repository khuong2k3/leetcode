

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listIter(node):
    currentNode = node
    yield node.val
    while currentNode.next is not None:
        currentNode = currentNode.next
        yield currentNode.val

def toListNode(array):
    outputs = ListNode(array[0])
    currentOut = outputs
    for ele in array[1:]:
        currentOut.next = ListNode(ele)
        currentOut = currentOut.next

    return outputs

def zipDefault(iter1, iter2, default):
    a = next(iter1, None)
    b = next(iter2, None)

    while a is not None or b is not None:
        if a is not None and b is not None:
            yield a, b
        elif a is None:
            yield default, b
        else:
            yield a, default
        a = next(iter1, None)
        b = next(iter2, None)


def addDig(a, b, carry):
    out = a + b + carry
    carry = 0
    if out > 9:
        carry = 1 
        out -= 10
    return out, carry

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        iterL1 = listIter(l1)
        iterL2 = listIter(l2)
        iterLR = zipDefault(iterL1, iterL2, 0)

        a, b = next(iterLR) 
        out, carry = addDig(a, b, 0)

        outputs = ListNode(out)
        currentOutput = outputs

        for a, b in iterLR:
            out, carry = addDig(a, b, carry)
            currentOutput.next = ListNode(out)
            currentOutput = currentOutput.next

        if carry > 0:
            currentOutput.next = ListNode(carry)
            currentOutput = currentOutput.next

        return outputs



# [9,9,9,9,9,9,9]
# [9,9,9,9]
# [8,9,9,9,0,0,0,1] 

