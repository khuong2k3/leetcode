
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 60):
            num1 -= num2
            if num1 < i:
                return -1

            bits = num1.bit_count()
            if bits <= i:
                return i

        return -1

sol = Solution()
# print(sol.makeTheIntegerZero(3, -2))
# print(sol.makeTheIntegerZero(5, 7))
print(sol.makeTheIntegerZero(85, 42))
