
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minNum = prices[0]
        ans = 0

        for price in prices[1:]:
            ans = max(price - minNum, ans)

            if price < minNum:
                minNum = price

        return ans


sol = Solution()

print(
    sol.maxProfit([7,1,5,3,6,4])
)
