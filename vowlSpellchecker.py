
VOWLS = set('auioeAUIOE')

def hashVowl(word: str):
    idx = 0
    ans = ""
    while idx < len(word):
        if word[idx] in VOWLS:
            ans += '*'
        else:
            ans += word[idx]

        idx += 1
        
    return ans


class Solution:
    wordDict: set
    vowlDict: dict[str, str]
    capDict: dict[str, str]

    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        self.wordDict = set()
        self.vowlDict = {}
        self.capDict = {}

        for word in wordlist:
            self.wordDict.add(word)

            wordLower = word.lower()
            if wordLower not in self.capDict:
                _ = self.capDict.setdefault(wordLower, word)

            wordVowls = hashVowl(wordLower)
            if wordVowls not in self.vowlDict:
                _ = self.vowlDict.setdefault(wordVowls, word)

        print(self.capDict)
        return [self.solve(word) for word in queries]

    def solve(self, word: str) -> str:
        if word in self.wordDict:
            return word

        wordLower = word.lower()
        if wordLower in self.capDict:
            return self.capDict[wordLower]

        wordVowls = hashVowl(wordLower)
        if wordVowls in self.vowlDict:
            return self.vowlDict[wordVowls]

        return ''


sol = Solution()
print(
    sol.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])
)

# ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# ['kite', '', 'KiTe', 'Hare', '', '', '', 'kite', '', 'kite']
# ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
# print(hash("".join(["12", "4"])))
