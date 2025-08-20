
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations = sorted(citations, reverse=True)

        return max(map(lambda ele: ele[0], filter(lambda ele: ele[1] >= ele[0], enumerate(citations, 1))), default=0)

sol = Solution()

print(
    sol.hIndex([3,0,6,1,5])
)

print(
    sol.hIndex([1,1,3])
)
# [3,0,6,1,5]

# [6,5,3,1,0]

        
