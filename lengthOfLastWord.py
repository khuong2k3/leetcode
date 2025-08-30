
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        idx = len(s) - 1

        while idx >= 0:
            if s[idx] == ' ':
                idx -= 1
            else:
                break
        while idx >= 0:
            if s[idx] != ' ':
                ans += 1
                idx -= 1
            else:
                break

        return ans


