from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph: defaultdict[int, list[int]] = defaultdict(lambda : [])

        for course in prerequisites:
            graph[course[0]].append(course[1])

        visited = set()
        recursionStack = set()

        def dfs(node: int):
            visited.add(node)
            recursionStack.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in recursionStack:
                    return True

            recursionStack.remove(node)
            return False

        def have_circle():
            for node in list(graph.keys()):
                if node not in visited:
                    if dfs(node):
                        return True

            return False

        return not have_circle()

sol = Solution()

print(sol.canFinish(2, [[1,0],[0,1]]))
        
