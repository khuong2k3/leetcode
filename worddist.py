# If either word1 or word2 is empty, return the maximum length of the two strings as the minimum edit distance.
#
# If word1 is equal to word2, return 0 as the minimum edit distance.
#
# Create a 2D array dp of size (m+1) x (n+1), where m and n are the lengths of word1 and word2 respectively.
# Each element of the array dp[i][j] represents the minimum edit distance between the first i characters of word1 and the first j characters of word2.
#
# Initialize the first row of dp to the values from 0 to n, and the first column of dp to the values from 0 to m. This is because the minimum edit distance between an empty string and a string of length j is j, and vice versa.
#
# Iterate over each character in word1 and word2 and fill in the rest of the dp array based on the following conditions:
#
# If i is 0, dp[i][j] is equal to j, because the minimum edit distance between an empty string and a string of length j is j.
#
# If j is 0, dp[i][j] is equal to i, because the minimum edit distance between a string of length i and an empty string is i.
#
# If the characters at positions i-1 and j-1 of word1 and word2 respectively are equal, dp[i][j] is equal to dp[i-1][j-1], because no edit is needed.
#
# If the characters at positions i-1 and j-1 of word1 and word2 respectively are not equal, dp[i][j] is equal to 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]), where dp[i-1][j-1] represents the minimum edit distance after replacing the character at position i-1 in word1 with the character at position j-1 in word2, dp[i][j-1] represents the minimum edit distance after inserting the character at position j-1 of word2 into word1, and dp[i-1][j] represents the minimum edit distance after deleting the character at position i-1 of word1.
#
# The final answer is the value of dp[m][n], which represents the minimum edit distance between the entire strings word1 and word2.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        if word1 == word2:
            return 0

        templist = list(range(0, len(word2) + 1))
        dp = [templist.copy() for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(0, len(word2) + 1):
                if j == 0:
                    dp[i][0] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j-1], # replacing
                        dp[i][j-1], # inserting
                        dp[i-1][j] # deleting
                    )
                    

        return dp[len(word1)][len(word2)]

sol = Solution()
print(sol.minDistance("hourse", 'rose'))
