# class Solution:
#     def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
#         lr = grid.copy()
#
#         for i in range(1, len(lr)):
#             for j in range(1, len(lr[i])):
#                 lr[i][j] += lr[i - 1][j - 1]
#
#         rl = grid.copy()
#         for i in range(1, len(lr)):
#             for j in range(len(lr[i])-1):
#                 rl[i][j] += rl[i - 1][j + 1]
#
#         ans = 0
#         # for j in range(len(grid)):
#         #     vShape = lr[-1][j] + rl[-1][j] - grid[-1][j]
#         #     if vShape > ans:
#         #         ans = vShape
#         #
#         # bottoml = [1] * (len(grid[0]) + 1)
#         # bottomr = [1] * (len(grid[0]) + 1)
#         #
#         # bottoml[1:] = grid[-1]
#         # bottomr[:-1] = grid[-1]
#
#         for i in reversed(range(len(grid)-1)):
#             for j in range(len(grid)):
#                 vShape = lr[i][j] + rl[i][j] - grid[-1][j]
#                 if vShape > ans:
#                     ans = vShape
#
#         return ans

class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n == 0 or m == 0:
            return 0
        
        # dp[r][c][dir][turn] stores the length of the segment ending at (r, c)
        # dir: 0-TL, 1-TR, 2-BL, 3-BR
        # turn: 0-no turn, 1-one turn
        dp = [[[[0] * 2 for _ in range(4)] for _ in range(m)] for _ in range(n)]
        
        dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # TL, TR, BL, BR
        dir_map_clockwise = {
            (-1, -1): (-1, 1),
            (-1, 1): (1, 1),
            (1, 1): (1, -1),
            (1, -1): (-1, -1)
        }
        
        max_len = 0
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    max_len = max(max_len, 1)
                    for i in range(4):
                        dp[r][c][i][0] = 1
                
                # Check previous cells to extend segments
                for i in range(4):
                    dr, dc = dirs[i]
                    pr, pc = r - dr, c - dc
                    
                    if 0 <= pr < n and 0 <= pc < m:
                        # Case 1: Continue a straight segment
                        if dp[pr][pc][i][0] > 0:
                            expected = 2 if (dp[pr][pc][i][0] + 1) % 2 == 0 else 0
                            if grid[r][c] == expected:
                                dp[r][c][i][0] = dp[pr][pc][i][0] + 1
                                max_len = max(max_len, dp[r][c][i][0])
                        
                        # Case 2: Continue a turned segment
                        if dp[pr][pc][i][1] > 0:
                            expected = 2 if (dp[pr][pc][i][1] + 1) % 2 == 0 else 0
                            if grid[r][c] == expected:
                                dp[r][c][i][1] = dp[pr][pc][i][1] + 1
                                max_len = max(max_len, dp[r][c][i][1])
                        
                        # Case 3: Make a clockwise turn
                        if dp[pr][pc][i][0] > 0 and grid[pr][pc] == 2:
                            new_dr, new_dc = dir_map_clockwise[dirs[i]]
                            new_dir_idx = dirs.index((new_dr, new_dc))
                            
                            if grid[r][c] == 0:
                                current_len = dp[pr][pc][i][0] + 1
                                dp[r][c][new_dir_idx][1] = max(dp[r][c][new_dir_idx][1], current_len)
                                max_len = max(max_len, dp[r][c][new_dir_idx][1])
        
        return max_len


sol = Solution()
print(
    sol.lenOfVDiagonal(
        [
            [2, 2, 1, 2, 2],
            [2, 0, 2, 2, 0],
            [2, 0, 1, 1, 0],
            [1, 0, 2, 2, 2],
            [2, 0, 0, 2, 2],
        ]
    )
)

