class MinStack:

    def __init__(self):
        self.stack=[]
        self.minV= [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minV.append(min(val,self.minV[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minV.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minV[-1]    
