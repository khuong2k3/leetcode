
def inList(a: list[list[int]], b: list[int]):
    for x in a:
        if x == b:
            return True
    return False

def insertSorted(a: list[int], value: int) -> list[int]:
    if len(a) == 0:
        return [value]
    newSet = []

    inserted = False
    for i in range(len(a)):
        if not inserted and a[i] >= value:
            newSet.append(value)
            inserted = True
        newSet.append(a[i])

    if not inserted:
        newSet.append(value)
        
    return newSet
            
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    candidates = sorted(candidates)
    dp: list[list[list[int]]] = [[] for _ in range(target + 1)]
    dp[0].append([])

    for i in range(1, len(dp)):
        for num in candidates:
            if num > i:
                break

            for prev in dp[i - num]:
                newSet = insertSorted(prev, num)

                if not inList(dp[i], newSet):
                    dp[i].append(newSet)

    return dp[target]

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        return combinationSum(candidates, target)

# 2 + 2 + 2
# 3 + 3
# 6
# 7
test1 = [2,3,6,7]

print(
    combinationSum(test1, 7)
)


print([1, 2] == [1, 2])
