
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxValue = max(nums)
        if maxValue < 0:
            return maxValue

        value = 0
        for num in nums:
            value += num
            if value < 0:
                value = 0

            if value > maxValue:
                maxValue = value

        return maxValue

sol = Solution()

print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        
