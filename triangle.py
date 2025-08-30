
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[10**5] * (len(triangle[i]) + 2) for i in range(len(triangle))]
        dp[0][1] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                dp[i][j+1] = triangle[i][j] + min(
                    dp[i-1][j],
                    dp[i-1][j+1]
                )

        return min(dp[-1])

    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1] * i for i in range(1, numRows+1)]

        for i in range(numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]

        return ans
        
    def getRow(self, rowIndex: int) -> list[int]:
        prev = [1] * rowIndex
        current = [1] * (rowIndex+1)

        for i in range(rowIndex+1):
            for j in range(1, i):
                current[j] = prev[j] + prev[j-1]

            prev[:i] = current[:i]

        return current



sol = Solution()

# triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
# triangle2 = [[-1],[2,3],[1,-1,-3]]
#
# print(sol.minimumTotal(triangle1))
# print(sol.minimumTotal(triangle2))

# print(sol.generate(3))
print(sol.getRow(3))
