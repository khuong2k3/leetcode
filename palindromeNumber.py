
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = str(x)
        n = len(num)
        left = n >> 1
        right = left
        if len(num) & 1 == 0:
            left -= 1

        while left >= 0 and right < n:
            if num[left] != num[right]:
                return False
            left -= 1
            right += 1

        return True

sol = Solution()
print(
    sol.isPalindrome(12222)
)
