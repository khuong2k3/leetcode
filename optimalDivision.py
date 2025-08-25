
class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        n = len(nums)
        if n == 0:
            return ""
        elif n == 1:
            return str(nums[0])
        elif n == 2:
            return f'{nums[0]}/{nums[1]}'

        return ''


sol = Solution()
print(
    sol.optimalDivision([1000,100,10,2])
)


