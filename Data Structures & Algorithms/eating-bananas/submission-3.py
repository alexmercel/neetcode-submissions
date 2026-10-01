import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time to finish one pile = pile height/k ceil
        def time(h,k):
            return math.ceil(h/k)
        mink=max(piles)
        r=max(piles)
        l=1
        while l<=r:
            mid=(l+r)//2
            t=0
            for i in piles:
                t+=time(i,mid)
            if t<=h:
                mink=min(mink,mid)
                r=mid-1
            else:
                l=mid+1
        return mink

        