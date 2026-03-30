class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixsum=[1]
        suffixsum=[1]
        res=[]
        a=1
        b=1
        for i in range (1,len(nums)):
            a=a*nums[i-1]
            b=b*nums[len(nums)-i]
            prefixsum.append(a)
            suffixsum.append(b)
        for i in range (len(nums)):
            res.append(prefixsum[i]*suffixsum[len(nums)-i-1])
        return res