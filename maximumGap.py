
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        nums = sorted(nums)
        maxGap = 0
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i-1]
            if gap > maxGap:
                maxGap = gap

        return maxGap

