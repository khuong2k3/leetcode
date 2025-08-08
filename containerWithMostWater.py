
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        maxA = 0

        while left < right:
            area = 0
            width = right - left
            if height[left] < height[right]:
                area = width * height[left]
                left += 1
            else:
                area = width * height[right]
                right -= 1

            maxA = max(maxA, area)

        return maxA


sol = Solution()

height1 = [1,8,6,2,5,4,8,3,7]

print(
    sol.maxArea(height1)
)
