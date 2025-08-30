
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        n2 = 2 * n
        def _bactract(current: list[bool], close: int, open: int):
            if close + open == n2: 
                result.append("".join(map(lambda x: '(' if x else ')', current)))
                return

            if close < n:
                current.append(True)
                _bactract(current, close + 1, open)
                _ = current.pop()


            if open < n and close > open:
                current.append(False)
                _bactract(current, close, open + 1)
                _ = current.pop()

        _bactract([], 0, 0)
        return result

sol = Solution()
print(
    sol.generateParenthesis(3)
)
