from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count=defaultdict(int)
        res=0
        fmax=0
        for i in range (len(s)):
            count[s[i]] += 1  
            fmax=max(count.values())

            while (((i-l+1) - fmax) > k):
                count[s[l]]-=1
                l+=1
            res=max(res,i-l+1)
        return res
