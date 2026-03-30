from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)
        for i in nums:
            res[i] += 1

        op=[]
        for i in range(k):
            op.append(max(res, key=res.get))
            del res[max(res, key=res.get)]
        
        return op