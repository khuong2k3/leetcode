
MAX_INT =  2**31 - 1

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [MAX_INT] * (amount + 1)
        coins = sorted(coins)
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if coin > i:
                    break
                dp[i] = min(dp[i], dp[i - coin]+1)

        return dp[-1] if dp[-1] != MAX_INT else -1

sol = Solution()
print(
    sol.coinChange([1,2,5], 11)
)

