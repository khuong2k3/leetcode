
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distx = abs(x - z)
        disty = abs(y - z)
        if distx == disty:
            return 0
        elif distx < disty:
            return 1 
        else:
            return 2

