class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # keep adding index in stack untill stack is empty or current element is > stack top.
        #if stack current element greater than stack top, pop the top subtract it from current index and add the value at that index in second string.
        # add the current element to the stack

        stack=[]
        res=[0]*len(temperatures)
        for i in range (len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                x=stack.pop()
                res[x]=i-x
                print("Removed ",x," from stack and added ",i)
            stack.append(i)
            print ("Added ",i," to stack")
        return res
        