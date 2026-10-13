class MinStack:

    def __init__(self):
        self.stack=[]
        # self.mStack=[]
        self.minVal=float("inf")
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minVal = val
        else:
            # Store the difference between val and the current minimum
            self.stack.append(val - self.minVal)
            # Update minVal if the new value is smaller
            if val < self.minVal:
                self.minVal = val

        
    def pop(self) -> None:
        val=self.stack.pop()
        if val<0:
            self.minVal -= val
        return val + self.minVal

    def top(self) -> int:
        top_val = self.stack[-1]
        # If top_val is negative, it means the current minimum IS the top element
        if top_val < 0:
            return self.minVal
        else:
            # Otherwise, the original value is minVal + difference
            return self.minVal + top_val

    def getMin(self) -> int:
        return self.minVal
        
