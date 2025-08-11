
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        if len(s) > len(t):
            return False
        elif len(s) == 0:
            return True

        for c in t:
            if s[idx] == c:
                idx += 1

            if idx == len(s):
                return True

        return False


s1 = "abc"
t1 = "ahbgdc"

sol = Solution()

print(
    sol.isSubsequence(s1, t1)
)

