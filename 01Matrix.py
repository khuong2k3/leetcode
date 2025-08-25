MAX_INT = 10**5

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        n, m = len(mat), len(mat[0])
        dist = [mat[i].copy() for i in range(n)]

        for ri in [range(n), reversed(range(n))]:
            for rj in [range(m), reversed(range(m))]:
                for i in ri:
                    for j in rj:
                        if dist[i][j] == 0:
                            continue

                        d = min(
                            dist[i][j - 1] if j > 0 else MAX_INT,
                            dist[i][j + 1] if j < m - 1 else MAX_INT,
                            dist[i - 1][j] if i > 0 else MAX_INT,
                            dist[i + 1][j] if i < n - 1 else MAX_INT,
                            dist[i][j],
                        )

                        dist[i][j] = d + 1

        return dist


sol = Solution()
print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
