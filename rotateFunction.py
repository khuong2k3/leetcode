
class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        sumNums = sum(nums)
        n = len(nums)
        fn = sum(map(lambda x: x[0] * x[1], enumerate(nums)))
        max = fn

        for i in reversed(range(1, len(nums))):
            fn1 = fn + sumNums - n * nums[i]

            if max < fn1:
                max = fn1

            fn = fn1

        return max
        
sol = Solution()

print(sol.maxRotateFunction([4,3,2,6]))
