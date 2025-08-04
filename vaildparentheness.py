
def isOpenParenthenss(c: str):
    return c == "[" or c == "(" or c == "{"

def isCloseParenthenss(c: str):
    return c == "]" or c == ")" or c == "}"

PARENTHENLOOKUP = {
    '[': ']',
    '{': '}',
    '(': ')',
}

class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        for c in s:
            if isOpenParenthenss(c):
                stacks.append(c)
            elif isCloseParenthenss(c):
                if len(stacks) > 0 and PARENTHENLOOKUP[stacks[-1]] == c:
                    stacks.pop()
                else:
                    return False
        return len(stacks) == 0



