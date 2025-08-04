
# 0
# 11, 10
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        while i < len(bits):
            if i + 1 < len(bits):
                if bits[i] == 1:
                    i += 2
                else:
                    i += 1
            else:
                return bits[i] == 0

        return False


sol = Solution()
print(sol.isOneBitCharacter([0,1,1,0,0]))
print(sol.isOneBitCharacter([0,1,1,1,0]))
