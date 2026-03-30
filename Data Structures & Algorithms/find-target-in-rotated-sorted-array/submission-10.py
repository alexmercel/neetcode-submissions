class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)-1
        m=0
        ans=-1
        while m<=n:
            k= m + (n-m)//2
            if target==nums[k]:
                return k

            if nums[m]<=nums[k]:
                # if the left half is sorted
                if nums[m]<=target<nums[k]:
                    n=k-1
                else:
                    m=k+1
            else:
                #the right half is sorted
                if nums[k]<target<=nums[n]:
                    m=k+1
                else:
                    n=k-1
        return -1

        