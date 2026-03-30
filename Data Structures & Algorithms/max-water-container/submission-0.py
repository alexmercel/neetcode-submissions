class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        index=[]
        left=0
        right=len(heights)-1
        while left<right:
            temp= (right-left)*(min(heights[left],heights[right]))
            if temp>maxarea:
                maxarea=temp
                index=[left,right]
            if heights[left]>=heights[right]:
                right-=1
            elif heights[right]>heights[left]:
                left+=1
        return maxarea