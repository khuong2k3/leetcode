class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        i = 0
        ans = []
        while i < len(prev):
            c = prev[i]
            count = 0
            while i < len(prev) and prev[i] == c:
                count += 1
                i += 1
            ans.append(str(count))
            ans.append(c)

        return "".join(ans)


sol = Solution()

print(sol.countAndSay(5))

class SolutionIter:
    def countAndSay(self, n: int) -> str:
        ans = ["1"]

        for _ in range(n-1):
            newAns = []
            i = 0
            while i < len(ans):
                c = ans[i]
                count = 0
                while i < len(ans) and ans[i] == c:
                    count += 1
                    i += 1
                newAns.append(str(count))
                newAns.append(c)

            ans = newAns
            
        return "".join(ans)



sol = SolutionIter()

print(sol.countAndSay(5))



