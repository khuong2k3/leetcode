
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        idx2 = 0

        sortedArray = []
        while idx1 < m and idx2 < n:
            if nums1[idx1] <= nums2[idx2]:
                sortedArray.append(nums1[idx1])
                idx1 += 1
            else:
                sortedArray.append(nums2[idx2])
                idx2 += 1

        while idx1 < m:
            sortedArray.append(nums1[idx1])
            idx1 += 1

        while idx2 < n:
            sortedArray.append(nums2[idx2])
            idx2 += 1

        for i in range(len(sortedArray)):
            nums1[i] = sortedArray[i]
        

sol = Solution()

sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

