

def rob(nums: list[int]) -> int:
    moneys = [0] * (len(nums) + 1)
    moneys[1] = nums[0]

    for i in range(1, len(nums)):
        moneys[i+1] = max(moneys[i - 1] + nums[i], moneys[i])

    return moneys[len(nums)]

class Solution:
    def rob(self, nums: list[int]) -> int:
        if (len(nums) <= 3):
            return max(nums)

        return max(rob(nums[0:-1]), rob(nums[1:]))


sol = Solution()

print(sol.rob([2,3,2]))
print(sol.rob([1,2,3,1]))




