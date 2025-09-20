import bisect
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Package:
    source: int
    destination: int
    timestamp: int


class Router:
    def __init__(self, memoryLimit: int):
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0
        self.packages: list[Package] = [Package(0, 0, 0)] * memoryLimit
        self.packagesDict: set[tuple[int, int, int]] = set()
        self.destDict: defaultdict[int, list[int]] = defaultdict(lambda: [])

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        newPackageTub = (source, destination, timestamp)
        if newPackageTub in self.packagesDict:
            return False

        newPackage = Package(source, destination, timestamp)
        if self.size == len(self.packages):
            left = self.packages[self.head]
            leftTub = (left.source, left.destination, left.timestamp)
            self.head = (self.head + 1) % len(self.packages)
            if leftTub in self.packagesDict:
                self.packagesDict.remove(leftTub)
                _ = self.destDict[left.destination].pop(0)

            self.size -= 1

        self.size = min(self.size + 1, len(self.packages))
        self.packages[self.tail] = newPackage
        self.destDict[newPackage.destination].append(newPackage.timestamp)
        self.packagesDict.add(newPackageTub)

        self.tail = (self.tail + 1) % len(self.packages)

        return True

    def forwardPacket(self) -> list[int]:
        if self.size == 0:
            return []

        package = self.packages[self.head]
        self.packagesDict.remove(
            (package.source, package.destination, package.timestamp)
        )
        _ = self.destDict[package.destination].pop(0)

        self.head = (self.head + 1) % len(self.packages)
        self.size -= 1

        return [package.source, package.destination, package.timestamp]

    def packIndex(self, idx: int):
        return (idx + self.head) % len(self.packages)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        destinationPack = self.destDict[destination]
        startIdx = bisect.bisect_left(destinationPack, startTime)
        endIdx = bisect.bisect_right(destinationPack, endTime)

        return endIdx - startIdx

    # def getCount(self, destination: int, startTime: int, endTime: int) -> int:
    #     count = 0
    #     startIdx = self.getIdx(startTime)
    #
    #     for i in range(startIdx, self.size):
    #         idx = self.packIndex(i)
    #         package = self.packages[idx]
    #         if package.timestamp < startTime:
    #             continue
    #
    #         if package.timestamp <= endTime:
    #             if package.destination == destination:
    #                 count += 1
    #         else:
    #             break
    #
    #     return count


router = Router(3)

for package in [[1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105]]:
    print(router.addPacket(package[0], package[1], package[2]))

print(router.forwardPacket())
_ = router.addPacket(5, 2, 110)

print(router.packages)
print(router.getCount(5, 100, 110))


# router = Router(5)
#
# print(router.addPacket(1,2,5))
# print(router.packages)
# print(router.getCount(2,4,5))

# def isDuplicated(self, package: Package):
#     idx = self.tail - 1
#     if idx == -1:
#         idx = len(self.packages) - 1
#     for _ in range(self.size):
#         if self.packages[idx].timestamp != package.timestamp:
#             break
#
#         if (
#             self.packages[idx].source == package.source
#             and self.packages[idx].destination == package.destination
#         ):
#             return True
#
#         idx -= 1
#         if idx == -1:
#             idx = len(self.packages) - 1
#
#     return False
# def getIdx(self, time: int):
#     left = 0
#     right = self.size - 1
#     result = 0
#
#     while left <= right:
#         mid = (left + right) >> 1
#         midIdx = self.packIndex(mid)
#
#         if self.packages[midIdx].timestamp == time:
#             result = mid
#             right = mid - 1
#         elif self.packages[midIdx].timestamp < time:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return result
#
