class Solution:
    def sumZero(self, n: int) -> list[int]:
        ans = [0] * n

        left = (n - 1) >> 1
        right = left + 1

        count = 1
        if n & 1 == 1:
            left -= 1

        while left >= 0 and right < n:
            ans[left] = -count
            ans[right] = count
            count += 1
            left -= 1
            right += 1

        return ans


sol = Solution()

print(sol.sumZero(3))
print(sol.sumZero(2))
print(sol.sumZero(4))
print(sol.sumZero(5))
