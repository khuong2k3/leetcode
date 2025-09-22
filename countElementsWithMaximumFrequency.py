from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        ans = 0
        maxValue = 0
        for value in Counter(nums).values():
            if maxValue < value:
                maxValue = value
                ans = value
            elif maxValue == value:
                ans += value

        return ans


sol = Solution()
print(sol.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
