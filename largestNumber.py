from typing import Callable

def quicksort(arr: list[str], cmp: Callable[[str, str], int]):
    def _quicksort_recursive(arr: list[str], low: int, high: int):
        if low < high:
            pivot_index = _partition(arr, low, high)

            _quicksort_recursive(arr, low, pivot_index - 1)
            _quicksort_recursive(arr, pivot_index + 1, high)

    def _partition(arr: list[str], low: int, high: int):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if cmp(arr[j], pivot) != 1:
            # arr[j] <= pivot
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    _quicksort_recursive(arr, 0, len(arr) - 1)

def cmpStr(a: str, b: str) -> int:
    ab = a + b
    ba = b + a
    if ab > ba:
        return -1
    elif ab == ba:
        return 0
    else:
        return 1

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        numsStr = list(map(lambda x: str(x), nums))
        quicksort(numsStr, cmp=cmpStr)
        ans = "".join(numsStr)
        start = 0
        while start <= len(ans) - 2 and ans[start] == '0':
            start += 1
        return ans[start:]

sol = Solution()

print(
    sol.largestNumber([3,30,34,5,9])
)
