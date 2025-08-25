from collections import deque

def propagate(board: list[list[str]], visited: list[list[bool]], start: tuple[int, int]) -> list[tuple[int, int]]:
    n, m = len(board), len(board[0])

    ans = []
    def _backtract(start: tuple[int, int]) -> bool:
        if (
            start[0] >= n
            or start[1] >= m
            or start[0] < 0
            or start[1] < 0
        ):
            return False

        if (
            board[start[0]][start[1]] == "X"
            or visited[start[0]][start[1]]
        ):
            return True

        visited[start[0]][start[1]] = True
        ans.append(start)

        # move right
        right = _backtract((start[0], start[1] + 1))
        # move left
        left = _backtract((start[0], start[1] - 1))
        # move up
        up = _backtract((start[0] - 1, start[1]))
        # move down
        down = _backtract((start[0] + 1, start[1]))
        return right and left and up and down

    if not _backtract(start):
        return []
    return ans


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        v = [False] * m
        visited = [v.copy() for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    for moved in propagate(board, visited, (i, j)):
                        print(moved)
                        board[moved[0]][moved[1]] = 'X'


sol = Solution()

board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

sol.solve(board)
print(board)



class Solution2:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        
        # Helper function for BFS traversal to find all 'O's connected to the border.
        # It marks these 'O's as a temporary character (e.g., '#') to protect them from being flipped.
        def bfs_and_mark_safe(r, c):
            if board[r][c] == 'O':
                q = deque([(r, c)])
                board[r][c] = '#'
                
                while q:
                    row, col = q.popleft()
                    
                    # Check all four neighbors
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = row + dr, col + dc
                        
                        # Check if the neighbor is within bounds and is an 'O'
                        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                            board[nr][nc] = '#'
                            q.append((nr, nc))

        # 1. Start BFS from all 'O's on the border (first and last rows/columns).
        # These are the 'O's that should not be flipped.
        
        # Top and bottom borders
        for c in range(cols):
            if board[0][c] == 'O':
                bfs_and_mark_safe(0, c)
            if board[rows - 1][c] == 'O':
                bfs_and_mark_safe(rows - 1, c)

        # Left and right borders
        for r in range(rows):
            if board[r][0] == 'O':
                bfs_and_mark_safe(r, 0)
            if board[r][cols - 1] == 'O':
                bfs_and_mark_safe(r, cols - 1)

        # 2. Iterate through the entire board and flip the cells.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    # 'O's that were not reached by BFS from the border are surrounded.
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    # 'O's that were reached by BFS are "safe" and should be restored.
                    board[r][c] = 'O'

