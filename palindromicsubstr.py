
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalin = ""
        for i in range(max(1, len(s)-1)):
            for mode in range(0, 2):
                left = i
                right = i + mode

                while left >= 0 and right < len(s):
                    if s[left] != s[right]:
                        break
                    else:
                        if len(longestPalin) < right-left+1:
                            longestPalin = s[left:right+1]

                        left -= 1
                        right += 1

        return longestPalin



a = Solution()
print(a.longestPalindrome("babad"))
print(a.longestPalindrome("bbb"))
# print(a.longestPalindrome("a"))
# print(a.longestPalindrome("aacabdkacaa"))
print(a.longestPalindrome("aaaabaaa"))
# print(a.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
#

