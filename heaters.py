
MAX_INT = 10 ** 9 
class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)

        housesGap = [MAX_INT] * len(houses)

        houseIdx = 0
        heaterIdx = 0
        while houseIdx < len(houses) and heaterIdx < len(heaters):
            if heaters[heaterIdx] >= houses[houseIdx]:
                housesGap[houseIdx] = heaters[heaterIdx] - houses[houseIdx]
                houseIdx += 1
            else:
                heaterIdx += 1


        houseIdx = len(houses) - 1
        heaterIdx = len(heaters) - 1
        while houseIdx >= 0 and heaterIdx >= 0:
            if heaters[heaterIdx] <= houses[houseIdx]:
                housesGap[houseIdx] = min(houses[houseIdx] - heaters[heaterIdx], housesGap[houseIdx])
                houseIdx -= 1
            else:
                heaterIdx -= 1

        return max(housesGap)

sol = Solution()

print(sol.findRadius([1,2,3], [1, 2, 3]))
# print(sol.findRadius([1,5], [4]))
