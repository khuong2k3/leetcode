class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ans = 0
        n = len(nums)
        right = n - 1

        while right >= 0 and nums[right] == val:
            right -= 1
            ans += 1

        for idx in range(n-1, -1, -1):
            if right >= idx and nums[idx] == val:
                nums[idx] = nums[right]
                nums[right] = val
                while right >= 0 and nums[right] == val:
                    ans += 1
                    right -= 1
                
        return n - ans 


sol = Solution()
# print(sol.removeElement([0,1,2,2,3,0,4,2], 2))
# print(sol.removeElement([2,2,3], 2))
print(sol.removeElement([4,2,0,2,2,1,4,4,1,4,3,2], 4))
