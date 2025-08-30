
MAX_INT = 2 ** 31
MIN_INT = 2 ** 31 - 1

class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        idx = 0
        n = len(s)
        while idx < n and s[idx] == ' ':
            idx += 1
        isNegative = False
        if idx >= n:
            return 0
        if s[idx] == '-':
            isNegative = True
            idx += 1
        elif s[idx] == '+':
            idx += 1

        while idx < n and s[idx] >= '0' and s[idx] <= '9':
            ans *= 10
            ans += ord(s[idx]) - 48
            idx += 1

        if ans > MAX_INT:
            ans = MAX_INT

        return -ans if isNegative else ans


sol = Solution()
print(
    sol.myAtoi("-042")
)
# print(ord('0') - 48)
