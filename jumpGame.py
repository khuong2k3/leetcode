from collections import deque

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return True

        queue = deque()
        moved = set()
        queue.append(len(nums) - 1)
        moved.add(len(nums) - 1)
        while len(queue) != 0:
            target = queue.pop()
            for j in reversed(range(0, target)):
                if nums[j] >= target - j and j not in moved:
                    queue.append(j)
                    moved.add(j)
                    if j == 0:
                        return True

        return False


class Solution2:
    def canJump(self, nums: list[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1

        return True

test1 = [2,3,1,1,4]
test2 = [3,2,1,0,4]
test3 = [0]

test4 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6] 

test4 = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]

sol = Solution()
print(sol.canJump(test1))
print(sol.canJump(test2))
print(sol.canJump(test3))
print(sol.canJump(test4))

