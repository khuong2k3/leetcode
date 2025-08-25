MIN_INT = -(2**31)

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        mid = int((right + left) // 2)

        while (mid == left or mid == right) and left < right:
            if nums[mid] < (nums[mid + 1] if mid + 1 < n else MIN_INT):
                left = mid
            else:
                right = mid

            mid = int((right + left) // 2)

        return right if nums[right] > nums[left] else left

sol = Solution()
print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(sol.findPeakElement([2, 1]))
