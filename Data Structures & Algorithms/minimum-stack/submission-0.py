class MinStack:

    def __init__(self):
        self.Stack=[]
        self.Mini=[]

    def push(self, value: int) -> None:
        self.Stack.append(value)
        if not self.Mini or value <= self.Mini[-1]:
            self.Mini.append(value)

    def pop(self) -> None:
        x=self.Stack.pop()
        if x == self.Mini[-1]:
            self.Mini.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.Mini[-1]
