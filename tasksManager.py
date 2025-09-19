from dataclasses import dataclass
import heapq


@dataclass
class Task:
    userId: int
    taskId: int
    priority: int


class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.tasks: list[tuple[int, int]] = []
        self.tasksInfo: dict[int, Task] = {}

        for task in tasks:
            self.add(task[0], task[1], task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasksInfo[taskId] = Task(userId, taskId, priority)
        heapq.heappush(self.tasks, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        taskInfo = self.tasksInfo[taskId]
        taskInfo.priority = newPriority
        heapq.heappush(self.tasks, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.tasksInfo:
            _ = self.tasksInfo.pop(taskId)

    def execTop(self) -> int:
        while len(self.tasks) != 0:
            priority, taskId = heapq.heappop(self.tasks)
            taskId = -taskId

            if taskId in self.tasksInfo:
                taskInfo: Task = self.tasksInfo[taskId]
                if taskInfo.priority == -priority:
                    userId = taskInfo.userId
                    del self.tasksInfo[taskId]
                    return userId

        return -1



