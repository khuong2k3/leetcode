

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        sumNums = sum(nums)
        count = [0]

        def _backtract(idx: int, tar: int):
            if tar < target:
                return
            
            for i in range(idx, len(nums)):
                _backtract(i+1, tar - 2 * nums[i])

            if tar == target:
                count[0] += 1
                return

            return

        _backtract(0, sumNums)

        return count[0]


sol = Solution()

print(
    sol.findTargetSumWays([1,1,1,1,1], 3)
)

print(
    sol.findTargetSumWays([1,0], 1)
)

print(
    sol.findTargetSumWays([1], 1)
)

print(
    sol.findTargetSumWays(
        [26,33,25,41,15,46,36,11,29,18,17,26,28,11,39,4,19,13,40,8], 5
    )
)
