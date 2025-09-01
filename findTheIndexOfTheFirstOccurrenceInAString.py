
def lps(pattern: str):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    # aabaaac
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[length] = 0
                i += 1

    return lps


def kmp(text: str, pat: str) -> int:
    LPS = lps(pat)
    n = len(text)
    m = len(pat)

    i = j = 0
    while i < n:
        if text[i] == pat[j]:
            i += 1
            j += 1

            if j == m:
                return i - j

        else:
            if j != 0:
                j = LPS[j - 1]
            else:
                i += 1

    return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return kmp(haystack, needle)
        # n = len(haystack)
        # m = len(needle)
        #
        # for i in range(n - m + 1):
        #     if haystack[i : i + m] == needle:
        #         return i
        #
        # return -1


sol = Solution()
# print(sol.strStr("aabaaabaaac", "aabaaac"))


# print(kmp("aabaaabaaac", "aabaaac"))
print(lps("aabaaac"))
