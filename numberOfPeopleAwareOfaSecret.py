MOD = 10**9 + 7


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        dp[0] = 1
        share = 0

        for i in range(1, n):
            if i - delay >= 0:
                share = (share + dp[i - delay]) % MOD

            if i - forget >= 0:
                share = (share - dp[i - forget]) % MOD

            dp[i] = share

        res = 0
        for i in range(max(n - forget, 0), n):
            res = (res + dp[i]) % MOD

        return res


sol = Solution()

print(sol.peopleAwareOfSecret(6, 2, 4))
# print(sol.peopleAwareOfSecret(4, 1, 3))
# print(sol.peopleAwareOfSecret(684, 18, 496))
