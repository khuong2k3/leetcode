
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for _ in range(32):
            ans = ans << 1
            ans = ans | (n & 1)
            n = n >> 1 

        return ans

sol = Solution()
print(sol.reverseBits(43261596))
