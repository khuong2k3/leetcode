import math

# def isNonCoprime(a: int, b: int):
#     minVal = min(a, b)
#     maxVal = max(a, b)
#     dp = [False] * (minVal + 1)
#
#     for i in range(2, len(dp)):
#         if not dp[i] and minVal % i == 0:
#             if maxVal % i == 0:
#                 return True
#             else:
#                 for j in range(i, len(dp), i):
#                     dp[j] = True

class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        top = -1
        for n in nums:
            curr = n
            while (top != -1):
                g = math.gcd(nums[top], curr)
                if g == 1:
                    break
                curr *= nums[top] // g
                top -= 1
            top += 1
            nums[top] = curr

        return nums[:top+1]


sol = Solution()
# print(sol.replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]))
# print(sol.replaceNonCoprimes([517, 11, 121, 517, 3, 51, 3, 1887, 5]))
# print(sol.replaceNonCoprimes([9901,41,41,1927]))
# print(sol.replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825]))
# [12,7,6]
# print(isNonCoprime(899, 20677))

# 20677 / 899


