class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        bits = self.hammingWeight(n >> 1)

        if n & 1 == 1:
            return bits + 1
        else:
            return bits

    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y

        return x.bit_count()

    def totalHammingDistance(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for bit in range(0, 32):
            ones = 0
            for num in nums:
                if ((num & (1 << bit)) != 0):
                    ones += 1
            zero = n - ones
            total += ones * zero

        return total


sol = Solution()
# print(sol.countBits(5))
# print(sol.hammingWeight(10))
print(sol.hammingDistance(2, 3))
# for i in range(1, 30):
#     print(i & (i - 1), i)
