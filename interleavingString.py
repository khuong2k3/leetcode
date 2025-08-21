class Solution:
    def _interleaveDp(self, s1: str, s2: str, s3: str) -> list[list[bool]]:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len1 + len2 != len3:
            return [[False]]

        dp = [[False] * (len1 + 1) for _ in range(len2 + 1)]
        dp[0][0] = True
        for j in range(0, len1):
            if dp[0][j] and s1[j] == s3[j]:
                dp[0][j + 1] = True
            else:
                break

        for i in range(0, len2):
            if dp[i][0] and s2[i] == s3[i]:
                dp[i + 1][0] = True
            else:
                break

        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                dp[i][j] = (dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]
                )
        return dp

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = self._interleaveDp(s1, s2, s3)

        return dp[-1][-1]

    def waysInterleave(self, s1: str, s2: str, s3: str) -> int:
        dp = self._interleaveDp(s1, s2, s3)

        return self.uniquePathsWithObstacles(dp)
        
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[bool]]) -> int:
        dp = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0]:
            dp[0][1] = 1

        for i, obs in enumerate(obstacleGrid[0][1:], 2):
            if obs:
                dp[0][i] = dp[0][i-1]

        for i in range(1, len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    dp[i][j+1] = dp[i][j] + dp[i-1][j+1]

        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])]

sol = Solution()

print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(sol.waysInterleave("aabcc", "dbbca", "aadbbcbcac"))
