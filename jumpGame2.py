
class Solution:
    def jump(self, nums: list[int]) -> int:
        for i, n in enumerate(nums[1:], 1):
            nums[i] = max(nums[i-1], n + i)

        index = 0
        jumpCount = 0
        while index < len(nums) - 1:
            jumpCount += 1
            index = nums[index]

        return jumpCount


sol = Solution()

test1 = [2,3,1,1,4]
test2 = [2,3,1]

print(
    sol.jump(test1)
)
