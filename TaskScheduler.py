from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = Counter(tasks)
        
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0

        while len(max_heap) != 0:
            temp_heap = []

            runned = 0
            for _ in range(n+1):
                if len(max_heap) == 0:
                    break

                runned += 1
                count = heapq.heappop(max_heap)
                count += 1

                if count != 0:
                    temp_heap.append(count)
                    # heapq.heappush(temp_heap, count)

            for count in temp_heap:
                heapq.heappush(max_heap, count)

            if len(max_heap) != 0:
                time += n+1
            else:
                time += runned
        
        return time 


sol = Solution()

print(
    sol.leastInterval(["A","A","A","B","B","B"], 3)
)

# print(
#     sol.leastInterval(["A","C","A","B","D","B"], 2)
# )

