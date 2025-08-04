from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0 
        cStore = defaultdict(lambda : -1)
        startIdx = -1

        for i, c in enumerate(s):
            if cStore[c] > startIdx:
                startIdx = cStore[c]
            cStore[c] = i
            maxLen = max(maxLen, i - startIdx)

        return maxLen


        
