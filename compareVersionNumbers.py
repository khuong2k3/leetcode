
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(lambda n: int(n), version1.split('.')))
        v2 = list(map(lambda n: int(n), version2.split('.')))

        for i1, i2 in zip(v1, v2):
            if i1 < i2:
                return -1
            elif i1 > i2:
                return 1


        if len(v1) > len(v2):
            for i1 in v1[len(v2):]:
                if i1 > 0:
                    return 1

        elif len(v1) < len(v2):
            for i2 in v2[len(v1):]:
                if i2 > 0:
                    return -1

        return 0

sol = Solution()
# print(sol.compareVersion("1.0", "1.0.0.1"))
print(sol.compareVersion("1.0", "1"))

# print(float("1.20"))
