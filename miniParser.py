
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
import numbers


class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution:
    def parseNum(self, s: str, i: int) -> tuple[int, int]:
        num = 0
        numLen= 0
        for j in range(i, len(s)):
            if s[j] >= '0' and s[j] <= '9':
                num *= 10
                num += int(s[j])
                numLen += 1
            else:
                break
        return (num, numLen) if numLen > 0 else (0, 0)

    def deserialize(self, s: str) -> NestedInteger:
        def _bactract(idx: int) -> tuple[list | int, int]:
            if s[idx] == '[':
                arr = []
                j = 1 
                while j < len(s)-idx:
                    if s[idx+j] == ']':
                        j+=1
                        break
                    elif s[idx+j] == ',':
                        j += 1
                    else:
                        num, numLen = _bactract(idx+j)
                        arr.append(num)
                        j += numLen

                return (arr, j) 
            else:
                if s[idx] == '-':
                    num, numLen = self.parseNum(s, idx+1)
                    return (-num, numLen+1)
                else:
                    num, numLen = self.parseNum(s, idx)
                    return (num, numLen)

        value, _ = _bactract(0)

        return NestedInteger(value)



sol = Solution()

print(sol.deserialize("[123,456,[788,799,833],[[]],10,[]]"))
# print(sol.deserialize("[[123],[[]]]"))
