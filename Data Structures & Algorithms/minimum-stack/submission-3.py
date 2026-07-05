class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val) 
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)       

    def pop(self) -> None:
        pop = self.stack[-1]
        if self.min_stack[-1] == pop:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
