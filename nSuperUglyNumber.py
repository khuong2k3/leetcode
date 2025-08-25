
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        idxes = [0] * len(primes)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, len(dp)):
            nextList = [dp[idx] * prime for idx, prime in zip(idxes, primes)]
            next = min(nextList)
            dp[i] = next

            for i, nxt in enumerate(nextList):
                if next == nxt:
                    idxes[i] += 1

        return dp[-1]


sol = Solution()
print(sol.nthSuperUglyNumber(12, [2,7,13,19]))
        
