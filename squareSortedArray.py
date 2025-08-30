
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            squareRight = nums[right] * nums[right]
            squareLeft = nums[left] * nums[left]
            if squareRight > squareLeft:
                ans[i] = squareRight
                right -= 1
            else:
                ans[i] = squareLeft
                left += 1

        return ans

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
