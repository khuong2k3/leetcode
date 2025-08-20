
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if len(s) == 0 or s[0] == '0':
#             return 0
#
#         if len(s) == 1 and s[0] != '0':
#             return 1
#
#         n = len(s)
#         dp = [0] * (n+1)
#         dp[n] = 1
#         for i in reversed(range(0, len(s))):
#             if s[i] == '0':
#                 dp[i] = 0
#             else:
#                 dp[i] = dp[i+1]
#                 if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
#                     dp[i] += dp[i+2]
#
#         return dp[0]

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0

        if len(s) == 1 and s[0] != '0':
            return 1

        n = len(s)
        prev = 0
        mid = 1 
        curr = 0
        for i in reversed(range(0, len(s))):
            if s[i] == '0':
                curr = 0
            else:
                curr = mid 
                if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    curr += prev

            prev = mid
            mid = curr

        return curr
        

sol = Solution()

print(
    sol.numDecodings("12")
)
print(
    sol.numDecodings("226223")
)

print(
    sol.numDecodings("2101")
)

print(
    sol.numDecodings("27")
)
