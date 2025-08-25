
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0

        cSecret = Counter(list(secret))
        cGuess = Counter(list(guess))

        for c, value in cGuess.items():
            if cSecret.get(c) is not None:
                cow += min(value, cSecret[c])

        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
                cow -= 1

        return f"{bull}A{cow}B"


sol = Solution()

print(
    sol.getHint("1807", "7810")
)
