
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(filter(lambda w: w != '', reversed(s.split(' '))))

sol = Solution()
# sol.reverseWords("the sky is blue")
print(
    sol.reverseWords( "a good   example")
)

        
