
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 0:
            dp[0][1] = 1

        for i, obs in enumerate(obstacleGrid[0][1:], 2):
            if obs == 0:
                dp[0][i] = dp[0][i-1]

        for i in range(1, len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    dp[i][j+1] = dp[i][j] + dp[i-1][j+1]

        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])]


sol = Solution()

print(
    sol.uniquePathsWithObstacles([
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
))

print(
    sol.uniquePathsWithObstacles(
        [[0,1],
         [0,0]]
    )
)

# [0,1,1,1],
# [0,1,2,3],
# [0,1,3,6]]
