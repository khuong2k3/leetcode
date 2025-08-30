class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        dp: list[list[str]] = [[] for _ in range(n)]

        for i in range(n):
            for mode in range(0, 2):
                left = i
                right = i + mode

                while left >= 0 and right < len(s):
                    if s[left] != s[right]:
                        break
                    else:
                        dp[left].append(s[left : right + 1])
                        left -= 1
                        right += 1

        ans = []

        def _backtract(idx: int, part: list[str]):
            if idx > n:
                return
            elif idx == n:
                ans.append(part.copy())
                return

            for pali in dp[idx]:
                part.append(pali)
                _backtract(idx + len(pali), part)
                _ = part.pop()

        _backtract(0, [])
        return ans

    def minCut(self, s: str) -> int:
        n = len(s)
        cuts: list[int] = [0] * n
        pali: list[list[bool]] = [[False] * n for _ in range(n)]

        for i in range(n):
            minCut = i
            for j in range(i+1):
                if s[j] == s[i] and (j + 1 > i - 1 or pali[j+1][i-1]):
                    pali[j][i] = True
                    minCut = 0 if j == 0 else min(minCut, cuts[j-1] + 1)

            cuts[i] = minCut

        return cuts[-1]



sol = Solution()
print(sol.minCut("ababaaabbaa"))

# [['a', 'aa'], ['a'], ['b', 'aba', 'aabaa'], ['a', 'aa'], ['a', 'aaa', 'aa', 'aaaa'], ['a', 'aaa', 'aa'], ['a']]
