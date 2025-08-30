
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start: int, end: int):
            """Reverses a section of the array in place."""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n

        # Step 1: Reverse the entire array
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements
        reverse(0, k - 1)

        # Step 3: Reverse the remaining elements
        reverse(k, n - 1)


