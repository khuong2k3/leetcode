class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        list.sort(nums)
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n

        maxI = 0
        maxValue = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > maxValue:
                maxI = i
                maxValue = dp[i]

        ans = []
        while maxI >= 0:
            ans.append(nums[maxI])
            maxI = prev[maxI]

        return ans


sol = Solution()
# print(sol.largestDivisibleSubset([1, 2, 4, 6, 8, 20]))
# print(sol.largestDivisibleSubset([1, 2]))
# print(sol.largestDivisibleSubset([4,8,10,240]))
print(sol.largestDivisibleSubset([3,4,6,8,12,16,32]))

