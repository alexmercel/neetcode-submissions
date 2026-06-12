import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in points:
            heap.append([self.getDistance(i),i])
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result



    def getDistance(self, point: List[int]) -> int :
        return (point[0]**2 + point[1]**2)**(1/2)