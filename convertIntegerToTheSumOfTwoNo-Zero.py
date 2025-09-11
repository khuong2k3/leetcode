

def isNoneZero(n: int):
    for c in str(n):
        if c == '0':
            return False
    return True

class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for a in range(1, n):
            if not isNoneZero(a):
                continue

            b = n - a
            if isNoneZero(b):
                return [a, b]

        return []
        

for i in range(0, 100, 5):
    print(i, bin(i))

