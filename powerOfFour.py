class Solution:
    # def isPowerOfFour(self, n: int) -> bool:
    #     if n == 0:
    #         return False
    #
    #     isNegative = n < 0
    #     count = 0
    #
    #
    #     while n > 1:
    #         m = n >> 2
    #         count += 1
    #         if m << 2 != n:
    #             return False
    #
    #         n = m
    #
    #     return count & 1 == 1 if isNegative else True

    def isPowerOfFour(self, n: int) -> bool:
        return not not(n > 0 and not n & (n - 1) and (n & 0x55555555))


sol = Solution()
print(sol.isPowerOfFour(3))

# print(bin(0x55555555))
