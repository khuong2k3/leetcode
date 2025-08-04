

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(current_string, open_count, close_count):
            # Base case: if the string is complete, add it to the result
            if len(current_string) == 2 * n:
                result.append(current_string)
                return

            # Recursive step:
            # 1. Add an opening parenthesis if we haven't used all n of them
            if open_count < n:
                backtrack(current_string + '(', open_count + 1, close_count)

            # 2. Add a closing parenthesis if it's a valid move
            # (i.e., we have more open parentheses than closed ones)
            if close_count < open_count:
                backtrack(current_string + ')', open_count, close_count + 1)

        result = []
        backtrack("", 0, 0)

        return result




sol = Solution()
print(
    sol.generateParenthesis(3)
)
