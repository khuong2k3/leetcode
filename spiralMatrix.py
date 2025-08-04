
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        output = [[0 for _ in range(n)] for _ in range(n)]

        num = 1
        top, bottom, left, right = 0, n - 1, 0, n - 1

        while top <= bottom and left <= right:
            # Go right
            for col in range(left, right + 1):
                output[top][col] = num
                num += 1
            top += 1

            # Go down
            for row in range(top, bottom + 1):
                output[row][right] = num
                num += 1
            right -= 1

            # Go left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    output[bottom][col] = num
                    num += 1
                bottom -= 1

            # Go up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    output[row][left] = num
                    num += 1
                left += 1

        return output

sol = Solution()
print(sol.generateMatrix(4))

