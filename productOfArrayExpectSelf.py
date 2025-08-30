class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = [1] * len(nums)
        # right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]

        
        right = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            left[i] *= right
            right *= nums[i]

        return left


sol = Solution()
print(sol.productExceptSelf([2, 3, 4, 5, 6]))
print(sol.productExceptSelf([1,2,3,4]))
