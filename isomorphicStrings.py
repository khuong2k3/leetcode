
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def oneWay(a: str, b: str):
            strDict: dict[str, str] = dict()
            for cs, ts in zip(a, b):
                # if cs == ts:
                #     continue

                if strDict.get(cs, None) is not None:
                    if strDict[cs] != ts:
                        return False
                else:
                    strDict[cs] = ts

            return True

        return oneWay(s, t) and oneWay(t, s)


sol = Solution()
print(
    sol.isIsomorphic("badc", "baba")
)
