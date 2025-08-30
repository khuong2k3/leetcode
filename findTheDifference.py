
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for cs, ts in zip(s, t):
            ans ^= ord(cs)
            ans ^= ord(ts)

        ans ^= ord(t[-1])

        return chr(ans)

sol = Solution()
print(
    sol.findTheDifference("abcd", "abcde")
)

