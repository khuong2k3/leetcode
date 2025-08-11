class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minNum = prices[0] 

        profit = 0
        for price in prices:
            if minNum < price:
                profit += price - minNum

            minNum = price

        return profit


sol = Solution()

print(sol.maxProfit([7, 1, 5, 3, 6, 4]))


print(sol.maxProfit([1, 2, 3, 4, 5]))
