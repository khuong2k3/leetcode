
class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        need = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            ok = False
            for x in languages[u]:
                if x in languages[v]:
                    ok = True
                    break
            if not ok:
                need.add(u)
                need.add(v)

        ans = len(languages) + 1
        for i in range(1, n + 1):
            cans = 0
            for v in need:
                if i not in languages[v]:
                    cans += 1
            ans = min(ans, cans)
        return ans

sol = Solution()

print(
    sol.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]])
)

