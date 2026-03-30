class Solution:
    

    def search(self, nums: List[int], target: int) -> int:
        
        def binSearch(l,r,nums,target):
                if l > r:
                    return -1
                m = l + ( r - l ) // 2
                if nums[m]==target:
                    return m
                if nums[m]<target:
                    return binSearch(m + 1,r,nums,target)
                return binSearch(l,m - 1,nums,target)


        return binSearch(0,len(nums)-1,nums,target)