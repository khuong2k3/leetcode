from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1 = Counter(list(s))
        count2 = Counter(list(t))

        return count1 == count2


sol = Solution()

print(sol.isAnagram("anagram", "nagaram"))
