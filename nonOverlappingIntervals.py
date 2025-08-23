class Solution:
    def overlaping(self, a: list[int], b: list[int]) -> bool:
        return a[0] < b[1] and b[0] < a[1]

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        ans = -1

        r = intervals[0]
        for interval in intervals:
            if self.overlaping(r, interval):
                if r[1] > interval[1]:
                    r = interval

                ans += 1

            if r[1] <= interval[0]:
                r = interval

        return ans


sol = Solution()

print(
    sol.eraseOverlapIntervals(
        [
            [-98, 15],
            [-88, 45],
            [-83, -23],
            [-71, 60],
            [-65, 40],
            [-64, 17],
            [-59, -50],
            [-58, 98],
            [-57, 81],
            [-49, 81],
            [-17, 5],
            [-16, 90],
            [-2, 85],
            [27, 50],
            [36, 97],
            [50, 57],
            [54, 88],
            [59, 68],
            [73, 78],
            [76, 96],
            [76, 78],
            [78, 99],
            [81, 97],
            [83, 84],
            [85, 90],
            [86, 100],
        ]
    )
)
