
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        for i, num in enumerate(nums):
            ans ^= num
            ans ^= i 
        ans ^= n

        return ans
        # numsSum = sum(nums)
        # return int((n + 1) * n / 2) - numsSum

sol = Solution()
print(
    sol.missingNumber( [3,0,1])
)

