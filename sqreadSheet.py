class Spreadsheet:
    def __init__(self, rows: int):
        self.sheet: list[list[int]] = [[0] * 26 for _ in range(rows)]

    def _col_row(self, cell: str) -> tuple[int, int]:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        return col, row

    def setCell(self, cell: str, value: int) -> None:
        col, row = self._col_row(cell)

        self.sheet[row][col] = value

    def getCell(self, cell: str):
        col, row = self._col_row(cell)
        return self.sheet[row][col]

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        valueA = self.getCell(a) if a[0] >= "A" and a[0] <= "Z" else int(a)
        valueB = self.getCell(b) if b[0] >= "A" and b[0] <= "Z" else int(b)

        return valueA + valueB
