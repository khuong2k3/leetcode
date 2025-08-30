class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def checkAdditive(idxM: int, idxR: int):
            idxL = 0

            while idxR < len(num):
                if (num[idxL] == "0" and idxM - idxL > 1) or (
                    num[idxM] == "0" and idxR - idxM > 1
                ):
                    return False

                value = str(int(num[idxL:idxM]) + int(num[idxM:idxR]))
                if num[idxR : idxR + len(value)] != value:
                    return False

                idxL = idxM
                idxM = idxR
                idxR += len(value)

            return True

        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                if checkAdditive(i, j):
                    return True

        return False


sol = Solution()

# print(sol.isAdditiveNumber("199100199"))
# print(sol.isAdditiveNumber("10"))
# print(sol.isAdditiveNumber("111"))
# print(sol.isAdditiveNumber("1023"))
print(sol.isAdditiveNumber("101"))
