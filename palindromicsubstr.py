from collections import Counter


class Solution:

    def extendPalindrome(self, s: str, left: int, right: int, maxRange: list[int]):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if maxRange[1] - maxRange[0] < right - left + 1:
                maxRange[0] = left
                maxRange[1] = right + 1
            left -= 1
            right += 1

        # return (left, right)

    def longestPalindrome(self, s: str) -> str:
        lRange = [0, 0]

        for i in range(len(s)):
            self.extendPalindrome(s, i, i, lRange)
            self.extendPalindrome(s, i, i+1, lRange)

        return s[lRange[0]:lRange[1]]

    def longestPalindromeDp(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        maxLength = 1 
        start = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and maxLength < length: 
                    start = i
                    maxLength = length

        return s[start : start + maxLength]

    def longestPalindrome2(self, s: str) -> int:
        sCounter = Counter(s)
        hasOdd = False

        ans = 0
        for value in sCounter.values():
            if value & 1 == 0:
                ans += value
            else:
                hasOdd = True
                ans += value - 1

        if hasOdd:
            ans += 1

        return ans


# class Solution:
#     def longestPalindrome(self, s: str) -> int:


a = Solution()
print(a.longestPalindrome("babad"))
# print(a.longestPalindromeDp(""))
# print(a.longestPalindrome("bbb"))
# print(a.longestPalindrome("a"))
# print(a.longestPalindrome("aacabdkacaa"))
