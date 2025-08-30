
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left != right:
            mid = (left + right) >> 1
            if mid == left or mid == right:
                return mid

            val = mid * mid
            if val == x:
                return mid
            elif val > x:
                right = mid
            else:
                left = mid

        return x


sol = Solution()
print(sol.mySqrt(5))

