
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        outputs = list()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]

            left = i + 1
            end = len(nums) - 1

            while left < end:
                ans = target + nums[left] + nums[end]
                if ans < 0:
                    left += 1
                elif ans > 0:
                    end -= 1
                else:
                    outputs.append(
                        [target, nums[left], nums[end]]
                    )
                    while left < end and nums[left] == nums[left + 1]:
                        left+=1
                    while left < end and nums[end] == nums[end - 1]:
                        end-=1
                    left+=1
                    end-=1

        return outputs
