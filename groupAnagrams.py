from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = defaultdict(lambda: [])

        for s in strs:
            hashMap["".join(sorted(s))].append(s)

        return list(hashMap.values())
        

sol = Solution()

print(
    sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
)
