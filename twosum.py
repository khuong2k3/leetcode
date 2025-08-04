
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = dict()
        currentIdx = 0
        other = 0
        for i, num in enumerate(nums):
            other = target - num
            if other in store:
                currentIdx = i
                break
            store[num] = i

        return [store[other], currentIdx]



