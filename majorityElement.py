class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candiate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == candiate:
                count += 1
            else:
                count -= 1

            if count == 0:
                candiate = nums[i]
                count = 1

        return candiate

    def majorityElement2(self, nums: list[int]) -> list[int]:
        candiate1 = candiate2 = 0
        count1 = count2 = 0
        thres = len(nums) // 3

        for num in nums:
            if num == candiate1:
                count1 += 1
            elif num == candiate2:
                count2 += 1
            elif count1 == 0:
                candiate1 = num
                count1 = 1
            elif count2 == 0:
                candiate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == candiate1:
                count1 += 1
            elif num == candiate2:
                count2 += 1

        ans = []
        if count1 > thres:
            ans.append(candiate1)
        if count2 > thres:
            ans.append(candiate2)

        return ans


sol = Solution()
print(sol.majorityElement2([2, 2, 1, 1, 1, 2, 2]))
print(sol.majorityElement2([3, 2, 3]))
print(sol.majorityElement2([3, 2]))
