

def longestSubsequence(nums: list[int]) -> int:
    lis = [1] * len(nums)
    maxLength = 1
    for i in range(1, len(nums)):
        seqs = [lis[j] for j in range(i) if nums[j] > nums[i]]
        lis[i] = 1 + max(seqs, default=0)
        maxLength = max(maxLength, lis[i])

    return maxLength


print(
    longestSubsequence([5, 2, 8, 6, 3, 6, 9, 5])
)
