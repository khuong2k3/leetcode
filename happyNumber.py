
class Solution:

    def isHappy(self, n: int) -> bool:
        def nextNum(n: int) -> int:
            s = 0
            while n != 0:
                s += (n%10)**2
                n = int(n/10)
            return s

        slow = nextNum(n)
        fast = nextNum(slow)

        while slow != fast:
            if fast == 1:
                return True
            slow = nextNum(slow)
            fast = nextNum(nextNum(fast))

        return slow == 1 


    def _isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        searchDict = set()
        searchDict.add(n)

        while n != 1:
            s = 0
            while n != 0:
                s += (n%10)**2
                n = int(n/10)
            n = s
            if n in searchDict:
                return False
            searchDict.add(n)

        return True

sol = Solution()
print(
    sol.isHappy(1)
)

