MAX_INT = 2**31 - 1
MIN_INT = -(2**31)

class Solution:
    def reverse(self, x: int) -> int:
        if x < MIN_INT or x > MAX_INT:
            return 0

        values = []
        isNegative = x < 0
        x = abs(x)
        while x != 0:
            value = x % 10
            x = int(x / 10)
            values.append(value)

        ans = 0
        n = len(values) - 1
        for value in values:
            ans += value * (10**n)
            n -= 1

        if ans > MAX_INT:
            return 0

        return -ans if isNegative else ans


sol = Solution()
print(sol.reverse(123))
