class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 1. keep traversing until the new height is larger
        # 2. create a stack to store index and height pairs
        # 3. if a smaller height is detected calculate area till last stack entry by popping it and insert that index into the stack
        # 4. if we reach the end check the stack and cosider the last height as 0.
        # 5. keep incrementing max height

        stack=[]
        maxArea=0
        n=len(heights)
        for i in range (n):
            if not stack or stack[-1][1]<heights[i]:
                stack.append([i,heights[i]])
                maxArea=max(maxArea,heights[i])
                print ("Adding index,height to stack as it is greater than previous: ",[i,heights[i]])
                print ("Current Max area is: ",maxArea)
                print ("Stack = ", stack)
            temp=[]
            while stack and stack[-1][1]>heights[i]:
                temp=stack.pop()
                area=temp[1]*(i-temp[0])
                maxArea=max(area,maxArea)
                print ("We hit a smaller height, however current max area is: ", maxArea)
                
            if temp:
                stack.append([temp[0],heights[i]])
            print ("Stack is: ",stack)

        for index, height in stack:
            maxArea = max(maxArea, height * (n - index))
        return maxArea

