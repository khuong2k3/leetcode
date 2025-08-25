def propagate(
    board: list[list[str]], visited: list[list[bool]], start: tuple[int, int]
) -> bool:
    n, m = len(board), len(board[0])

    ans = [False]

    def _backtract(start: tuple[int, int]):
        if start[0] >= n or start[1] >= m or start[0] < 0 or start[1] < 0:
            return

        if board[start[0]][start[1]] == "0" or visited[start[0]][start[1]]:
            return

        visited[start[0]][start[1]] = True
        # ans.append(start)
        ans[0] = True

        # right
        _backtract((start[0], start[1] + 1))
        # left
        _backtract((start[0], start[1] - 1))
        # up
        _backtract((start[0] - 1, start[1]))
        # down
        _backtract((start[0] + 1, start[1]))

    _backtract(start)

    return ans[0]


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        ans = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    if propagate(grid, visited, (i, j)):
                        ans += 1

        return ans


sol = Solution()

print(
    sol.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
