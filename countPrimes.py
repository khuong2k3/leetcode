
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        table = [True] * n
        table[0] = False
        table[1] = False

        for j in range(4, len(table), 2):
            table[j] = False

        numPrime = 1
        for i in range(3, len(table), 2):
            if table[i]:
                numPrime += 1
                for j in range(i+i, len(table), i):
                    table[j] = False

        return numPrime

sol = Solution()

print(sol.countPrimes(10))

print(sol.countPrimes(3))
print(sol.countPrimes(2))

