
class NumArray:

    def __init__(self, nums: list[int]):
        self.sumLeft: list[int] = [0] * (len(nums)+1)
        s = 0
        for i, num in enumerate(nums):
            s += num
            self.sumLeft[i+1] = s

    def sumRange(self, left: int, right: int) -> int:
        return self.sumLeft[right+1] - self.sumLeft[left]

sol = NumArray([-2,0,3,-5,2,-1])

print(sol.sumRange(0, 2))




