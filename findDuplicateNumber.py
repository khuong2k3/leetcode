
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0] 
        fast = nums[0]

        while True:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        print("====")
        fast = nums[0]
        while slow != fast:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[fast]

        return slow

sol = Solution()
print(
    # sol.findDuplicate([1,3,4,2,2])
    sol.findDuplicate([2,5,9,6,9,3,8,9,7,1])
)

# [2,5,9,6,9,3,8,9,7,1]
