from itertools import chain, product

SOLVED_CELL = [(1 << 10) - 2] * 9


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # use 1d array as 2d array
        row, col, cell = [0] * 9, [0] * 9, [0] * 9

        for i, j in product(range(9), repeat=2):
            if board[i][j] != ".":
                mask = 1 << int(board[i][j])
                k = (i // 3) * 3 + j // 3

                if mask & row[i] or mask & col[j] or mask & cell[k]:
                    return False

                # act as a fast for loop
                row[i] |= mask
                col[j] |= mask
                cell[k] |= mask

        return True

    # def _solvedSudoku(self, col: list[int], row: list[int], cell: list[int]) -> bool:
    #     for mask in [col, row, cell]:
    #         if mask != SOLVED_CELL:
    #             return False
    #
    #     return True

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        boardInt = [[-1 if cell == "." else int(cell) for cell in row] for row in board]
        row, col, cell = [0] * 9, [0] * 9, [0] * 9
        for i, j in product(range(9), repeat=2):
            if boardInt[i][j] != -1:
                mask = 1 << boardInt[i][j]
                k = (i // 3) * 3 + j // 3

                # act as a fast for loop
                row[i] |= mask
                col[j] |= mask
                cell[k] |= mask

        def _backtract(i: int, j: int) -> bool:
            if j >= 9:
                j = 0
                i += 1

            while i != 9 and boardInt[i][j] != -1:
                j += 1
                if j >= 9:
                    j = 0
                    i += 1

            if i == 9:
                return True

            # for i, r in enumerate(chain([range(cIdx, 9)], [range(9)] * (rIdx - 1)), rIdx):
            #     for j in r:
            #         if boardInt[i][j] != -1:
            #             continue

            k = (i // 3) * 3 + j // 3
            for num in range(1, 10):
                mask = 1 << num
                if mask & row[i] or mask & col[j] or mask & cell[k]:
                    continue

                boardInt[i][j] = num

                row[i] |= mask
                col[j] |= mask
                cell[k] |= mask

                if _backtract(i, j + 1):
                    return True

                boardInt[i][j] = -1

                row[i] ^= mask
                col[j] ^= mask
                cell[k] ^= mask

            return False

        _ = _backtract(0, 0)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    board[i][j] = str(boardInt[i][j])
        print(board)



sol = Solution()
ans = 0
for i in range(1, 10):
    ans ^= 1 << i

# print(ans, (1 << 10) - 2)

print(
    sol.solveSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
