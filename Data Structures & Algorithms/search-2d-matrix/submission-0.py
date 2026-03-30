class Solution:
    def mIndex(self,m,i):
        row=i//(m)
        col=i%(m)
        res=[row,col]
        return res

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,l=len(matrix[0])*len(matrix)-1,0
        print (l,r)
        while l<=r:
            m = l + (r-l)//2
            mi = self.mIndex(len(matrix[0]),m)
            print (m,mi)
            if matrix[mi[0]][mi[1]] == target:
                return True
            if matrix[mi[0]][mi[1]] < target:
                l=m+1
            if matrix[mi[0]][mi[1]] > target:
                r=m-1
        return False


