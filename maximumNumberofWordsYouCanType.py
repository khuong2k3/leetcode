
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        idx = 0
        n = len(text)

        ans = 0
        while idx < n:
            ok = True
            while idx < n and text[idx] != ' ':
                if ok:
                    if text[idx] in brokenLetters:
                        ok = False
                idx += 1

            if ok:
                ans += 1

            while idx < n and text[idx] == ' ':
                idx += 1

        return ans 

sol = Solution()
print(sol.canBeTypedWords("hello world", "ad"))
print(sol.canBeTypedWords("leet code", "lt"))
