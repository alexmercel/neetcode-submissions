import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        n=1
        ans=m
        while n<m:
            k= n+ (m-n)//2
            hourstaken=0
            for i in piles:
                hourstaken += math.ceil(i/k)
            print ("Hours taken: ", hourstaken, "for k:", k)
            if hourstaken > h:
                n=k+1
            else:
                m=k
                ans=min(ans,k)
        return ans
            
