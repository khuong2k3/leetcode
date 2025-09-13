from collections import defaultdict


VOWLS = list("aeiou")


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowlsTb = defaultdict(lambda: 0)
        consonantsTb = defaultdict(lambda: 0)
        maxVowl = ""
        maxConsonant = ""
        for c in s:
            if c in VOWLS:
                vowlsTb[c] += 1
                if vowlsTb[c] > vowlsTb[maxVowl]:
                    maxVowl = c
            else:
                consonantsTb[c] += 1
                if consonantsTb[c] > consonantsTb[maxConsonant]:
                    maxConsonant = c

        return vowlsTb[maxVowl] + consonantsTb[maxConsonant]
