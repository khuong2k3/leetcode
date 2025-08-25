
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ans = digits.copy()
        ans[-1] += 1
        for i in reversed(range(len(ans))):
            if ans[i] == 10:
                ans[i] = 0
                if i != 0:
                    ans[i-1] += 1
                else:
                    ans.insert(0, 1)

        return ans

