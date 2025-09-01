
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        writeIdx = 1

        for i in range(1, n):
            if nums[i-1] != nums[i]:
                nums[writeIdx] = nums[i]
                writeIdx += 1

        return writeIdx

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
