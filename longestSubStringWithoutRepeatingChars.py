class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        idxDict = [-1] *  256
        start = 0
        for i in range(len(s)):
            idx = ord(s[i])
            if idxDict[idx] >= 0:
                start = max(idxDict[idx] + 1, start)

            idxDict[idx] = i
            ans = max(i - start + 1, ans)

        return ans

sol = Solution()
# print(sol.lengthOfLongestSubstring("abba"))
print(ord('a'))


