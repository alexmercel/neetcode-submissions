class MinStack:

    def __init__(self):
        self.stack=[]
        self.mStack=[]
        self.minVal=float("inf")
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = min(self.minVal,val)
        self.mStack.append(self.minVal)
        
    def pop(self) -> None:
        self.stack.pop()
        self.mStack.pop()
        self.minVal = self.mStack[-1] if len(self.mStack) else float("inf")

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mStack[-1]
        
