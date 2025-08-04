from math import ceil, floor

# k       n
# h     i g
# u   d
# o g
# n

# k     d
# h   g i
# u n   n
# o     g

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        readIdx = 0
        width = ceil(len(s) / numRows)
        # colGap = max(0, numRows - 2)

        # read col
        colIdx = 0
        while colIdx < width:
            rowIdx = 0
            while rowIdx < numRows:
                readIdx = rowIdx * width + colIdx # -1 for last element
                # print(rowIdx, colIdx)
                if readIdx >= len(s):
                    break
                ans += s[readIdx]
                rowIdx += 1

            rowIdx = numRows - 2
            colIdx += 1
            while rowIdx > 0 :
                # print(rowIdx, colIdx)
                readIdx = rowIdx * width + colIdx
                if readIdx < len(s):
                    ans += s[readIdx]
                colIdx += 1
                rowIdx -= 1

        return ans

sol = Solution()
print( sol.convert("""
k   
h gd
un ig
o  n
"""[1:], 4))
