
LETTERMAPPING = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z']
]

def genLetter(currentstr: str, digits: str, ans: list[str]):
    if len(currentstr) == len(digits):
        ans.append(currentstr)
        return

    digit = int(digits[len(currentstr)]) - 2
    for letter in LETTERMAPPING[digit]:
        genLetter(currentstr + letter, digits, ans)
            
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ans = []
        if len(digits) == 0:
            return []
        genLetter("", digits, ans)
        
        return ans


sol = Solution()

print(len(""))
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))
