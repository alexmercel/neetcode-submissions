class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for i in matrix:
            flat+=i
        r = len(flat)-1
        l=0
        while l<=r:
            mid=(r+l)//2
            if flat[mid] == target:
                return True
            elif flat[mid] > target:
                r=mid-1
            else:
                l=mid+1
        return False