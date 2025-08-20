
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        i2 = 0
        i3 = 0
        i5 = 0

        for i in range(1,n):
            next2 = dp[i2] * 2
            next3 = dp[i3] * 3 
            next5 = dp[i5] * 5
            next = min(next2, next3, next5)
            dp[i] = next
            if next == next2:
                i2+=1
            if next == next3:
                i3+=1
            if next == next5:
                i5+=1
            
        return dp[-1]


sol = Solution()

print(
    sol.nthUglyNumber(10)
)
