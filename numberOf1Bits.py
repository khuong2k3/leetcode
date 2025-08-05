
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            print(bin(n))
            n &= n - 1
            count += 1

        return count


num = 3
sol = Solution()

print(
    sol.hammingWeight(300)
)
