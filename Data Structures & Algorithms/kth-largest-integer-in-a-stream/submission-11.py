import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = sorted(nums)
        self.k = k
        while len(self.min_heap)>k:
            self.min_heap.pop(0)
        heapq.heapify(self.min_heap) 
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.k:
            heapq.heappop(self.min_heap)
        return (self.min_heap[0])
        

