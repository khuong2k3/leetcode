class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dictSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in dictSet:
                    dp[i] = True
                    break

        return dp[len(s)]


sol = Solution()
print(
    sol.wordBreak("leetcode", ["leet","code"])
)
