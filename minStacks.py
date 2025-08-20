
class MinStack:
    def __init__(self):
        self.minS: list[int] = []
        self.stack: list[int] = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minS) == 0:
            self.minS.append(val)
        elif self.minS[-1] >= val:
            self.minS.append(val)

    def pop(self) -> None:
        if len(self.minS) != 0 and self.stack.pop() == self.minS[-1]:
            _ = self.minS.pop()

    def top(self) -> int | None:
        return self.stack[-1] if len(self.stack) != 0 else None
        
    def getMin(self) -> int | None:
        return self.minS[-1] if len(self.minS) != 0 else None

