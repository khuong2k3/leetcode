

def permutation(nums: list[int], i: int, ans: list[int]):
    if len(ans) == len(nums):
        print(ans)
        return

    for j in range(len(nums)):
        if nums[j] in ans:
            continue

        ans.append(nums[j])
        permutation(nums, j, ans)
        ans.pop()


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        outputs: list[list[int]] = []
        def _backtract(ans: list[int], checker: list[bool]):
            if len(ans) == len(nums):
                outputs.append(ans.copy())
                return

            for j in range(len(nums)):
                if checker[j]:
                    continue

                ans.append(nums[j])
                checker[j] = True
                _backtract(ans, checker)
                checker[j] = False
                ans.pop()

        _backtract([], [False for _ in range(len(nums))])
        return outputs
        
class Solution2:
    def permute(self, nums: list[int]) -> list[list[int]]:
        outputs: list[list[int]] = [[]]

        for num in nums:
            new_outputs_for_num: list[list[int]] = []

            for current_permutation in outputs:
                for i in range(len(current_permutation) + 1):
                    new_permutation = current_permutation[i:] + [num] + current_permutation[:i]
                    new_outputs_for_num.append(new_permutation)

            outputs = new_outputs_for_num

        return outputs

class Solution3:
    def permute(self, nums: list[int]) -> list[list[int]]:
        outputs: list[list[int]] = [[]]

        return outputs



sol = Solution2()

test1 = [1, 2, 3]
# permutation(test1, 0, [])

print(
    sol.permute(test1)
)
