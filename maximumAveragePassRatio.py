import heapq


def diff(clss: list[int]):
    return float(clss[0]) / clss[1] - float(clss[0] + 1) / (clss[1] + 1)


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        ratioes = [(diff(clss), i) for i, clss in enumerate(classes)]
        heapq.heapify(ratioes)

        for _ in range(extraStudents):
            _, idx = heapq.heappop(ratioes)
            classes[idx][0] += 1
            classes[idx][1] += 1

            heapq.heappush(ratioes, (diff(classes[idx]), idx))

        return sum(map(lambda cl: float(cl[0]) / cl[1], classes)) / len(classes)


sol = Solution()
print(sol.maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2))
