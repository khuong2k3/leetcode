import sys

MIN_INT = -sys.maxsize - 1

class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        list.sort(points, key=lambda p: (p[0], -p[1]))
        n = len(points)
        

        ans = 0
        for i in range(n):
            _, y = points[i]
            lower = MIN_INT
            for j in range(i + 1, n):
                if lower < points[j][1] <= y:
                    ans += 1
                    lower = points[j][1]

                if lower == y:
                    break

        return ans


sol = Solution()
# print(sol.numberOfPairs([[1,1],[2,2],[3,3]]))
print(sol.numberOfPairs([[6, 2], [4, 4], [2, 6]]))
print(sol.numberOfPairs([[3, 1], [1, 3], [1, 1]]))
# print(sol.numberOfPairs([[0,0],[0,3]]))
# print(sol.numberOfPairs([[0,0],[2,5]]))
