VOWLS = list("aeiouAEIOU")

class Solution:
    def sortVowels(self, s: str) -> str:
        indexes = []
        vowls = []
        for i, c in enumerate(s):
            if c in VOWLS:
                indexes.append(i)
                vowls.append(c)

        print(vowls)
        vowls.sort()
        ans = ""
        idx = 0
        n = len(indexes)
        for i, c in enumerate(s):
            if idx < n and indexes[idx] == i:
                ans += vowls[idx]
                idx += 1
            else:
                ans += c

        return ans 


sol = Solution()
print(sol.sortVowels("lYmpH"))
