class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = sorted(stones)
        while len(arr)>1:
            if arr[-1]==arr[-2]:
                arr=[0]+arr[:-2]
                
            else :
                arr=arr[:-2]+[abs(arr[-1]-arr[-2])]
                arr.sort()
        return arr[0]

        