from itertools import chain

class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)

        digs = [[0] * i for i in chain(range(1, n), range(n, 0, -1))]

        for i, length in enumerate(range(1, n + 1)):
            col = n - length
            row = 0
            for j in range(len(digs[i])):
                digs[i][j] = grid[row][col]
                row += 1
                col += 1

        for i, length in enumerate(range(n - 1, 0, -1), n):
            col = 0
            row = n - length

            for j in range(len(digs[i])):
                digs[i][j] = grid[row][col]
                row += 1
                col += 1

        for i in range(n-1):
            list.sort(digs[i])

        for i in range(n-1, len(digs)):
            list.sort(digs[i], reverse=True)

        ans = grid.copy()
        for i, length in enumerate(range(1, n + 1)):
            col = n - length
            row = 0
            for j in range(len(digs[i])):
                ans[row][col] = digs[i][j]
                row += 1
                col += 1

        for i, length in enumerate(range(n - 1, 0, -1), n):
            col = 0
            row = n - length

            for j in range(len(digs[i])):
                ans[row][col] = digs[i][j]
                row += 1
                col += 1

        return ans


sol = Solution()
print(sol.sortMatrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]]))
