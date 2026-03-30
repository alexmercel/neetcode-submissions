class Solution:
    def trap(self,height: List[int],area=0) -> int:
        prefixmax=[0]
        suffixmax=[0]
        m=0
        n=0
        for i in range(len(height)):
            if height[i]>=m:
                prefixmax.append(height[i])
                m=height[i]
            if height[i]<m:
                prefixmax.append(m)
            if height[len(height)-i-1]>=n:
                suffixmax.append(height[len(height)-i-1])
                n=height[len(height)-i-1]
            if height[len(height)-i-1]<n:
                suffixmax.append(n)

        prefixmax,suffixmax= prefixmax[0:-1],suffixmax[-1::-1]
        print (prefixmax,suffixmax)
        a=0
        for i in range(len(height)-1):
            area=min(prefixmax[i],suffixmax[i])-height[i]
            print (prefixmax[i],suffixmax[i],height[i])
            if area>0:
                a+=area
            print (a)
        return a
