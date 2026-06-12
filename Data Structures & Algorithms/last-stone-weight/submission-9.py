import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #create a maxheap
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)

            if a != b:
                heapq.heappush(stones, a-b)
            else:
                heapq.heappush(stones,0)

        return -stones[0]


        