
def equalPrefix(strs: list[str], i: int):
    if i >= len(strs[0]):
        return False

    current = strs[0][i]
    for s in strs[1:]:
        if i >= len(s) or current != s[i]:
            return False

    return True

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        right = 0
        while True:
            if equalPrefix(strs, i):
                right += 1
            else:
                break
            i += 1

        return strs[0][:right]

sol = Solution()

print(
    sol.longestCommonPrefix(["flower","flow","flight"])
)
