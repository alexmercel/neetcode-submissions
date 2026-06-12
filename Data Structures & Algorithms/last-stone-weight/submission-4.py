class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = sorted(stones)
        while len(arr)>1:
            print ("iter ", arr)
            a = arr.pop()
            b = arr.pop()
            if a==b:
                arr=[0]+arr
                
            else :
                arr.append(abs(a-b))
                arr.sort()
        return arr[0]

        