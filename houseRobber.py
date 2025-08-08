
class Solution:
    def rob(self, nums: list[int]) -> int:
        moneys = [0] * (len(nums) + 1)
        moneys[1] = nums[0]

        for i in range(1, len(nums)):
            moneys[i+1] = max(moneys[i - 1] + nums[i], moneys[i])

        return moneys[len(nums)]


nums = [1,2,3,1]

sol = Solution()
print(sol.rob(nums))
