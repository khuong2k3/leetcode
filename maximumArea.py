
class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        maxDig = 0
        ans = 0

        for dim in dimensions:
            dig = dim[0] ** 2  + dim[1] ** 2

            if dig > maxDig:
                maxDig = dig
                ans = dim[0] * dim[1]
            elif dig == maxDig:
                area = dim[0] * dim[1]
                if area > ans:
                    ans = area

        return ans

