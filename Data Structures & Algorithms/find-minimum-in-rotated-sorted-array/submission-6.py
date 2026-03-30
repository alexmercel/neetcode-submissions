class Solution:
    def findMin(self, nums: List[int]) -> int:
        m=len(nums)-1
        n=0
        ans=0
        while n<m:
            k= n + (m-n)//2
            if nums[k]>nums[n]:
                n=k
                print("discarding: ",nums[0:n])
            else:
                print("discarding: ",nums[k:m])
                m=k
                if k==len(nums)-1:
                    return nums[0]
                if nums[k]>nums[k+1]:
                    print("Found inversion:", k+1)
                    ans=k+1

        return nums[ans] 
        