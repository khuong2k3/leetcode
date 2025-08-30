
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        def oneWay(s, t) -> bool:
            mapDict = {}
            for word, c in zip(s, t):
                if c not in mapDict:
                    mapDict[c] = word
                elif mapDict[c] != word:
                    return False

            return True

        return oneWay(pattern, words) and oneWay(words, pattern)

sol = Solution()
print(
    sol.wordPattern("abba", "dog cat cat dog")
)

