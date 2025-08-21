from math import ceil, log2

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        elif n == 3:
            return 2
        dp = [1] * (n + 1)

        dp[2] = 2 
        dp[3] = 3
        for i in range(4, n + 1):
            logI = int(log2(i))
            for div in range(logI, logI+2):
                mf = int(i / div)
                mc = ceil(i / div)

                dp[i] = max(
                    dp[i - mf] * dp[mf],
                    dp[i - mc] * dp[mc],
                    dp[i],
                )

        print(dp)
        return dp[n]


sol = Solution()

# print(sol.integerBreak(7))
# print(sol.integerBreak(8))
# print(sol.integerBreak(9))
print(sol.integerBreak(20))
