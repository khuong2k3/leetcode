import random

class Solution:
    org: list[int]

    def __init__(self, nums: list[int]):
        self.org = nums
        
    def reset(self) -> list[int]:
        return self.org
        
    def shuffle(self) -> list[int]:
        ans = self.org.copy()
        random.shuffle(ans)
        return ans
