
class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = str(num)
        idx = 0
        ans = 0
        while idx < len(numStr):
            ans *= 10
            if numStr[idx] == '6':
                ans += 9
                idx += 1
                break
            else:
                ans += int(numStr[idx])
            idx += 1

        while idx < len(numStr):
            ans *= 10
            ans += int(numStr[idx])
            idx += 1
        return ans

sol = Solution()
print(
    sol.maximum69Number(9969)
)


