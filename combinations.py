# 1, 2, 3, 4


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        output = []
        def _combine(i: int, chosed: int, ans: list[int]):
            if i == k:
                output.append(ans.copy())
                return

            for c in range(chosed, n + 1):
                ans.append(c)
                _combine(i+1, c+1, ans)
                ans.pop()

        _combine(0, 1, [])
        return output

