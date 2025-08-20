
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single = double = 0

        for num in nums:
            single = (single ^ num) & ~double
            double = (double ^ num) & ~single
            print(single, double)

        return single

sol = Solution()

print(
    sol.singleNumber([2,2,3,2])
)

# print("====")
# print(
#     sol.singleNumber(
#         [0,1,0,1,0,1,99,2,2,2]
#     )
# )

