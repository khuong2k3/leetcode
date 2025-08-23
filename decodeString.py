class Solution:
    def parseNum(self, s: str, i: int) -> tuple[int, int]:
        num = 0
        numLen = 0
        for j in range(i, len(s)):
            if s[j] >= "0" and s[j] <= "9":
                num *= 10
                num += int(s[j])
                numLen += 1
            else:
                break
        return (num, numLen) if numLen > 0 else (0, 0)

    def subString(self, s: str, idx: int) -> str:
        left = idx
        right = left
        for j in range(left, len(s)):
            if s[j] >= "a" and s[j] <= "z":
                right += 1
            else:
                break

        return s[left:right]

    def decodeString(self, s: str) -> str:
        def _backtract(idx: int) -> tuple[str, int]:
            ans = "" 

            while idx < len(s):
                if s[idx] >= "0" and s[idx] <= "9":
                    num, numLen = self.parseNum(s, idx)
                    idx += numLen + 1
                    substr, pos = _backtract(idx)
                    idx = pos+1
                    ans += num * substr
                elif s[idx] == ']':
                    break
                else:
                    value = self.subString(s, idx)
                    idx += len(value)
                    ans += value

            return (ans, idx)

        return _backtract(0)[0]


sol = Solution()

print(sol.decodeString("3[a]2[bc]"))
