
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        prev = 1
        curr = 2
        for _ in range(n-2):
            next = curr + prev
            prev = curr
            curr = next

        return curr

sol = Solution()

print(
    sol.climbStairs(3)
)

