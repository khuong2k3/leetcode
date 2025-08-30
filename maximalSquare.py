class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        dp = [
            [int(matrix[i][j]) for j in range(len(matrix[i]))]
            for i in range(len(matrix))
        ]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if dp[i][j] == 0:
                    continue

                dp[i][j] = 1 + min(
                    dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]
                )

        maxEdge = max(map(lambda x: max(x), dp))

        return maxEdge * maxEdge




sol = Solution()

print(
    sol.maximalSquare(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "1"],
        ]
    )
)
