
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m = m - 1
        n = n - 1

        ans = 1
        maxN = max(m, n)
        minN = min(m, n)
        for i in range(maxN+1, m + n + 1):
            ans *= i

        for i in range(2, minN + 1):
            ans /= i

        return int(ans)


sol = Solution()

print(
    sol.uniquePaths(3, 7)
)
