VOWLS = set("aeiou")

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowlCount = 0

        for c in s:
            if c in VOWLS:
                vowlCount += 1

        return vowlCount != 0

