class MedianFinder:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, num: int) -> None:
        self.insert(self.arr,num,0,len(self.arr)-1)
        

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            return (self.arr[(len(self.arr)//2)-1]+self.arr[len(self.arr)//2])/2
        else:
            return (self.arr[len(self.arr)//2])
        
    def insert(self,arr,x,left,right):
        if left>right:
            arr.insert(left,x)
            return
        
        mid = (left + right)//2
        if x > arr[mid]:
            self.insert(arr,x,mid+1,right)
        else:
            self.insert(arr,x,left,mid -1)
        
        